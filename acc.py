# +===================================================================+
# Adaptive Cruise Control (ACC)
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2 (OOP_PCOM7E), Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

from collections import deque

class AdaptiveCruiseControl():
  active = False
  vehicle_in_range = False
  target_speed = 100
  # the command queue here is irrelevant really, but it was a requirement of the assignment
  # to implement a queue. the commands are queued and processed in one function call
  commands_queue = deque()
  vh = None

  def __init__(self, vehicle):
    self.vh = vehicle
  
  def queue_command(self, command):
    self.commands_queue.enqueue(command)
  
  def run_command(self):
    self.commands_queue.dequeue()(self)

  def maintain(self):
    self.queue_command(self.vh.maintain(self.target_speed))
    self.run_command()

  def accelerate(self):
    self.queue_command(self.vh.accelerate(self.target_speed))
    self.run_command()

  def decelerate(self):
    self.queue_command(self.vh.brake(self.vh.speed - self.target_speed))
    self.run_command()
  
  def activate(self):
    self.active = True

  def deactivate(self):
    self.active = False

  def update(self):
    if self.active:
      if self.vehicle_in_range:
        self.maintain()
      else:
        # if target speed is greater than current speed, accelerate
        if self.target_speed > self.vh.speed:
          self.accelerate()
        else:
          # if current speed is greater than target speed, decelerate
          self.decelerate()
