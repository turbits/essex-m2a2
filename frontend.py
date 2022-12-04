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

from title import title_art
from utility import get_choice, c_err
import sys

class Frontend():
  program = None

  def __init__(self, program):
    self.program = program

  def main_menu(self):
    main_choices = ('Start Simulation', 'Stop Simulation', 'Show Vehicle Functions', 'Show Backend Data Stream', 'Exit')
    print title_art
    
    print "---\nData Generation Running: {}\n---".format("Yes" if self.program.data_gen_on else "No")

    ch = get_choice(main_choices)
    print ch
    if ch in ['exit', 4]:
      self.program.stop_event.set()
      print "Exiting program..."
      self.program.stop()
    elif ch in ['start simulation', 0]:
      self.program.start_data_generation()
      return self.main_menu()
    elif ch in ['stop simulation', 1]:
      self.program.stop_data_generation()
      return self.main_menu()
    elif ch in ['show vehicle functions', 2]:
      pass
    elif ch in ['show backend data stream', 3]:
      if self.program.data_gen_on:
        self.program.backend.show_data_stream()
      else:
        c_err("AVS-BAK-COMM", "DATA GENERATION IS OFF")
        return self.main_menu()
    return self.main_menu()

  def start_frontend(self):
    print "DEBUG: start_frontend"
    return self.main_menu()
