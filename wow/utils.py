import battlenet, battlenet.enums
from battlenet import Character as BnetChar


def update_character(char):
    print("Getting info for: {}".format(char.name))
    try:
        character = BnetChar(battlenet.UNITED_STATES, 
                             char.server,
                             char.name, 
                             fields=[BnetChar.GUILD])

        char.class_name = battlenet.enums.CLASS[character.class_]
        char.level = character.level
        char.ilvl = character.equipment.average_item_level

        char.save()
    except:
        print("There was an error getting!")
