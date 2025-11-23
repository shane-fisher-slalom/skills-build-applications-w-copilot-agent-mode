from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.assertEqual(team.name, 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Superheroes')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team, is_superhero=True)
        self.assertEqual(user.name, 'Superman')
        self.assertTrue(user.is_superhero)

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-11-23', points=10)
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.points, 10)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body strength')
        self.assertEqual(workout.name, 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, month='November')
        self.assertEqual(leaderboard.total_points, 100)
