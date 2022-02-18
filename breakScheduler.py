##contains the breakSlots class

from employee import *
import ast

with open('breakSlots.txt') as slotsFile:
    slotsData = slotsFile.read()
    slots = ast.literal_eval(slotsData)

class breakSlots:
    slotsIndexes = slots
    name = ""
    breakArr = [0]
    emps = []
    
    def __init__(self, breakArrLen, name):
        self.breakArr = self.breakArr * breakArrLen
        self.name = name
        self.emps = []
    
    def assignRestBreak(self, emp, optTime, attempts):
        #print(emp.name)
        empEndTime = emp.getEndTime()
        breakSlot = self.slotsIndexes.get(optTime)
        #print("Checking rest break " + str(optTime) + " on attempt " + str(attempts))
        
        if optTime < empEndTime-100:
            ##Checking break isn't scheduled within 1 hour of end time
            if int(self.breakArr[breakSlot]) == 0:
                #print("Found suitable break at " + str(optTime))
                ##found suitable rest break
                self.breakArr[breakSlot] = 1
                return optTime
            else:
                if attempts < 3:
                    ##look for slot after optimal time
                    return self.assignRestBreak(emp, optTime + 25, attempts + 1)
                elif attempts == 3:
                    ##begin looking for slot before optimal time
                    return self.assignRestBreak(emp, optTime - 75, attempts + 1)
                elif attempts < 6:
                    return self.assignRestBreak(emp, optTime - 25, attempts + 1)
                else:
                    print("Could not find suitable break.")
                    return -1
        else:
            if attempts == 3:
                ##begin looking for slot before optimal time
                return self.assignRestBreak(emp, optTime - 75, attempts + 1)
            elif attempts < 5:
                return self.assignRestBreak(emp, optTime - 25, attempts + 1)
            else:
                print("Could not find suitable break.")
                return -1
    
    def assignMealBreak(self, emp, optTime, attempts):
        #print(emp.name)
        empStartTime = emp.getStartTime()
        breakSlot = self.slotsIndexes.get(optTime)
        #print("Checking meal break " + str(optTime) + " on attempt " + str(attempts))
        
        if optTime <= empStartTime + 450:
            ##Checking break isn't scheduled within 1 hour of end time
            if (int(self.breakArr[breakSlot]) == 0) and (int(self.breakArr[breakSlot+1]) == 0):
                ##found suitable rest break
                self.breakArr[breakSlot] = 1
                self.breakArr[breakSlot+1] = 1
                return optTime
            else:
                if attempts < 3:
                    ##look for slot after optimal time
                    return self.assignMealBreak(emp, optTime + 25, attempts + 1)
                elif attempts == 3:
                    ##begin looking for slot before optimal time
                    return self.assignMealBreak(emp, optTime - 75, attempts + 1)
                elif attempts < 7:
                    return self.assignMealBreak(emp, optTime - 25, attempts + 1)
                else:
                    print("Could not find suitable lunch.")
                    return -1
        else:
            if attempts == 3:
                ##begin looking for slot before optimal time
                return self.assignMealBreak(emp, optTime - 75, attempts + 1)
            elif attempts < 7:
                return self.assignMealBreak(emp, optTime - 25, attempts + 1)
            else:
                print("Could not find suitable lunch.")
                return -1
        
    def assignBreaks(self, emp):
        ##Assigns breaks
        restBreaks = emp.getRestBreaks()
        mealBreaks = emp.getMealBreaks()
        startTime = emp.getStartTime()
        break1 = 0
        lunch = 0
        break2 = 0
        
        if restBreaks == 0:
            return
        
        if restBreaks >= 1:
            break1 = self.assignRestBreak(emp, startTime + 200, 0)
            
        
        if mealBreaks > 0:
            lunch = self.assignMealBreak(emp, break1 + 200, 0)
            
        if restBreaks >= 2:
            break2 = self.assignRestBreak(emp, lunch + 200, 0)
            
        break1 = toHM(break1)
        lunch = toHM(lunch)
        break2 = toHM(break2)
        emp.assignBreaks(break1, lunch, break2)
        

##time management

def toHM(time):
    ##convert to hhmm format
    if time == 0:
        return 0
    
    minutePortion = abs(time) % 100 ##will return 00, 25, 50, or 75
    hour = time - minutePortion ##isolates the hour portion
    mm = minutePortion ##placeholder
    
    if hour > 1200:
        hour = hour - 1200
        
    if minutePortion == 00:
        ##0/4 of an hour
        mm = 0
        return int(hour / 100)
    elif minutePortion == 25:
        ##1/4 of an hour
        mm = 15
    elif minutePortion == 50:
        ##2/4 of an hour
        mm = 30
    elif minutePortion == 75:
        ##3/4 of an hour
        mm = 45
        
    hhmm = hour + mm
    
    return hhmm

def toHP(time, pm):
    ##Convert to hourportion format
    if time == 0:
        return 0
    
    if time < 13:
        ##single digit hour
        time = time * 100
        if pm:
            time = time + 1200
        return time
    
    minutes = abs(time) % 100
    hours = time - minutes
    
    if minutes == 15:
        minutes = 25
    elif minutes == 30:
        minutes = 50
    elif minutes == 45:
        minutes = 75
    
    if pm:
        hours = hours + 1200
    
    return hours + minutes
        
