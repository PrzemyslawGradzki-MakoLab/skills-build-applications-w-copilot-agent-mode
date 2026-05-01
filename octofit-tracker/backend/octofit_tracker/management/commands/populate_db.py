from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data safely (avoid unhashable errors)
        Leaderboard.objects.exclude(pk=None).delete()
        Activity.objects.exclude(pk=None).delete()
        Workout.objects.exclude(pk=None).delete()
        User.objects.exclude(pk=None).delete()
        Team.objects.exclude(pk=None).delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(email='tony@stark.com', username='IronMan', team=marvel),
            User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel),
            User.objects.create(email='bruce@wayne.com', username='Batman', team=dc),
            User.objects.create(email='clark@kent.com', username='Superman', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Cardio', difficulty='Medium'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Pushups', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Running', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Pushups', duration=20, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Running', duration=60, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=80, rank=3)
        Leaderboard.objects.create(user=users[3], score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
