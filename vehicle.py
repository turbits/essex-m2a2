# +===================================================================+
# Vehicle
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

class Vehicle():
  direction = 0
  speed = 0
  running = false
  action_history = deque()
  
  def start():
    pass

  def stop():
    
    pass

  def accelerate():
    pass

  def brake():
    pass

  def turn(float):
    pass

  def append_action(action_name, value=0):
    if value = 0:
      action_history.append(action_name)
    else:
      action_history.append('{}:{}'.format(action_name, value))

  def set_state(int):
    pass
