import datetime
from ffxiv.models import *

def characters(request):
    characters = Character.objects.all()
    return dict(characters=characters)
