# breakScheduler V1.0.1
This program will take a schedule for a given day and assign 15 minute and 30 minute breaks according to the duration of their shift without allowing overlapping breaks for employees within the same department.

## Changes from previous version:
- Added the --noconsole tag to PyInstaller to prevent the console from running when running the executable

## Current functionality: <br />
- Generates input fields for specified number of employees <br />
- Takes user input to create employee objects containing their start time, end time, and department <br />
- Calculates duration of shift, number of rest breaks and meal breaks <br />
- Schedules breaks depending on number of rest breaks and meals breaks in accordance to California law without overlapping with employees in the same department <br />
 - Schedule an employee to not overlap with cashiers if backup box is checked  <br />
 - Color cells based on special attribute "clean"
 - Allow "pricer" employees to overlap by 15 mins on their lunch with a non-pricer in the same department  <br />
 - Export break schedule to excel to be printed<br />
 - Allow user to open a schedule file and auto populate input fields with that information <br />
