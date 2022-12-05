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
  target_speed = 100
  # the command queue here is irrelevant really, but it was a requirement of the assignment
  # to implement a queue. the commands are queued and processed in one function call
  commands_queue = deque()
  vh = None

  def __init__(self, vehicle):
    self.vh = vehicle

  def queue_command(self, command):
    self.commands_queue.append(command)

  def run_command(self):
    self.commands_queue.popleft()

  def maintain(self):
    self.queue_command(self.vh.maintain())
    self.run_command()

  def accelerate(self):
    self.queue_command(self.vh.accelerate(self.target_speed))
    self.run_command()

  def decelerate(self):
    self.queue_command(self.vh.decelerate(self.vh.speed - self.target_speed))
    self.run_command()

  def activate(self):
    self.active = True

  def deactivate(self):
    self.active = False

  def update(self, entity):
    if self.active:
      if self.entity_in_range:
        # if target speed is greater than current speed, accelerate
        if entity.speed > self.vh.speed:
          self.accelerate()
        elif entity.speed < self.vh.speed:
          # if current speed is greater than target speed, decelerate
          self.decelerate()
        else:
          # if current speed is equal to target speed, maintain
          self.maintain()

