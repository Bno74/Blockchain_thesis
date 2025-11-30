from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from poll.models import Voter, VoterPvt

class Command(BaseCommand):
    help = 'Clear test user data for fresh testing'

    def handle(self, *args, **options):
        # Clear Django Users for test accounts
        test_usernames = ['voter1', 'voter2', 'voter3']
        
        for username in test_usernames:
            # Delete Django User
            if User.objects.filter(username=username).exists():
                User.objects.filter(username=username).delete()
                self.stdout.write(f'Deleted Django User: {username}')
            
            # Delete Voter record
            if Voter.objects.filter(username=username).exists():
                Voter.objects.filter(username=username).delete()
                self.stdout.write(f'Deleted Voter: {username}')
            
            # Delete VoterPvt record
            if VoterPvt.objects.filter(username=username).exists():
                VoterPvt.objects.filter(username=username).delete()
                self.stdout.write(f'Deleted VoterPvt: {username}')
        
        self.stdout.write(
            self.style.SUCCESS('Test user data cleared successfully!')
        )
        self.stdout.write('You can now register test users fresh!')


