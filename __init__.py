import time
from datetime import datetime
import json
import caldav
from caldav.elements import dav, cdav

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
        self.caldav_ = self.caldavConnect()

        # TODO Add caching
        self.cache = {} # Caching object
        self.cache = self.settings.get("cache")
        self.cacheTimeout = 0 # Last fetch from remote, timestamp
        # self.ticker = self.settings.get("checkInterval") # Every X minutes, check if an appointment is near and warn the user

        
        
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

    def caldavConnect(self):
        username = self.settings.get("username")
        password = self.settings.get("password")
        protocol = self.settings.get("protocol")
        url = self.settings.get("url")
        LOGGER.info(username)

        # FIXME If a parameter is missing, the skill should warn the user and stop.
        if not username:
            LOGGER.error("No username in configuration.")
            self.speak_dialog('err.conf.username')
            return False
        elif not password:
            LOGGER.error("No password in configuration.")
            self.speak_dialog('err.conf.password')
            return False
        elif not url:
            self.speak_dialog('err.conf.url')
            return False


        caldavLink = protocol+"://"+username+":"+password+"@"+url
        LOGGER.info(caldavLink)
        obj = caldav.DAVClient(caldavLink)
        
        # Not sure how to close the connection once we are done.
        return obj
    
    # Test get an event
    @intent_file_handler('cal.appt.get.intent')
    def handle_cal_get(self, message):
        self.please_wait()

        # DateTime required
        timedate = message.data.get('timedate')

        # Calendar name *not* required
        calendar = message.data.get('calendar')

        machine_timedate = extract_datetime(timedate)

        LOGGER.info(machine_timedate)
        LOGGER.info(calendar)

        # principal = self.caldav_.principal()
        # calendars = principal.calendars()

        # r = calendars.date_search(datetime(2006,7,13,17,00,00),
        #                   datetime(2006,7,15,17,00,00))

                          
        


        LOGGER.info(calendars)

        self.speak("I don't know")
        # self.speak_dialog('cal.appt.single', {datetime: '3pm'})

    """
        Get the list of the calendars' names.
    """
    @intent_file_handler('cal.list.intent')
    def handle_cal_list(self, message):
        self.please_wait()

        principal = self.caldav_.principal()
        calendars = principal.calendars()

        listcals = list()
        totalCalendars = len(calendars)
        
        # There is at least one calendar.
        if totalCalendars > 0:
            for calendar in calendars:
                tnameRaw = calendar.get_properties([dav.DisplayName(),])
                tname = tnameRaw[dav.DisplayName.tag]
                listcals.append(tname)
            
            cals = ", ".join(listcals)

            self.speak_dialog('cal.list.calendars', data={"totalCalendars": totalCalendars, "calendars": cals}, expect_response=False)

        # There is no calendar.
        else:
            self.speak_dialog('cal.list.calendars.none', expect_response=False)


    """
        Create an appointment/event
    """
    @intent_file_handler('cal.appt.new.intent')
    def handle_cal_new(self, message):
        time = message.data.get('time')
        date = message.data.get('date')
        timedate = message.data.get('timedate')

        reminder_time = extract_datetime(timedate, now_local(), self.lang)
        self.speak('ok')
        # Date
        # Time
        # What
        # self.speak(cal.appt.new, {'time': nice_time(reminder_time),
        #                        'date': nice_date(reminder_time)})
        
    """
        Make Mycroft say something while it fetch the information remotly
        Shoudn't say that when caching is enabled, except if the cache is being refreshed
    """
    def please_wait(self):
        # TODO If caching is enabled, do not say that!
        self.speak_dialog('looking', expect_response=False)


def create_skill():
    return NextcloudSkill()

