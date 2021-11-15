from config.celery import app
from celery import shared_task
from celery import shared_task
from datetime import datetime



@shared_task(name = "print_msg_main")
def print_message():
  print(f"Celery is working!! Message is ")

@shared_task(name = "print_time")
def print_time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(f"Current Time is {current_time}")
  