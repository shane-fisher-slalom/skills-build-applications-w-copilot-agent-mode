from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date(), points=10)
        Activity.objects.create(user=users[1], type='Walking', duration=45, date=timezone.now().date(), points=8)
        Activity.objects.create(user=users[2], type='Strength Training', duration=60, date=timezone.now().date(), points=15)
        Activity.objects.create(user=users[3], type='Running', duration=25, date=timezone.now().date(), points=9)
        Activity.objects.create(user=users[4], type='Walking', duration=40, date=timezone.now().date(), points=7)
        Activity.objects.create(user=users[5], type='Strength Training', duration=55, date=timezone.now().date(), points=14)

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        workout2 = Workout.objects.create(name='Sprints', description='Cardio workout')
        workout1.suggested_for.set([users[0], users[3]])
        workout2.suggested_for.set([users[1], users[4]])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=33, month='November')
        Leaderboard.objects.create(team=dc, total_points=30, month='November')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
