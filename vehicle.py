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
from lka import LaneKeepingAssist
from acc import AdaptiveCruiseControl
from aeb import AutomaticEmergencyBraking
from state import State

class Vehicle():
  lka = LaneKeepingAssist()
  acc = AdaptiveCruiseControl()
  aeb = AutomaticEmergencyBraking()
  state = State()

  direction = 0 # north
  speed = 0
  running = False
  action_history = []
  current_state = State.NONE
  available_functions = ("start", "stop", "accelerate", "brake", "turn", "append_action", "get_state", "set_state")

  def start(self):
    self.running = True

  def stop(self):
    self.running = False

  def accelerate(self, value):
    if value <= 0:
      return
    self.speed += value

  def brake(self, value):
    if value <= 0:
      return
    self.speed -= value

  def turn(self, degrees):
    if value <= 0:
      return
    self.direction += degrees

  def append_action(self, action_name, value=0):
    print action_name
    print value
    if value == 0:
      self.action_history.append([action_name])
    else:
      self.action_history.append([action_name, value])

  def get_state(self):
    return self.current_state

  def set_state(self, state):
    if state not in self.state.states:
      print "not in"
      return
    self.current_state = state
    print self.current_state
    return

  def vehicle_functions(self):
    print "Vehicle Functions:"
    for count, item in enumerate(self.available_actions):
      print "{}: {}".format(count, item)
    return
    