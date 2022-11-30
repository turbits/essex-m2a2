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
from vehicle import Vehicle
from frontend import Frontend
from backend import Backend
from utility import get_choice

class Program():
  # threads will use this event to close
  stop_event = threading.Event()
  # instantiate our main vehicle
  vh = Vehicle()
  # update_tick dictates how quickly the simulation updates (front and backend)
  update_tick = 1
  backend = Backend(vh)
  frontend = Frontend(stop_event)

  # threading
  frontend_thread = threading.Thread(target=frontend.main_menu)
  frontend_thread.daemon = True
  
  # backend_thread = threading.Thread(target=backend.update)
  # backend_thread.daemon = True
  

  def main(self):
    self.frontend_thread.start()
    # self.backend_thread.start()
    while not self.stop_event.is_set():
      # print "program tick"
      # self.frontend.update()
      self.backend.update()
      # update interval
      time.sleep(self.update_tick)

    print "stop program"
    sys.exit(0)

prog = Program()
prog.main()
