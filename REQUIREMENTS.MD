# Assignment Requirements and Results

This file attempts to corrolate the requirements listed in the assignment page to the project features to provide some context on meeting these requirements.

I don't see this as counting towards the 600 word limit in the README, as it is technically a different file, and primarily to assist with navigating this project and presenting that I have (or haven't) met requirements, so hopefully this is acceptable.

## Diagrams

- Use-case, activity, class, and state transition diagrams were reworked and clarified as per feedback and development process
- Sequence diagram created based on feedback and development process

## Code Commenting and Best Practices

- Code was written in a local Python environment (as I detest Codio) using Python 2.7.15 to match Codio environment; it was uploaded to Codio and thoroughly tested to ensure functionality
- Code is commented where appropriate; over-commenting was omitted or removed in favour of self-documenting, i.e., the Vehicle "Start" method doesn't need a comment indicating it starts the vehicle
- Best practices were attempted, but I am honestly not entirely familiar with the "Pythonic" way; I am a (greater than)full-time sysadmin and primarily write PowerShell (for my job) and C# (for fun)
- Organised subsystems etc into a lib folder to keep the root folder clean

## Code

- The solution requirements were to implement three functions of autonomous vehicles; I chose three that had some overlap, but were distinct enough to demonstrate the ability to implement different types of subsystems
  - Automatic Emergency Braking: this implementation is simple, but demonstrates the ability to implement this subsystem. Given the time constraints and scope of the project, this is not a full implementation but monitors the 'traffic' vehicle and if the traffic vehicle comes to a full stop or performs an emergency stop, the autonomous vehicle will also perform an emergency stop
  - Adaptive Cruise Control: this implementation is very basic and could be improved with more time, but it does demonstrate the ability to implement a subsystem that monitors an 'entity' (the vehicle in front) and adjusts the vehicle's speed accordingly
  - ~~Lane Keeping Assist~~: this system, regrettably, is not implemented; I simply ran out of time. I did, however, code out what this subsystem could look like. I envisioned it as a simple subsystem that would monitor the distance to the sides of the road and if the vehicle was drifting out of the lane, it would adjust the steering wheel to bring the vehicle back into the center of the lane
- Application of OOP features;
  - Inheritance; 'object' in Program singleton
  - Polymorphism; not implemented in this project as I didn't see a use for it, but I am familiar with it
  - Encapsulation; honestly this is fairly half-baked in this program with scope creep and time constraints; would have liked to refactor the classes and overall program structure to be more encapsulated
  - Abstraction;
- Testing was not done from an ideal perspective, but there is a test suite. Ideally, it would have simulated the backend and done live testing, but the scope and time constraints did not allow this

## Summary

I am honestly not entirely happy with the end result here, given I was unable to implement the Lane-keeping Assist subsystem or more robust testing, and some things are a bit off (data stream printouts being incorrect in some situations), but I am OK with the progress I made and the demonstrated ability to implement the other two systems, implementing the other requirements of the project, and working out the overall functionality of the program.
I reworked several diagrams, and added a sequence diagram to demonstrate the overall flow of the program. I also added this requirements file to provide some context on the assignment requirements and how I met them as the project seemed to call for one given the complexity.
