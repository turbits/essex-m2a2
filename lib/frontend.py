# +===================================================================+
# Frontend - cli
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2 (OOP_PCOM7E), Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

import sys
from lib.title import title_art
from lib.utility import get_choice, c_err

class Frontend():
  program = None

  def __init__(self, program):
    self.program = program

  def main_menu(self):
    main_choices = ('Start Simulation', 'Stop Simulation', 'Show Backend Data Stream', 'Hide Backend Data Stream', 'Exit')
    print title_art
    
    print "---\nData Generation Running: {}\n---".format("Yes" if self.program.data_gen_on else "No")

    ch = get_choice(main_choices)
    print ch
    if ch in ['q', 'exit', 4]:
      # exit program
      self.program.stop_event.set()
      print "Exiting program..."
      self.program.stop()
    elif ch == 0:
      # start simulation
      self.program.start_data_generation()
      return self.main_menu()
    elif ch == 1:
      # stop simulation
      self.program.stop_data_generation()
      return self.main_menu()
    elif ch == 2:
      # show backend data stream
      self.program.backend.show_data_stream()
      return self.main_menu()
    elif ch == 3:
      # hide backend data stream
      if self.program.data_gen_on:
        self.program.backend.hide_data_stream()
      else:
        c_err("AVS-BAK-COMM", "DATA GENERATION IS OFF")
        return self.main_menu()
    return self.main_menu()

  def start_frontend(self):
    print "DEBUG: start_frontend"
    return self.main_menu()
