# Autonomous Vehicle System

Author: Trevor Woodman

Module: Module 2, Assignment 2: System Implementation

Course: Object Oriented Programming (OOP_PCOM7E) September 2022

School: University of Essex

## Running the Program

**Requirements**

- Python 2.7.15, or higher (_for some reason this was the version we had to use_)

**Steps to Run**

- open a CLI to the repo location
- `python main.py`

## Development Process

I began the development of this program with the previous module, available [here](https://github.com/turbits/essex-m2a1) as an essay. The overall premise was to design a partial autonomous vehicle system that contained three processes present in autonomous vehicles. I chose Lane-keeping Assist (LKA), Automatic Emergency Braking (AEB), and Adaptive Cruise Control (ACC). These three systems I felt represented separate concerns as far as autonomy in a vehicle goes, with LKA controlling the direction of the vehicle, ACC controlling cruising speed, and AEB representing one of many critical safety systems designed to assist or take over in the event of an emergency detection.

---

## Error Codes

`AVS-XYZ-123`

`AVS` - name of the program as a whole; in this program's case: AVS, Autonomous Vehicle System

`XYZ` - identifier of the system

`123` - status code

### System Identifiers

| System ID | System                                    |
| --------- | ----------------------------------------- |
| AVS       | Autonomous Vehicle System; primary system |
| VEH       | Vehicle; subsystem                        |
| LKA       | Lane-keeping Assist; subsystem            |
| AEB       | Automatic Emergency Braking; subsystem    |
| ACC       | Adaptive Cruise Control; subsystem        |
| FRO       | Frontend; subsystem                       |
| BAK       | Backend; subsystem                        |
| TST       | Testing; subsystem                        |
| UTL       | Utility; helper module                    |

### Status Codes

| Status Code | Meaning                |
| ----------- | ---------------------- |
| OK          | Generic OK             |
| BAD         | Generic BAD            |
| USER        | User input error       |
| COMM        | Communications failure |
| SYS         | Systems failure        |
