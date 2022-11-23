# +===================================================================+
# tests.py - testing of program
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2, Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

import Vehicle from Vehicle
import unittest

class VehicleAccelerationTest(unittest.TestCase):
  vehicle = new Vehicle()
  vehicle.
  # Accelerate vehicle by 4.45km/h
  def testAccelerate(self):
    self.assertEqual(vehicle.accelerate(4.45), vehicle.current_speed == 4.45)

class VehicleActionAppendTest(unittest.TestCase):
  vehicle = new Vehicle()
  
  # append an action without a value
  def testAppendNoValue(self):
    self.assertEqual(vehicle.append_action("brake"), vehicle.action_history[0] == ["brake"])

  def testAppendWithValue(self):
    self.assertEqual(vehicle.append_action("turn", 2.24), vehicle.action_history[1] == ["turn",2.24])
