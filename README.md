# breakScheduler V1.5
This program will take a schedule for a given day and assign 15 minute and 30 minute breaks according to the duration of their shift without allowing overlapping breaks for employees within the same department.

Current functionality: <br />
-generates input fields for specified number of employees <br />
-takes user input to create employee objects containing their start time, end time, and department <br />
-calculates duration of shift, number of rest breaks and meal breaks <br />
-schedules breaks depending on number of rest breaks and meals breaks in accordance to California law without overlapping with employees in the same department <br />
 <br />
 New this version:  <br />
 -Schedule an employee to not overlap with cashiers if backup box is checked  <br />
 -color cells based on special attribute "clean"
 -allow "pricer" employees to overlap by 15 mins on their lunch with a non-pricer in the same department  <br />
 -export break schedule to excel to be printed<br />
 -allow user to open a schedule file and auto populate input fields with that information <br />

<br />
Save for some bug fixes, this project is now complete. 
