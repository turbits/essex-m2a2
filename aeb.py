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
  distance_to_entity = 0
  minimum_collision_distance = 5
  vh = None
  
  def __init__(self, vehicle):
    self.vh = vehicle

  def emergency_brake(self):
    self.vh.brake(self.vh.speed)
    self.vh.set_state(self.vh.state.IDLE)

  def detect_collision(self):
    # for row in self.detection_matrix:
    #   for cell in row:
    #     if cell == 1 and self.distance_to_entity <= self.minimum_collision_distance:
    #       return True
    # return False
    if distance_to_entity <= self.minimum_collision_distance:
      collision_detected = True
      self.vh.entity_detected(distance=distance_to_entity)
    else:
      collision_detected = False
      self.vh.entity_detected(clear=True)

  def update(self):
    if self.detect_collision():
      self.emergency_brake()
