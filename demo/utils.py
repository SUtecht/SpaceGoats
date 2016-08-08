import requests


def update_character(char):
    print "Getting info for: {}".format(char.name)
    try:
        r = requests.get('https://us.api.battle.net/wow/character/{}/{}?fields=items&locale=en_US&apikey=APIKEY'
                         .format(char.server, char.name))
        character = r.json()

        char.level = character['level']
        char.ilvl = character['items']['averageItemLevel']

        char.save()
    except:
        print "There was an error getting!"
