# +===================================================================+
# Frontend - the CLI frontend
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2, Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

class Frontend():
  vh = None
  choice = 0

  def __init__(self, vehicle):
    self.vh = vehicle

  def get_vehicle_stats(self):
    return {
      'running': self.vh.running,
      'direction': self.vh.direction,
      'speed': self.vh.speed,
      'state': self.vh.state,
      'last action': "None" if len(self.vh.action_history) == 0 else self.vh.action_history[-1]
    }
  
  def update(self):
    pass
