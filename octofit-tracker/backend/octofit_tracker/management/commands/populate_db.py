from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete all data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name)

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=steve, type='swim', duration=45, date=timezone.now())
        Activity.objects.create(user=bruce, type='cycle', duration=60, date=timezone.now())
        Activity.objects.create(user=clark, type='fly', duration=120, date=timezone.now())

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=110)
        Leaderboard.objects.create(user=clark, score=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
