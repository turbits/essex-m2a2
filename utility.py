# +===================================================================+
# utility.py - helper functions
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2, Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

prompt = "$"

# https://stackoverflow.com/a/1695250
def enum(**enums):
  return type('Enum', (), enums)

def c_err(code, msg):
  print "ERROR: {}\n{}".format(code, msg)
  return

def get_choice(list):
  for count, value in enumerate(list):
    print "{}: {}".format(count, value)

  user_input = raw_input("{} ".format(prompt))
  for count, value in enumerate(list):
    if user_input == value or int(user_input) == count:
      return value
  
  print c_err("AVS-FRO-USER", "Invalid choice, please try again")
  return get_choice(list)
