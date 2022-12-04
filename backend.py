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
  top_traffic_speed = 100
  traffic_exists = False
  print_stats = False

  def __init__(self, program):
    self.program = program

  def start_backend(self):
    if self.program.data_gen_on == True:
      print "DEBUG: start_backend"
      vh = Vehicle()
      traffic = Vehicle()
      road = {"left": 0, "right": 0}
      self.update()
  
  def stop_backend(self):
    # print "DEBUG: stop_backend: sys.exit(0)"
    vh = None
    traffic = None
    road = None
    sys.exit(0)

  # def get_vehicle_stats(self):
  #   return "\n\nrunning: {}\ndirection: {}\nspeed: {}\nstate: {}\nlast action: {}".format(self.vh.running, self.vh.direction, self.vh.speed, self.vh.state, "None" if len(self.vh.action_history) == 0 else self.vh.action_history[-1])

  # def get_traffic_stats(self):
  #   stats = "\n\nrunning: {}\ndirection: {}\nspeed: {}\nstate: {}\nlast action: {}".format(self.traffic.running, self.traffic.direction, self.traffic.speed, self.traffic.state, "None" if len(self.traffic.action_history) == 0 else self.traffic.action_history[-1])
  #   return stats
  
  def generate_road(self):
    # called by update    
    # 10% chance for road to deviate slightly (and trigger LKA)
    road_deviation_chance = random.randint(0, 100)
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

  def traffic_speed_change(self):
    speed = self.traffic.speed
    top_speed = self.top_traffic_speed
    # 50% chance of traffic changing speed
    traffic_speed_change_chance = random.randint(0, 100)
    if traffic_speed_change_chance <= 50:
      # 50% chance of traffic speeding up
      traffic_speed_up_chance = random.randint(0, 100)
      if traffic_speed_up_chance <= 50:
        # traffic speeds up
        val = random.randint(1, top_speed)
        if speed + val >= top_speed:
          speed= top_speed
        else:
          self.traffic.accelerate(val)
      else:
        # traffic slows down, but not if already 0
        if not speed == 0:
          val = random.randint(1, speed)
          if speed - val <= 0:
            speed = 0
          else:
            self.traffic.brake(val)
    else:
      # traffic does not change speed
      self.traffic.maintain()
  
  def traffic_emerg_stop(self):
    emerg_stop = False
    traffic_full_stop_chance = random.randint(0, 100)
    if traffic_full_stop_chance <= 10:
      self.traffic.aeb.emergency_brake()

  def spawn_traffic(self):
    if self.traffic_exists == False:
      # 70% chance of traffic coming into existence
      traffic_chance = random.randint(0, 100)
      if traffic_chance <= 70:
        self.traffic = Vehicle()
        self.traffic_exists = True
    # else:
    #   # traffic exists; 5% chance of traffic going away
    #   traffic_stop_chance = random.randint(0, 100)
    #   if traffic_stop_chance <= 5:
    #     self.traffic_exists = False
    #     self.traffic = None
  
  def get_traffic_stats(self):
    _speed_change = 0
    _speed_change_type = ""

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
    
    print _speed_change
    print _speed_change_type
    print self.traffic.speed
    print self.traffic.last_speed

    print "TRAFFIC STATE: {}".format(self.traffic.get_state().split(" ")[0] if self.traffic_exists == True else "N/A")
    print "TRAFFIC SPEED CHANGE: {}{}".format(_speed_change_type, _speed_change)
    print "TRAFFIC SPEED: {}".format(self.traffic.speed if self.traffic_exists == True else "N/A")
    print "TRAFFIC E-STOP: {}".format(self.traffic.aeb.collision_detected if self.traffic_exists == True else "N/A")
  
  def get_vehicle_stats(self):
    _speed_change = 0
    _speed_change_type = ""

    # acceleration
    if self.vh.speed > self.vh.last_speed:
      _speed_change = int(self.vh.speed - self.vh.last_speed)
      _speed_change_type = "+"
    # deceleration
    elif self.vh.speed < self.vh.last_speed:
      _speed_change = int(self.vh.last_speed - self.vh.speed)
      _speed_change_type = "-"
    # no change
    elif self.vh.speed == self.vh.last_speed:
      _speed_change = 0
      _speed_change_type = ""
    
    print "VEHICLE STATE: {}".format(self.vh.get_state().split(" ")[0] if self.vh.running == True else "N/A")
    print "VEHICLE SPEED CHANGE: {}{}".format(_speed_change_type, _speed_change)
    print "VEHICLE SPEED: {}".format(self.vh.speed if self.vh.running == True else "N/A")
    print "VEHICLE E-STOP: {}".format(self.vh.aeb.collision_detected if self.vh.running == True else "N/A")
    print "VEHICLE LKA: {}".format(self.vh.lka.deviation_detected if self.vh.running == True else "N/A")
    print "VEHICLE LKA LEFT: {}".format(self.vh.lka.current_deviation["left"] if self.vh.running == True else "N/A")
    print "VEHICLE LKA RIGHT: {}".format(self.vh.lka.current_deviation["right"] if self.vh.running == True else "N/A")
    print "VEHICLE ACC ACTIVE: {}".format(self.vh.acc.active if self.vh.running == True else "N/A")

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

  def show_data_stream(self):
    if not self.program.data_gen_on:
      return c_err("AVS-BAK-COMM", "DATA GENERATION IS OFF")

    else:
      self.print_stats = True
  
  def hide_data_stream(self):
    self.print_stats = False

  def update(self):
    if not self.program.data_gen_on:
      self.stop_backend()
    # runs every X - set in main.py
    while not self.program.stop_event.is_set() and self.program.data_gen_on:
      self.generate_road()
      self.generate_traffic()
      if self.print_stats:
        print "\n\nSTATS: start backend update tick"
        print "TRAFFIC SPAWNED: {}".format("Yes" if self.traffic_exists == True else "No")
        print "VEHICLE RUNNING: {}".format("Yes" if self.vh.running == True else "No")
        print "-" * 50
        # get traffic stats
        self.get_traffic_stats()
        print "-" * 50
        # get vehicle stats
        self.get_vehicle_stats()
        # self.vh.update()
        print "-" * 50
        print "STATS: end backend update tick\n\n"
        print "Enter any key to exit stats mode"

      time.sleep(self.program.update_tick)
    self.stop_backend()

