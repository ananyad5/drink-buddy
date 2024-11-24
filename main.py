import time
from plyer import notification

def reminder_function():

    notification.notify(
        title = "Water reminder",
        message = "DRINK WATER DON'T DIE",
        timeout = 10

    )

reminders = 16
interval = 40*60 #40 mins in secs

while (reminders):
    time.sleep(interval)
    reminder_function()
    reminders -= 1