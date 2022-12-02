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
from utility import c_err
import time

class Backend():
  program = None
  vh = Vehicle()
  traffic = Vehicle()
  road = {"left": 0, "right": 0}
  maximum_road_deviation = 2
  traffic_exists = False

  def __init__(self, program):
    self.program = program

  def start_backend(self):
    print "DEBUG: start_backend"
    if self.program.data_gen_on == True:
      self.generate_data()
  
  def stop_backend(self):
    print "DEBUG: stop_backend: sys.exit(0)"
    sys.exit(0)

  def get_vehicle_stats(self):
    return "\n\nrunning: {}\ndirection: {}\nspeed: {}\nstate: {}\nlast action: {}".format(self.vh.running, self.vh.direction, self.vh.speed, self.vh.state, "None" if len(self.vh.action_history) == 0 else self.vh.action_history[-1])

  def get_traffic_stats(self):
    stats = "\n\nrunning: {}\ndirection: {}\nspeed: {}\nstate: {}\nlast action: {}".format(self.traffic.running, self.traffic.direction, self.traffic.speed, self.traffic.state, "None" if len(self.traffic.action_history) == 0 else self.traffic.action_history[-1])
    return stats

  def control_vehicle_system(self):
    # called by generate_data
    # 
  
  def generate_road(self):
    # called by generate_data
    # this is obviously heavily simplified due to time constraints
    
    # 10% chance for road to deviate slightly (and trigger LKA)
    road_deviation_chance = random.randint(0, 100)
    print "road deviation chance: {}".format(road_deviation_chance)
    if road_deviation_chance <= 10:
      print "road deviated"
      # only left (0) or right (1), to imitate a turn
      left_or_right = random.randint(0, 1)

      if left_or_right == 0:
        # left deviation
        r_left = random.randint(0, maximum_deviation)
        print "LEFT deviation: {}".format(r_left)
      else:
        # right deviation
        r_right = random.randint(0, maximum_deviation)
        print "RIGHT deviation: {}".format(r_right)

      road = {"left": r_left, "right": r_right}
      print "road: {}, {}".format(road["left"], road["right"])

  def generate_traffic(self):
    # called by generate_data
    # generate traffic will run every update_tick - set in Program class
    top_traffic_speed = 100
    # set car to do random things (AEB & ACC)

    # 10% chance to accelerate a random amount
    traffic_accel_chance = random.randint(0, 100)
    if traffic_accel_chance <= 10:
      val = random.randint(1, top_traffic_speed)
      #print "accel {}".format(val)
      if self.traffic.speed + val >= top_traffic_speed:
        self.traffic.speed = top_traffic_speed
      else:
        self.traffic.accelerate(val)
    
    # 10% chance to brake a random amount
    traffic_brake_chance = random.randint(0, 100)
    if self.traffic.speed > 0 and traffic_brake_chance <= 10:
      val = random.randint(1, self.traffic.speed)
      if self.traffic.speed - val <= 0:
        #print "brake {}".format(val)
        self.traffic.speed = 0
      else:
        #print "brake {}".format(val)
        self.traffic.brake(val)

    # 10% chance to full stop
    traffic_fullstop_chance = random.randint(0, 100)
    if traffic_fullstop_chance <= 5:
      #print "full stop"
      self.traffic.brake(self.traffic.speed)
    
    # print current speed
    #print "speed: {}".format(self.traffic.speed)
  
  # runs every X - set in main.py
  def generate_data(self):
    while not self.program.stop_event.is_set() and self.program.data_gen_on:
      self.generate_road()
      self.generate_traffic()
      print "DEBUG: backend generate_data tick"
      time.sleep(self.program.update_tick)
    self.stop_backend()

