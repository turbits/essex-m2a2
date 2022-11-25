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
from vehicle import Vehicle
from frontend import Frontend
from backend import Backend

def main():
  vh = Vehicle()
  stats = {}

  program_running = True
  frontend = Frontend(vh)
  backend = Backend(vh)
  update_tick = 1 # update every X seconds

  while program_running:
    frontend.update()
    backend.update()
    
    # update interval
    time.sleep(update_tick)

main()
