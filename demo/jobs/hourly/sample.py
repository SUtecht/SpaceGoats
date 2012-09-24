from django_extensions.management.jobs import HourlyJob
import battlenet, battlenet.enums
from battlenet import Connection
from battlenet import Character as BnetChar

from demo.models import Character

class Job(HourlyJob):
    help = "My sample job."
    connection = None


    def get_info(self, char):
        print "Getting info for: {}".format(char.name)
        character = self.connection.get_character(battlenet.UNITED_STATES, 
                                                  'Auchindoun', 
                                                  char.name, 
                                                  fields=[BnetChar.GUILD])

        print battlenet.enums.CLASS[character.class_]
        print character.level
        print character.equipment.average_item_level


    def execute(self):
        # executing empty sample job
        print "Executing sample job now."

        self.connection = Connection()


        for char in Character.objects.all():
            self.get_info(char)






