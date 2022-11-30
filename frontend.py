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

class Frontend():
  stop_event = None

  def __init__(self, e):
    self.stop_event = e

  def main_menu(self):
    main_choices = ('Start Simulation', 'Stop Simulation', 'Vehicle Functions', 'Backend Data', 'Exit')
    print title_art
    ch = get_choice(main_choices)
    if ch in ['exit', 4]:
      self.stop_event.set()
    elif ch in ['start simulation', 0]:
      pass
    elif ch in ['stop simulation', 1]:
      pass
    elif ch in ['vehicle functions', 2]:
      pass
    elif ch in ['backend data', 3]:
      pass
