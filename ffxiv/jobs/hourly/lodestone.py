from django_extensions.management.jobs import HourlyJob

import requests
import re

from ffxiv.models import Character, Level, Job as ZivarJob

class Job(HourlyJob):
    help = "Update ffxiv character info, from Lodestone."

    def execute(self):
        # executing empty sample job
        print "Updating ffxiv character info."

        update_all()

def update_character(c):
    headers = {
        # Pretend we're someone else!
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    }
    r = requests.get('http://na.finalfantasyxiv.com/lodestone/character/{}/'.format(c.lodestone_id), headers=headers)
    m = re.search('content="Character\s*profile\s*for\s*(.*).">', r.text)
    if m:
        print("Updating {}".format(m.group(1)))
    else:
        print("Character not found {} {}".format(c.name, c.lodestone_id))
        return
    for job in ZivarJob.objects.all():
        m = re.search('{}</td>\s*<td>(.*)</td>'.format(job.name.title()), r.text)
        if m:
            print("{} {}".format(job.name, m.group(1)))
            level, created = Level.objects.get_or_create(character=c, job=job)
            level.level = m.group(1)
            level.save()

def update_all():
    characters = Character.objects.all()
    for c in characters:
        update_character(c)


