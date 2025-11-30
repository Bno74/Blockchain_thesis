from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from poll.models import VoteAuth, Candidate, VoterList
import random

class Command(BaseCommand):
    help = 'Set up initial voting data for the application'

    def handle(self, *args, **options):
        # Create VoteAuth record
        if not VoteAuth.objects.exists():
            # Set voting to start in 1 hour and end in 24 hours
            start_time = timezone.now() + timedelta(hours=1)
            end_time = timezone.now() + timedelta(hours=24)
            
            vote_auth = VoteAuth.objects.create(
                username='admin',
                start=start_time,
                end=end_time,
                resultCalculated=False,
                prev_hash='0' * 64
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created VoteAuth: Voting starts at {start_time} and ends at {end_time}')
            )
        else:
            self.stdout.write('VoteAuth already exists')

        # Create some sample candidates
        candidates_data = [
            {'candidateID': 1, 'name': 'Zarek Tia', 'age': 45, 'party': 'Bangladesh National Party', 'criminalRecords': True},
            {'candidateID': 2, 'name': 'Nahid Islam', 'age': 52, 'party': 'National Citizen Party', 'criminalRecords': False},
            {'candidateID': 3, 'name': 'DR Shafiqur Rahman', 'age': 38, 'party': 'Independent', 'criminalRecords': False},
        ]
        
        for candidate_data in candidates_data:
            candidate, created = Candidate.objects.get_or_create(
                candidateID=candidate_data['candidateID'],
                defaults=candidate_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created candidate: {candidate.name}')
                )
            else:
                self.stdout.write(f'Candidate {candidate.name} already exists')

        # Create some sample voters in the voter list
        voters_data = [
            {'username': 'voter1', 'ph_country_code': '+1', 'phone_number': '5551234567'},
            {'username': 'voter2', 'ph_country_code': '+1', 'phone_number': '5559876543'},
            {'username': 'voter3', 'ph_country_code': '+1', 'phone_number': '5554567890'},
        ]
        
        for voter_data in voters_data:
            voter, created = VoterList.objects.get_or_create(
                username=voter_data['username'],
                defaults=voter_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created voter: {voter.username}')
                )
            else:
                self.stdout.write(f'Voter {voter.username} already exists')

        self.stdout.write(
            self.style.SUCCESS('Voting system setup completed successfully!')
        )
