from django.core.management.base import BaseCommand
from octofit_tracker import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        models.User.objects.all().delete()
        models.Team.objects.all().delete()
        models.Activity.objects.all().delete()
        models.Leaderboard.objects.all().delete()
        models.Workout.objects.all().delete()

        # Create teams
        marvel = models.Team.objects.create(name='Marvel')
        dc = models.Team.objects.create(name='DC')

        # Create users
        tony = models.User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = models.User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = models.User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = models.User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create activities
        models.Activity.objects.create(user=tony, type='Run', duration=30)
        models.Activity.objects.create(user=steve, type='Swim', duration=45)
        models.Activity.objects.create(user=bruce, type='Cycle', duration=60)
        models.Activity.objects.create(user=clark, type='Run', duration=50)

        # Create workouts
        models.Workout.objects.create(user=tony, description='Chest day', calories=500)
        models.Workout.objects.create(user=steve, description='Leg day', calories=600)
        models.Workout.objects.create(user=bruce, description='Cardio', calories=400)
        models.Workout.objects.create(user=clark, description='Strength', calories=700)

        # Create leaderboard
        models.Leaderboard.objects.create(user=tony, points=100)
        models.Leaderboard.objects.create(user=steve, points=90)
        models.Leaderboard.objects.create(user=bruce, points=95)
        models.Leaderboard.objects.create(user=clark, points=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
