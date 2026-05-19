from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        Activity.objects.create(user=tony, type='Run', duration=30)
        Workout.objects.create(user=tony, description='Chest day', calories=500)
        Leaderboard.objects.create(user=tony, points=100)

    def test_user_count(self):
        self.assertEqual(User.objects.count(), 2)
    def test_team_count(self):
        self.assertEqual(Team.objects.count(), 2)
    def test_activity_count(self):
        self.assertEqual(Activity.objects.count(), 1)
    def test_workout_count(self):
        self.assertEqual(Workout.objects.count(), 1)
    def test_leaderboard_count(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
