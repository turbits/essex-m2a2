# +===================================================================+
# utility.py - helper functions
# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m2a2
# Project: Module 2 (OOP_PCOM7E), Assignment 2: System Implementation
# Course: Object Oriented Programming (OOP_PCOM7E September 2022)
# School: University of Essex
# Date: September-December, 2022
# +===================================================================+

prompt = "$"

def c_err(code, msg):
  print "ERROR: {}\nREASON: {}".format(code, msg)
  return

def get_choice(list):
  for count, value in enumerate(list):
    print "{}: {}".format(count, value)

  user_input = raw_input("{} ".format(prompt))
  if user_input == 'q':
    return 'q'
  for count, value in enumerate(list):
    if not user_input.isalnum():
      c_err("AVS-FRO-USER", "Invalid choice, please try again")
      return ""
    elif user_input == value:
      return value.lower().strip()
    elif int(user_input) == count:
      return int(count)
  # print c_err("AVS-FRO-USER", "Invalid choice, please try again")
  return get_choice(list)
