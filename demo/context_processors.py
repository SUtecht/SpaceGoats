import datetime
from demo.models import *


def events(request):
    all_upcoming_events = Event.objects.all().filter(begin__gte = datetime.date.today())
    soon_events = all_upcoming_events.order_by('begin')[:10]
    return dict(upcoming_events=soon_events)

def raid(request):
    raids = Raid.objects.all().filter(current = True)
    return dict(raids=raids)

def bosses(request):
    raids = Raid.objects.all().filter(current = True)
    if len(raids) > 0:
        raid = raids[0]
        bosses = Boss.objects.all().filter(raid = raid).order_by('order')
        return dict(bosses=bosses)
    else:
        return {}

def gow(request):
    all_gows = Goat_of_the_Week.objects.all().order_by('-id')
    if all_gows:
        return dict(gow = all_gows[0])
    return dict(gow = None)
    
def roster(request):
    players = []
    for p in Player.objects.all():
        player = {}
        player['name'] = p.main.name
        player['class'] = p.main.class_name
        player['server'] = p.main.server.lower()
        player['ilvl'] = p.main.ilvl
        alts = []
        for a in Character.objects.filter(player=p.user):
            if a.name != p.main.name:
                alt = {}
                alt['name'] = a.name
                alt['server'] = a.server.lower()
                alt['class'] = a.class_name
                alt['ilvl'] = a.ilvl
                alts.append(alt)
        alts = sorted(alts, key=lambda x: x['ilvl'])
        alts.reverse()
        player['alts'] = alts
        players.append(player)
    players = sorted(players, key=lambda x: x['ilvl'])
    players.reverse()
    return dict(players=players)

def attending(request):
    return dict(im_attending=set(map(lambda x: x.event.id, Event_Attendee.objects.only('event'))))
