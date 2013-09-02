from django_extensions.management.jobs import HourlyJob

from demo.models import Character
from demo.utils import update_character

class Job(HourlyJob):
    help = "Update character info."

    def execute(self):
        # executing empty sample job
        print("Updating character info now.")

        for char in Character.objects.all():
            update_character(char)
