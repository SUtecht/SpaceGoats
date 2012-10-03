import datetime
from demo.models import *


def events(request):
    all_upcoming_events = Event.objects.all().filter(begin__gte = datetime.date.today())
    soon_events = all_upcoming_events.order_by('begin')[:10]
    return dict(upcoming_events=soon_events)

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
        player['alts'] = alts
        players.append(player)
    return dict(players=players)

def attending(request):
    if request.user.is_authenticated():
        my_chars = Character.objects.filter(player=request.user)
        print my_chars
        im_attending = list()
        for char in my_chars:
            atts =  Event_Attendee.objects.filter(character = char)
            for e in atts:
                im_attending.append(e.event.id)
        return dict(im_attending=im_attending)
    return dict(im_attending=None)