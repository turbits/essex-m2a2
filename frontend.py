# +===================================================================+
# Frontend - cli
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2, Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

from title import title_art
from utility import get_choice
import sys

class Frontend():
  program = None

  def __init__(self, program):
    self.program = program


  def main_menu(self):
    main_choices = ('Start Simulation', 'Stop Simulation', 'Vehicle Functions', 'Backend Data', 'Exit')
    print title_art
    
    print "---\nData Generation Running: {}\n---".format("Yes" if self.program.data_gen_on else "No")

    ch = get_choice(main_choices)
    if ch in ['exit', 4]:
      self.program.stop_event.set()
      print "Exiting program..."
      sys.exit(0)
    elif ch in ['start simulation', 0]:
      self.program.start_data_generation()
      return self.main_menu()
    elif ch in ['stop simulation', 1]:
      self.program.stop_data_generation()
      return self.main_menu()
    elif ch in ['vehicle functions', 2]:
      pass
    elif ch in ['backend data', 3]:
      pass

    return self.main_menu()

  def start_frontend(self):
    print "DEBUG: start_frontend"
    return self.main_menu()
