Right now my focus is to integrate contacts and calendar to Mycroft with Nextcloud.
I would like to eventually use Mycroft on my android phone, and some users might want to talk to it in their kitchen. Integrating with nextcloud would allow for a single set of skills, instead of trying to figure out how to do this on android :P and it would only work there.

I'm trying to allow flexibility in the way users would interact with the skill.

I personally have multiple calendars: Personal, Legal, Meals, Work.

What third party services, data sets or platforms will the Skill interact with?
This will need to be able to act on the already existing nextcloud API.

Are there similar Mycroft Skills already?
There are but not to specifically nextcloud to my knowledge.

What will the user Speak to trigger the Skill?
Could be many variations of things.
e.g.

Calendar skill:
what is on the calendar today
do I have anything for tomorrow
do I have any appointment 2 days
what do I have on friday

Hey mycroft, what is on the calendar today?
	You have 2 appointments today.
	You have a "legal" appointment for "Lawyer" at 1pm.
	You also have a "personal" appointment for "Groceries" at 4pm
	
Hey mycroft, do I have anything for tomorrow?
	- No, there is nothing in your callendars for tomorrow.
	- Yes, you have "Souper with Aunt Laura" at 5pm.
	
Hey mycroft, do I have any appointment 2 days?
	- In 2 days, saturday october 15th, your calendar is empty.
	- In 2 days, saturday october 15th, you have 1 appointment.
	  You have a "legal" appointment for "Lawyer" at 1pm.
	  
Hey mycroft, do I have something on friday? (the next day)
	- For tomorrow, friday october 14th, your calendar is empty.
	- Yes, you do have 1 appointment for tomorrow, friday october 14th.
	  You have a "personal" appointment for "Laundry" at 11am.
	  
Hey mycroft, do I have something on friday? (in 3 days)
	- In 3 days, on friday october 14th, your calendar is empty.
	- Yes, you do have 1 appointment in 3 days, on friday october 14th.
	  You have a "Cooking" appointment for "Lasagna" at 4pm.
	  
Hey mycroft, add running to my calendar for 5am tomorrow.
Hey mycroft, set an appointment in Personal for a haircut on the 13rd at 3pm.

Contact skill:
Hey Mycroft, what is the mobile phone number of Jane Doe?
Hey Mycroft, create a new contact for John Doe. His cell phone number is 555-123-4455

Hey mycroft what are my tasks for today?
Hey mycroft play smooth jass playlist from nextcloud.
hey mycroft play avatar on tv one
hey mycroft add pickles to my shopping list.

hey mycroft add note i need to call mom
hey mycroft do i have any new emails?
hey mycroft whats new in my technology news.

What phrases will Mycroft Speak?
You have a “personal” appointment today for “the doctor” at “9am”
Your task “create nextcloud skill” is due today by 3pm
Playing “smooth jass” from nextcloud
Playing “avatar” on “TV 1”
“pickles” has been added to your shopping list, is this correct?
event “running” has been added to your calendar for “5am”, is this correct?
added a note “i need to call mom”, is this correct?
You have “3” new emails do you want me to read the titles?
you have “10” new stories in “technology” from your news, Do you want me to read them all?

**What Skill Settings will this Skill need to store?**
Server URL, username and password
Is the calendar skill is enabled
What is the default calendar's name if none is set (Default: Personal)
Is the contact skill enabled

Other comments?

This is just a request that i feel will open the door to a lot of integration. I don’t expect any rush order just the awareness that it would be useful to a range of users who use nextcloud.
