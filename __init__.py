import time
from datetime import datetime
import json

from padatious.intent_container import IntentContainer
#from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler
from mycroft.util.format import nice_time
from mycroft.util.format import nice_number
from mycroft.util.log import getLogger

try:
    from mycroft.util.time import to_utc, to_local
except Exception:
    import pytz


LOGGER = getLogger(__name__)

class Test(MycroftSkill):
    def __init__(self):
        super(MycroftSkill, self).__init__(name="MycroftSkill")

    @intent_file_handler('cal.appointments.single.intent')
    def handle_cal_today(self, message):
        # word = message.data.get('your_keyword')
        self.speak_dialog('cal.appointments.single', {whentime: '3pm'})

    def handle_cal_new(self, message)
        pass
        



def create_skill():
    return Test()

