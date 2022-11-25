# +===================================================================+
# Lane-keeping Assist (LKA)
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2, Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

class LaneKeepingAssist():
  left_distance = 1.0 #float; 1.0 being centered in lane
  right_distance = 1.0 #float; 1.0 being centered in lane
  current_drift = {'left':0,'right':0} #string,float; 
  max_drift = 2.0 #float; 2.0 being a tire is on the line
  
  def get_drift(self):
    return self.current_drift

  def correct_drift(self):
    self.set_drift('left', 0)
    self.set_drift('right', 0)

  def set_drift(self, side, value):
    for s in self.current_drift:
      if side == s:
        self.current_drift[s] = value
