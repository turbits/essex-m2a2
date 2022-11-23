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

from utility import enum

class Vehicle():

  STATES = enum(NONE="NONE", OFF="OFF", IDLE="IDLE", ACCELERATE="ACCELERATE", BRAKE="BRAKE", MAINTAIN="MAINTAIN", TURN="TURN")

  direction = 0
  speed = 0
  running = False
  action_history = []
  state = STATES.NONE

  def start(self):
    running = True

  def stop(self):
    running = False

  def accelerate(self, value):
    if value <= 0:
      return
    speed += value

  def brake(self, value):
    speed -= 0

  def turn(self, degrees):
    direction += degrees

  def append_action(self, action_name, value=0):
    print action_name
    print value
    if value == 0:
      Vehicle.action_history.append([action_name])
    else:
      Vehicle.action_history.append([action_name, value])

  def get_state(self):
    return self.state

  def set_state(self, state):
    self.state = state

vh = Vehicle()

print(vh.get_state())
vh.set_state(vh.STATES.IDLE)
print(vh.get_state())
