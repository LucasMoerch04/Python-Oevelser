# Calendar klassen, der vil være den overordnede klasse, der styrer kalenderen
class Calendar:
    def __init__(self):
        self.__events = []  # Indkapsling af events-listen
    
    def add_event(self, event):
        # Metode til at tilføje en begivenhed til kalenderen
        self.__events.append(event)
    
    def remove_event(self, event):
        # Metode til at fjerne en begivenhed fra kalenderen
        self.__events.remove(event)
    
    def get_events(self):
        # Metode til at få en liste over alle begivenheder på kalenderen
        return self.__events

# Event klassen, der repræsenterer en begivenhed på kalenderen
class Event(Calendar):  # Nedarvning fra Calendar klassen
    def __init__(self, name, date, time):
        self.__name = name
        self.__date = date
        self.__time = time
        self.__reminders = []  # Indkapsling af reminders-listen
    
    def add_reminder(self, reminder):
        # Metode til at tilføje en påmindelse til begivenheden
        self.__reminders.append(reminder)
    
    def remove_reminder(self, reminder):
        # Metode til at fjerne en påmindelse fra begivenheden
        self.__reminders.remove(reminder)
    
    def get_reminders(self):
        # Metode til at få en liste over alle påmindelser for begivenheden
        return self.__reminders
    
    def get_name(self):
        return self.__name
    
    def get_date(self):
        return self.__date
    
    def get_time(self):
        return self.__time

# Reminder klassen, der repræsenterer en påmindelse for en begivenhed
class Reminder:
    def __init__(self, message, time):
        self.__message = message
        self.__time = time
    
    def get_message(self):
        return self.__message
    
    def get_time(self):
        return self.__time

# Opret en ny kalender
calendar = Calendar()

# Opret en ny begivenhed
event1 = Event("Møde med kollegaer", "2022-01-01", "10:00")
event2 = Event("Fødselsdag", "2022-02-01", "20:00")

# Tilføj begivenhederne til kalenderen
calendar.add_event(event1)
calendar.add_event(event2)

# Opret nye påmindelser
reminder1 = Reminder("Forbered præsentationen", "9:30")
reminder2 = Reminder("Køb gaver på vejen", "19:00")

# Tilføj påmindelserne til begivenhederne
event1.add_reminder(reminder1)
event2.add_reminder(reminder2)

# Få listen over alle begivenheder på kalenderen
events = calendar.get_events()

# Loop igennem begivenhederne og skriv deres detaljer ud
for event in events:
    print("Begivenhed:", event.get_name())
    print("Dato:", event.get_date())
    print("Tid:", event.get_time())
    
    # Få listen over alle påmindelser for begivenheden
    reminders = event.get_reminders()
    
    # Loop igennem påmindelserne og skriv deres detaljer ud
    for reminder in reminders:
        print("Påmindelse:", reminder.get_message())
        print("Tid:", reminder.get_time())