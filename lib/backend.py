# +===================================================================+
# Backend - generation of dummy data
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2 (OOP_PCOM7E), Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

import sys
import random
import time
from lib.vehicle import Vehicle
from lib.utility import c_err

class Backend():
  program = None
  vh = Vehicle()
  traffic = Vehicle()
  road = {"left": 0, "right": 0}
  maximum_road_deviation = 2
  top_traffic_speed = 100
  traffic_exists = False
  print_stats = False

  def __init__(self, program):
    self.program = program

  def start_user_vehicle_simulation(self):
    # initialize ACC
    self.vh.acc.activate()
    if self.traffic_exists == True:
      self.vh.acc.target_speed = self.traffic.speed
    else:
      # set initial target speed of user vehicle ACC
      self.vh.acc.target_speed = random.randint(1, self.vh.top_speed)

  def start_backend(self):
    if self.program.data_gen_on == True:
      vh = Vehicle()
      traffic = Vehicle()
      road = {"left": 0, "right": 0}
      self.start_user_vehicle_simulation()
      self.update()

  def stop_backend(self):
    vh = None
    traffic = None
    road = None
    sys.exit(0)

  def generate_road(self):
    # called by update    
    # 10% chance for road to deviate slightly (and trigger LKA)
    road_deviation_chance = random.randint(1, 100)
    if road_deviation_chance <= 10:
      left_or_right = random.randint(0, 1)
      if left_or_right == 0:
        # left deviation
        r_left = random.randint(1, self.maximum_road_deviation)
        self.road["left"] = r_left
      else:
        # right deviation
        r_right = random.randint(1, self.maximum_road_deviation)
        self.road["right"] = r_right

  # TRAFFIC data generation
  def traffic_speed_change(self):
    speed = self.traffic.speed
    top_speed = self.top_traffic_speed
    # 20% chance of traffic changing speed
    traffic_speed_change_chance = random.randint(1, 100)
    if traffic_speed_change_chance <= 20:
      # 20% chance of traffic speeding up
      traffic_speed_up_chance = random.randint(1, 100)
      if traffic_speed_up_chance <= 20:
        # traffic speeds up
        val = random.randint(1, 10)
        if speed + val >= top_speed:
          speed = top_speed
        else:
          self.traffic.accelerate(val)
      else:
        # traffic slows down, but not if already 0
        if not speed == 0:
          val = random.randint(1, 10)
          if speed - val <= 0:
            speed = 0
          else:
            self.traffic.decelerate(val)
    else:
      # traffic does not change speed
      self.traffic.maintain()

  def traffic_emerg_stop(self):
    traffic_full_stop_chance = random.randint(1, 100)
    if traffic_full_stop_chance <= 10:
      self.traffic.aeb.emergency_brake()

  def spawn_traffic(self):
    if self.traffic_exists == False:
      # 90% chance of traffic coming into existence
      traffic_chance = random.randint(1, 100)
      if traffic_chance <= 90:
        self.traffic = Vehicle()
        self.traffic_exists = True
        self.traffic.accelerate(random.randint(1, self.top_traffic_speed))
    else:
      # traffic exists; 2% chance of traffic going away
      traffic_stop_chance = random.randint(1, 100)
      if traffic_stop_chance <= 2:
        self.traffic_exists = False
        self.traffic = None

  def get_traffic_stats(self):
    _speed_change = 0
    _speed_change_type = ""

    if self.traffic_exists == True:
      # acceleration
      if self.traffic.speed > self.traffic.last_speed:
        _speed_change = int(self.traffic.speed - self.traffic.last_speed)
        _speed_change_type = "+"
      # deceleration
      elif self.traffic.speed < self.traffic.last_speed:
        _speed_change = int(self.traffic.last_speed - self.traffic.speed)
        _speed_change_type = "-"
      # no change
      elif self.traffic.speed == self.traffic.last_speed or self.traffic.speed == 0 or self.traffic.last_speed == 0:
        _speed_change = 0
        _speed_change_type = ""

    print "TRAFFIC STATE: {}".format(self.traffic.get_state().split(" ")[0] if self.traffic_exists == True else "N/A")
    print "TRAFFIC SPEED CHANGE: {}{}".format(_speed_change_type, _speed_change)
    print "TRAFFIC SPEED: {}".format(self.traffic.speed if self.traffic_exists == True else "N/A")
    print "TRAFFIC E-STOP: {}".format(self.traffic.aeb.emergency_brake_engaged if self.traffic_exists == True else "N/A")

  def generate_traffic(self):
    # called by update
    # generate traffic will run every update_tick - set in Program class
    # traffic spawn - 30% chance of traffic coming into existence
    self.spawn_traffic()
    if self.traffic_exists == True:
      # traffic speed change - 50% chance
      self.traffic_speed_change()
      # traffic emerg stop - 10% chance
      self.traffic_emerg_stop()

  # USER VEHICLE data generation
  def get_vehicle_stats(self):
    _speed_change = 0
    _speed_change_type = ""

    if self.vh.running == True:
      # acceleration
      if self.vh.speed > self.vh.last_speed:
        _speed_change = int(self.vh.speed - self.vh.last_speed)
        _speed_change_type = "+"
      # deceleration
      elif self.vh.speed < self.vh.last_speed:
        _speed_change = int(self.vh.last_speed - self.vh.speed)
        _speed_change_type = "-"
      # no change
      elif self.vh.speed == self.vh.last_speed or self.vh.speed == 0 or self.vh.last_speed == 0:
        _speed_change = 0
        _speed_change_type = ""
    
    print "VEHICLE STATE: {}".format(self.vh.get_state().split(" ")[0] if self.vh.running == True else "N/A")
    print "VEHICLE SPEED CHANGE: {}{}".format(_speed_change_type, _speed_change)
    print "VEHICLE SPEED: {}".format(self.vh.speed if self.vh.running == True else "N/A")
    print "VEHICLE E-STOP: {}".format(self.vh.aeb.emergency_brake_engaged if self.vh.running == True else "N/A")
    print "VEHICLE ACC ACTIVE: {}".format(self.vh.acc.active if self.vh.running == True else "N/A")

  def generate_vehicle(self):
    # called by update
    # generate vehicle will run every update_tick - set in Program class
    if self.traffic_exists == True:
      self.vh.acc.entity_in_range = True
      self.vh.acc.target_speed = self.traffic.speed
      # monitor for collision
      self.vh.aeb.update(self.traffic)
    else:
      self.vh.acc.entity_in_range = False
    
    self.vh.acc.update(self.traffic)

  # DATA STREAM CONTROL
  def show_data_stream(self):
    if not self.program.data_gen_on:
      return c_err("AVS-BAK-COMM", "DATA GENERATION IS OFF")
    else:
      self.print_stats = True

  def hide_data_stream(self):
    self.print_stats = False

  # runs every X - set in main.py
  def update(self):
    if not self.program.data_gen_on:
      self.stop_backend()
    while not self.program.stop_event.is_set() and self.program.data_gen_on:
      self.generate_road()
      self.generate_traffic()
      self.generate_vehicle()
      # self.vh.aeb.update(traffic)
      if self.print_stats:
        print "\n\nSTATS: start backend update tick"
        print "TRAFFIC SPAWNED: {}".format("Yes" if self.traffic_exists == True else "No")
        print "VEHICLE RUNNING: {}".format("Yes" if self.vh.running == True else "No")
        print "-" * 50
        print "TRAFFIC STATS:"
        # get traffic stats
        self.get_traffic_stats()
        print "-" * 50
        print "USER VEHICLE STATS:"
        # get vehicle stats
        self.get_vehicle_stats()
        # self.vh.update()
        print "-" * 50
        print "STATS: end backend update tick\n\n"
        print "TO HIDE: Enter 4 to hide backend data stream"

      time.sleep(self.program.update_tick)
    self.stop_backend()

