# +===================================================================+
# Automatic Emergency Braking (AEB)
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2 (OOP_PCOM7E), Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

class AutomaticEmergencyBraking():
  collision_detected = False
  emergency_brake_engaged = False
  # did not have time to implement a distance detection/reaction system, instead this system monitors an entity in the vehicle's path and if the other vehicle full stops, the AEB system will also full stop 
  # distance_to_entity = 0
  # minimum_collision_distance = 5
  vh = None
  
  def __init__(self, vehicle):
    self.vh = vehicle

  def emergency_brake(self):
    self.emergency_brake_engaged = True
    self.vh.decelerate(self.vh.speed)
    self.vh.set_state(self.vh.state.IDLE)

  def clear_emergency_brake(self):
    self.emergency_brake_engaged = False

  def detect_collision(self, entity):
    if entity != None:
      if entity.speed == 0 or entity.aeb.emergency_brake_engaged:
        self.emergency_brake_engaged = True
        self.collision_detected = True
        self.vh.entity_detected()
      else:
        self.emergency_brake_engaged = False
        self.collision_detected = False
        self.vh.entity_detected(clear=True)
    else:
      self.emergency_brake_engaged = False
      self.collision_detected = False
      self.vh.entity_detected(clear=True)

  def update(self, entity):
    if self.detect_collision(entity):
      self.emergency_brake()
    else:
      self.clear_emergency_brake()
