import time
from datetime import datetime
import json

from padatious.intent_container import IntentContainer
#from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler
from mycroft.util.format import nice_time, nice_date, nice_number
from mycroft.util.parse import extract_datetime, normalize
from mycroft.util.time import to_utc, to_local, now_local
from mycroft.util.log import getLogger

# Reminder SKill: https://github.com/MycroftAI/skill-reminder/blob/19.02/__init__.py

LOGGER = getLogger(__name__)

MINUTES = 60  # seconds

## Stolen from skill-reminder
def deserialize(dt):
    return datetime.strptime(dt, '%Y%d%m-%H%M%S-%z')


def serialize(dt):
    return dt.strftime('%Y%d%m-%H%M%S-%z')

def is_today(d):
    return d.date() == now_local().date()

def is_tomorrow(d):
    return d.date() == now_local().date() + timedelta(days=1)

def contains_datetime(utterance, lang='en-us'):
    return extract_datetime(utterance)[1] != normalize(utterance)

def is_affirmative(utterance, lang='en-us'):
    affirmatives = ['yes', 'sure', 'please do']
    for word in affirmatives:
        if word in utterance:
            return True
    return False


class NextcloudSkill(MycroftSkill):
    def __init__(self):
        super(NextcloudSkill, self).__init__()
        LOGGER.debug('Nextcloud loaded')
        # Reminder checker event
        # self.schedule_repeating_event(self.__check_calender, datetime.now(),
        #                               0.5 * MINUTES, name='reminder')

    # def __check_reminder(self, message):
    #     """ Repeating event handler. Checking if a reminder time has been
    #         reached and presents the reminder. """
    #     now = now_local()
    #     handled_reminders = []
    #     for r in self.settings.get('reminders', []):
    #         dt = deserialize(r[1])
    #         if now > dt:
    #             play_wav(REMINDER_PING)
    #             self.speak_dialog('Reminding', data={'reminder': r[0]})
    #             handled_reminders.append(r)
    #         if now > dt - timedelta(minutes=10):
    #             self.add_notification(r[0], r[0], dt)
    #     self.remove_handled(handled_reminders)

    # Test get an event
    @intent_file_handler('cal.appt.single.intent')
    def handle_cal_today(self, message):
        datetime = message.data.get('datetime')
        LOGGER.debug(datetime)
        self.speak(datetime)
        # self.speak_dialog('cal.appt.single', {datetime: '3pm'})

    # Test create new event
    @intent_file_handler('cal.appt.new.intent')
    def handle_cal_new(self, message):
        time = message.data.get('time')
        date = message.data.get('date')
        datetime = message.data.get('datetime')

        reminder_time = extract_datetime(timedate, now_local(), self.lang)
        self.speak('ok')
        # Date
        # Time
        # What
        # self.speak(cal.appt.new, {'time': nice_time(reminder_time),
        #                        'date': nice_date(reminder_time)})
        



def create_skill():
    return NextcloudSkill()

