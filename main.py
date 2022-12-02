# +===================================================================+
# main.py - main function
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2, Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

import signal
from sys import stdout
import sys
import time
import threading
from title import title_art
from frontend import Frontend
from backend import Backend
from utility import get_choice

class Program(object):
  _instance = None

  data_gen_on = False
  # instantiate our main vehicle
  # update_tick dictates how quickly the simulation updates (front and backend)
  update_tick = 1
  frontend = None
  backend = None

  # THREADING
  # threads will use this event to close
  stop_event = threading.Event()
  backend_stop_event = threading.Event()
  backend_thread = None
  frontend_thread = None
  
  def __init__(self):
    raise RuntimeError("Call instance() instead")
  
  # https://python-patterns.guide/gang-of-four/singleton/
  @classmethod
  def instance(cls):
    if cls._instance is None:
      # print "Creating new instance of Program"
      cls._instance = cls.__new__(cls)
      cls._instance.frontend = Frontend(cls._instance)
      cls._instance.backend = Backend(cls._instance)
    return cls._instance

  def start_data_generation(self):
    # if data generation is turned on, create and start a backend thread
    # Thread setup; daemon = threads will die on process kill
    self.data_gen_on = True
    self.backend_thread = threading.Thread(target=self.backend.start_backend)
    self.backend_thread.daemon = True
    self.backend_thread.start()
  
  def stop_data_generation(self):
    self.data_gen_on = False

  def main(self):
    # Thread setup; daemon = threads will die on process kill
    self.frontend = Frontend(self.instance())
    self.frontend_thread = threading.Thread(target=self.frontend.start_frontend)
    self.frontend_thread.daemon = True
    self.frontend_thread.start()

      # print "program tick"
      # self.backend.update()
      # update interval
      # time.sleep(self.update_tick)
    
    while not self.stop_event.is_set():
      pass

prog = Program.instance()
prog.main()
