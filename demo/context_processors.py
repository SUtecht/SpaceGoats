import datetime
from demo.models import *


def events(request):
    all_upcoming_events = Event.objects.all().filter(begin__gte = datetime.date.today())
    soon_events = all_upcoming_events.order_by('begin')[:4]
    return dict(upcoming_events=soon_events)

def gow(request):
    all_gows = Goat_of_the_Week.objects.all().order_by('-id')
    return dict(gow = all_gows[0])
    