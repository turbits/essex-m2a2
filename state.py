# +===================================================================+
# State - vehicle
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2, Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

class State:
  NONE = "NONE"
  OFF = "OFF"
  IDLE = "IDLE"
  ACCELERATE = "ACCELERATE"
  DECELERATE = "DECELERATE"
  MAINTAIN = "MAINTAIN"
  TURN = "TURN"

  states = ("NONE", "OFF", "IDLE", "ACCELERATE", "DECELERATE", "MAINTAIN", "TURN")
