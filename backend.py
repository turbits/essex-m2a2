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

import sys
from vehicle import Vehicle
import random
import threading

class Backend():
  vh = None
  road = {"left": 0, "right": 0} # 0,0 straight; 1,0 would be turning left 1deg per tick
  traffic_exists = False
  traffic = Vehicle()
  data_generation_active = True
  
  def __init__(self, vehicle):
    self.vh = vehicle

  def get_vehicle_stats(self):
    return "\n\nrunning: {}\ndirection: {}\nspeed: {}\nstate: {}\nlast action: {}".format(self.vh.running, self.vh.direction, self.vh.speed, self.vh.state, "None" if len(self.vh.action_history) == 0 else self.vh.action_history[-1])

  # generate data will run every X - as set in main.py
  # this is called in the backend update method
  def generate_data(self):
    top_traffic_speed = 100
    # set car to do random things (AEB & ACC)

    # 10% chance to accelerate a random amount
    traffic_accel_chance = random.randint(0, 100)
    if traffic_accel_chance <= 10:
      val = random.randint(1, top_traffic_speed)
      print "accel {}".format(val)
      if self.traffic.speed + val >= top_traffic_speed:
        self.traffic.speed = top_traffic_speed
      else:
        self.traffic.accelerate(val)
    
    # 10% chance to brake a random amount
    traffic_brake_chance = random.randint(0, 100)
    if self.traffic.speed > 0 and traffic_brake_chance <= 10:
      val = random.randint(1, self.traffic.speed)
      if self.traffic.speed - val <= 0:
        print "brake {}".format(val)
        self.traffic.speed = 0
      else:
        print "brake {}".format(val)
        self.traffic.brake(val)

    # 10% chance to full stop
    traffic_fullstop_chance = random.randint(0, 100)
    if traffic_fullstop_chance <= 5:
      print "full stop"
      self.traffic.brake(self.traffic.speed)
    
    # print current speed
    print "speed: {}".format(self.traffic.speed)
  
  def get_backend_stats(self):
    stats = "\n\nrunning: {}\ndirection: {}\nspeed: {}\nstate: {}\nlast action: {}".format(self.vh.running, self.vh.direction, self.vh.speed, self.vh.state, "None" if len(self.vh.action_history) == 0 else self.vh.action_history[-1])
    return stats


  # runs every X - set in main.py
  def update(self):
    # print "backend tick"
    self.generate_data()


