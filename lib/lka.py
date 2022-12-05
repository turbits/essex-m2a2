# +===================================================================+
# Lane-keeping Assist (LKA)
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2 (OOP_PCOM7E), Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

class LaneKeepingAssist():
  left_distance = 1
  right_distance = 1
  current_deviation = {'left':0,'right':0}
  max_deviation = 1 # one unit from center, indicating lane drifting
  deviation_detected = False
  vh = None

  def __init__(self, vehicle):
    self.vh = vehicle

  def get_drift(self):
    return self.current_deviation

  def set_drift(self, side, value):
    for s in self.current_deviation:
      if side == s:
        self.current_deviation[s] = value

  def correct_drift(self):
    self.set_drift('left', 0)
    self.set_drift('right', 0)

  def update(self, road):
    # 'road' being the road defined in the Backend class, indicating road deviation
    if road["left"] >= self.max_deviation or road["right"] >= self.max_deviation:
      deviation_detected = True
      # if the road deviation is greater than the LKA's maximum_deviation on either side,
      # we should trigger LKA's drift correction to keep the car inside the lines
      correct_drift()
    else:
      deviation_detected = False
