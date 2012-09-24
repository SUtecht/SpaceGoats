from django_extensions.management.jobs import HourlyJob
from demo.models import Character

class Job(HourlyJob):
    help = "My sample job."

    def execute(self):
        # executing empty sample job
        print "Executing sample job now."
        print Character.objects.all()




