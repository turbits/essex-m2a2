# +===================================================================+
# tests.py - testing of program
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2 (OOP_PCOM7E), Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

import unittest
from lib.vehicle import Vehicle

# case 1: test vehicle creation and functions
class VehicleFunctionsCase(unittest.TestCase):
  def setUp(self):
    self._vehicle = Vehicle()

  def tearDown(self):
    self._vehicle = None

  # Start vehicle
  def testStart(self):
    self._vehicle.start()
    self._vehicle.start()
    self.assertEqual(self._vehicle.running, True)
  
  # Stop vehicle
  def testStop(self):
    self._vehicle.stop()
    self.assertEqual(self._vehicle.running, False)

  # Accelerate vehicle by 4.45 and maintain
  def testMaintain(self):
    self._vehicle.accelerate(4.45)
    self._vehicle.maintain()
    self.assertEqual(self._vehicle.speed, 4.45)

  # Accelerate vehicle by 4.45
  def testAccelerate(self):
    self._vehicle.accelerate(4.45)
    self.assertEqual(self._vehicle.speed, 4.45)

  # Decelerate vehicle by 4.45
  def testDecelerate(self):
    self._vehicle.accelerate(4.45)
    self._vehicle.decelerate(4.45)
    self.assertEqual(self._vehicle.speed, 0)

if __name__ == '__main__':
  unittest.main()
