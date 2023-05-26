from flask import Flask
import threading
import os
import random

import schedule
import time
from os import system
def run_job():
 system("main.py")

# işlemi her 2 saatte bir çalıştırmak için
schedule.every(1).hours.do(run_job)

while True:
  schedule.run_pending()
  time.sleep(1)