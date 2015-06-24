#!/usr/bin/env python2
#
# This module extracts gear and calculates ilvls from the Lodestone.
# The methods used here are a bit more resilient than regexes, but not much.
# This can generally be expected to fail any time the structure of the
# lodestone is significantly altered.
#

from bs4 import BeautifulSoup


def get_gear_info(data):
    """Retrieve a list of gear from the given HTML.

    data: HTML, as a string, from a character page of the Lodestone
    returns: A dict of the gear, {'name': (slot, ilvl)}
    """

    soup = BeautifulSoup(data)

    # Elements with this class are always the "item level" element from a piece
    # of gear.
    items = soup.find_all(class_='pt3 pb3')

    gear = {}

    for i in items:
        name, slot, ilvl = get_details(i)
        gear[name] = (slot, ilvl)

    return gear


def get_details(ilvl_e):
    """Get the item name, slot and ilvl, starting from the given ilvl element.

    ilvl_e: An ilvl element
    returns: (name, slot, ilvl)
    """

    # move up to the correct parent - this is pretty flakey
    top_e = ilvl_e.parent.parent.parent.parent

    slot_e = top_e.find_all(class_='category_name')[0]
    name_e = top_e.find_all(class_='item_name')[0]

    ilvl = ilvl_e.get_text().strip()
    name = name_e.get_text().strip()
    slot = slot_e.get_text().strip()

    ilvl_int = int(ilvl.split()[2])

    return (name, slot, ilvl_int)


def calculate_ilvl(gear):
    """Calculate the ilvl of the given gear set.

    gear: A dict of gear, as returned by get_gear_info()
    returns: integer ilvl, matching that given in-game
    """

    # the item ending with text "Arm" is the MH weapon
    mh_weapon_ilvl = 0
    for i in gear:
        slot, ilvl = gear[i]
        if slot.endswith("Arm") or slot.endswith("Tool"):
            mh_weapon_ilvl = ilvl
            break

    # print mh_weapon

    count = len(gear)
    # Subtract 30 to remove the Soul Stone. This will be invalid for any
    # character that does not have a job (only a class), but that should be
    # very rare, and it's acceptable for the ilvl to be wrong in that case.
    total = sum([gear[i][1] for i in gear]) - 30

    # add in the mh weapon again if no offhand
    if count < 14:  # 14 is the item count including 2 weapons and soul stone
        total += mh_weapon_ilvl

    return total / 13


if __name__ == '__main__':
    with open("thenmal.html") as f:
        data = f.read()
    gear = get_gear_info(data)

    ilvl = calculate_ilvl(gear)
    print ilvl

    # from pprint import pprint
    # pprint(gear)
