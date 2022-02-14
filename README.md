# breakScheduler
This program will take a schedule for a given day and assign 15 minute and 30 minute breaks according to the duration of their shift without allowing overlapping breaks for employees within the same department.

Current functionality:
-reads employees from a file containing their start, end, and department
-calculates duration of shift, number of rest breaks and meal breaks
-schedules breaks depending on number of rest breaks and meals breaks

Currently working on:
-checking the created break schedules are in accordance to California law (ex. lunch isn't finished after 5 hours into shift, last break isn't taken within 1 hour of end of shift, etc.)

Goals:
-convert between hourportion format and hh:mm format (ex. from 1650 to 4:30 and vice versa)
-create a GUI 
-create file that can export and/or print schedule
