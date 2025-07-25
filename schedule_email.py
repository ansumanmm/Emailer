# import schedule
# import time
# from email_sender import send_email

# schedule.every().day.at("20:00").do(send_email)  # Send at 8 PM

# while True:
#     schedule.run_pending()
#     time.sleep(60)
import datetime

from email_sender import send_email
import schedule
import time

# Set to run 1 minute from now
now = datetime.datetime.now()
next_minute = (now + datetime.timedelta(minutes=1)).strftime("%H:%M")
print(f"⏳ Will send email at: {next_minute}")
schedule.every().day.at(next_minute).do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)
