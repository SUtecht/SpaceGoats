import datetime
from ffxiv.models import *

def characters(request):
    characters = Character.objects.all()
    return dict(characters=characters)

def levels(request):
    levels = Level.objects.filter(level__exact='50')
    return dict(levels=levels)
