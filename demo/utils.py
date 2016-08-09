import requests


def update_character(char):
    print "Getting info for: {}".format(char.name)
    try:
        r = requests.get('https://us.api.battle.net/wow/data/character/classes?locale=en_US&apikey=pyzc93kv2jdvpbswygb5h2cqvrjy6uhw')
        classes = r.json()['classes']

        r = requests.get('https://us.api.battle.net/wow/character/{}/{}?fields=items&locale=en_US&apikey=APIKEY'
                         .format(char.server, char.name))
        character = r.json()

        char.level = character['level']
        char.ilvl = character['items']['averageItemLevel']
        for class_name in classes:
            if character['class'] == class_name['id']:
                name = class_name['name']
                if name == 'Demon Hunter':
                    name = 'Demon_Hunter'
                char.class_name = name

        char.save()
    except Exception as e:
        print "There was an error getting!"
        return e
