# +===================================================================+
# Backend - generation of dummy data
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2, Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

from vehicle import Vehicle

class Backend():
  vh = None
  
  def __init__(self, vehicle):
    self.vh = vehicle

  # generate road
  def generate_road(self):
    road = {"left": 0, "right": 0} # 0,0 straight; 1,0 turning left 1deg per second


  # generate traffic
  def generate_traffic(self):
    traffic = Vehicle()
    traffic.accelerate(50.4)
  
  # update method will run every 1 second
  def update(self):
    pass
