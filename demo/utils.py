import requests


def update_character(char):
    print "Getting info for: {}".format(char.name)
    try:
        r = requests.get('https://us.api.battle.net/wow/character/{}/{}?fields=items&locale=en_US&apikey=zpwrz24xqd8yhmhk2uv8b4qr5gv6ecef'
                         .format(char.server, char.name))
        character = r.json()

        char.level = character['level']
        char.ilvl = character['items']['averageItemLevelEquipped']

        char.save()
    except:
        print "There was an error getting!"
