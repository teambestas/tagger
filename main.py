from threading import Thread
import os

def maa():
  os.system("python main2.py")
def maaa():
  os.system("python main3.py")
  
Thread(target=maa)
Thread(target=maaa)