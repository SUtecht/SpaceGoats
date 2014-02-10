import datetime
from ffxiv.models import *

def characters(request):
    characters = Character.objects.all()
    return dict(characters=characters)

def max_levels(request):
    max_levels = Level.objects.filter(level__exact='50')
    return dict(max_levels=max_levels)
    
def levels(request):
    levels = Level.objects.extra(select={'level_num': 'CAST(level AS INTEGER)'},
                      order_by=['-level_num'])
    return dict(levels=levels)
