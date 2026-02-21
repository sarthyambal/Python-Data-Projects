import time
from player import notification


title = 'Drink Water Reminder'
message = 'Time to drink some water! Staying hydrated is important for your health.'

timeout = 10

def water_notification():
    notification.notify(
        title=title,
        message=message,
     
        timeout=timeout
    )

if __name__ == '__main__':
    while True:
        water_notification()

        time.sleep(60 * 60)
