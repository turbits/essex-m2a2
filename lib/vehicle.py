# +===================================================================+
# Vehicle
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2 (OOP_PCOM7E), Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

from lib.lka import LaneKeepingAssist
from lib.acc import AdaptiveCruiseControl
from lib.aeb import AutomaticEmergencyBraking
from lib.state import State

class Vehicle():
  lka = None
  acc = None
  aeb = None
  state = State()
  # distance_to_entity = None
  entity_in_range = False
  speed = 0
  last_speed = 0
  top_speed = 100
  running = False
  action_history = []
  current_state = State.NONE
  available_functions = ("start", "stop", "accelerate", "decelerate", "turn", "append_action", "get_state", "set_state")

  def __init__(self):
    self.start()
    # initialise subsystems
    self.lka = LaneKeepingAssist(self)
    self.acc = AdaptiveCruiseControl(self)
    self.aeb = AutomaticEmergencyBraking(self)

  def get_state(self):
    return self.current_state

  def set_state(self, state):
    if state not in self.state.states:
      c_err("AVS-VEH-BAD", "Attempted to set invalid state: {}".format(state))
      return
    self.current_state = state
  
  def entity_detected(self, clear=False):
    if clear:
      self.append_action("entity detection clear")
      entity_in_range = False
      # self.distance_to_entity = None
      return
    self.append_action("entity detection")
    entity_in_range = True
    # self.distance_to_entity = distance

  def start(self):
    self.running = True
    self.set_state(State.IDLE)
    self.append_action("start")

  def stop(self):
    self.running = False
    self.set_state(State.OFF)
    self.append_action("stop")

  def idle(self):
    self.set_state(State.IDLE)
    self.append_action("idle")

  def accelerate(self, value):
    if value <= 0:
      return
    self.last_speed = self.speed
    self.set_state(State.ACCELERATE)
    self.speed += value
    self.append_action("accelerate", value)
  
  def maintain(self):
    self.last_speed = self.speed
    self.set_state(State.MAINTAIN)
    self.append_action("maintain")

  def decelerate(self, value):
    if value <= 0:
      return
    self.last_speed = self.speed
    self.set_state(State.DECELERATE)
    self.speed -= value
    self.append_action("decelerate", value)

  def turn(self, degrees):
    if value <= 0:
      return
    self.direction += degrees
    self.set_state(State.TURN)
    self.append_action("turn", degrees)

  def append_action(self, action_name, value=0):
    if value == 0:
      self.action_history.append([action_name])
    else:
      self.action_history.append([action_name, value])
  
  def update(self, traffic_detected):
    self.lka.update(self)
    self.acc.update(self)
    self.aeb.update(self)
    if speed == 0:
      self.idle()
