from sched import scheduler
from time import time
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
from motivator import send_whatsapp_text,client,quote
import time

scheduler=BackgroundScheduler(timezone="Asia/Karachi");
scheduler.start()
job=scheduler.add_job(send_whatsapp_text,'cron',[client,quote],hour="5",minute="25")
print(job)
while True:
    time.sleep(1)
