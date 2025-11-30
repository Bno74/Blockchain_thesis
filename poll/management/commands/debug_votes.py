from django.core.management.base import BaseCommand
from poll.models import Vote, Candidate, Block, VoteAuth

class Command(BaseCommand):
    help = 'Debug the current state of votes, candidates, and blocks'

    def handle(self, *args, **options):
        self.stdout.write("=== VOTING SYSTEM DEBUG INFO ===")
        
        # Check VoteAuth
        try:
            vote_auth = VoteAuth.objects.get(username='admin')
            self.stdout.write(f"VoteAuth: start={vote_auth.start}, end={vote_auth.end}, resultCalculated={vote_auth.resultCalculated}")
        except VoteAuth.DoesNotExist:
            self.stdout.write(self.style.ERROR("VoteAuth not found!"))
        
        # Check Candidates
        candidates = Candidate.objects.all()
        self.stdout.write(f"\nCandidates ({candidates.count()}):")
        for candidate in candidates:
            self.stdout.write(f"  {candidate.name} (ID: {candidate.candidateID}): {candidate.count} votes")
        
        # Check Votes
        votes = Vote.objects.all()
        self.stdout.write(f"\nVotes ({votes.count()}):")
        for vote in votes:
            self.stdout.write(f"  Vote ID: {vote.id}, Candidate: {vote.vote}, Block ID: {vote.block_id}, Timestamp: {vote.timestamp}")
        
        # Check Blocks
        blocks = Block.objects.all()
        self.stdout.write(f"\nBlocks ({blocks.count()}):")
        for block in blocks:
            self.stdout.write(f"  Block ID: {block.id}, Merkle Hash: {block.merkle_hash[:20]}..., Nonce: {block.nonce}")
        
        # Check vote distribution
        self.stdout.write(f"\nVote Distribution:")
        for candidate in candidates:
            vote_count = votes.filter(vote=candidate.candidateID).count()
            self.stdout.write(f"  {candidate.name}: {vote_count} votes (DB count: {candidate.count})")
        
        self.stdout.write("\n=== END DEBUG INFO ===")
