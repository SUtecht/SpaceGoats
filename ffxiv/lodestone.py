import requests
import re
from ffxiv.models import *

def update_character(c):
    r = requests.get('http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(c.lodestone_id))
    m = re.search('player_name_brown">(.*)</a>', r.text)
    if m:
        print("Updating {}".format(m.group(1)))
    else:
        print("Character not found {} {}".format(c.name, c.lodestone_id))
        return
    for job in Job.objects.all():
        m = re.search('{}</td>\s*<td>(.*)</td>'.format(job.name.lower()), r.text)
        if m:
            print("{} {}".format(job.name, m.group(1)))
            level, created = Level.objects.get_or_create(character=c, job=job)
            level.level = m.group(1)
            level.save()

def update_all():
    characters = Character.objects.all()
    for c in characters:
        update_character(c)
