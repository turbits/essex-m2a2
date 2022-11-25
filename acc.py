# +===================================================================+
# Adaptive Cruise Control (ACC)
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2, Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

from collections import deque

class AdaptiveCruiseControl():
  vehicle_in_range = False #bool
  target_speed = 0
  commands_queue = deque() #string queue

  #void
  def acc_accelerate(self):
    pass

  #void
  def acc_decelerate(self):
    pass
