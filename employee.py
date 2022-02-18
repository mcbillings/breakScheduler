from breakScheduler import *

##contains the employee class
class Employees:
    name = ""
    startTime = 0
    endTime = 0
    duration = 0
    restBreaks = 0
    mealBreaks = 0
    restBreak1 = 0
    restBreak2 = 0
    mealBreak1 = 0
    department = "none"
    
    def __init__(self, n, sT, eT, dep):
        ##Initilizes employee with all necessary parameters
        self.name = n
        self.startTime = sT
        self.endTime = eT
        self.department = dep
        self.duration = eT-sT
        self.calculateBreaks()
        print(self.name + ' init complete.')
    
    def calculateBreaks(self):
        ##calculates the number of rest and meal breaks according to shift duration
        if self.duration < 350:
            ##employee works 0-3:29 hours
            self.restBreaks = 0
            self.mealBreaks = 0
            
        elif self.duration < 501:
            ##employee works 3:30-5:00 hours
            self.restBreaks = 1
            self.mealBreaks = 0
            
        elif self.duration < 1001:
            ##employee works 5:01-10:00 hours
            self.restBreaks = 2
            self.mealBreaks = 1
        else:
            ##employee works over 10 hours
            self.restBreaks = 2
            self.mealBreaks = 2
            
    def assignBreaks(self, break1, lunch, break2):
        self.restBreak1 = break1
        self.mealBreak1 = lunch
        self.restBreak2 = break2
            
    def printInfo(self):
        print('Name: ' + self.name + ' Start: ' +
              str(self.startTime) + ' End: ' + str(self.endTime) +
              ' Duration: ' + str(self.duration) + ' Dept: ' + self.department +
              ' Rest Breaks: ' + str(self.restBreaks) + ' Meal Breaks: ' + str(self.mealBreaks) +
              '\nRest Break 1: ' + str(self.restBreak1) + ' Meal Break: ' + str(self.mealBreak1) +
              ' Rest Break 2: ' + str(self.restBreak2))
        
    def writeToFile(self):
        output = self.name + ',' + str(toHM(self.startTime)) + '-' + str(toHM(self.endTime)) + ',' + str(self.restBreak1) + ',' + str(self.mealBreak1) + ',' +str(self.restBreak2) + '\n'
        
        return output
    
    def getStartTime(self):
        return self.startTime
    
    def getEndTime(self):
        return self.endTime
    
    def getRestBreaks(self):
        return self.restBreaks
    
    def getMealBreaks(self):
        return self.mealBreaks
    
    def getDepartment(self):
        return self.department