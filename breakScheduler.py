##contains the breakSlots class
from employee import *
import ast
from breakSlots import *

class breakSlots:
    slotsIndexes = slots
    name = ""
    breakArr = [0]
    emps = []
    dispRow = 0
    dispCol = 0
    
    def __init__(self, breakArrLen, name, row, col):
        self.breakArr = self.breakArr * breakArrLen
        self.name = name
        self.emps = []
        self.dispRow = row
        self.dispCol = col
        
    def resetBreaks(self):
        breakArrLen = len(self.breakArr)
        self.breakArr = [0] * breakArrLen
    
    def assignRestBreak(self, emp, optTime, attempts):
        ##if breakArr[i] = 0, break is open
        ##breakArr[i] = 1, break is taken but can be overlapped by 15 mins by pricer
        ##breakArr[i] = 2, break is taken by pricer
        empEndTime = emp.getEndTime()
        empSA = emp.getAttribute()
        empMarker = 1
        
        if empSA == 'Pricer':
            empMarker = 2
            
        print("optTime: " + str(optTime))
        breakSlot = self.slotsIndexes.get(optTime)
        if breakSlot == None:
            if attempts == 4:
                ##begin looking for slot before optimal time
                return self.assignRestBreak(emp, optTime - 75, attempts + 1)
            elif attempts < 8:
                return self.assignRestBreak(emp, optTime - 25, attempts + 1)
            else:
                print("Could not find suitable break.")
                return -1
        
        if optTime < empEndTime-100:
            ##Checking break isn't scheduled within 1 hour of end time
            if int(self.breakArr[breakSlot]) == 0:
                #print("Found suitable break at " + str(optTime))
                ##found suitable rest break
                self.breakArr[breakSlot] = empMarker
                return optTime
            else:
                if attempts < 4:
                    ##look for slot after optimal time
                    return self.assignRestBreak(emp, optTime + 25, attempts + 1)
                elif attempts == 4:
                    ##begin looking for slot before optimal time
                    return self.assignRestBreak(emp, optTime - 75, attempts + 1)
                elif attempts < 8:
                    return self.assignRestBreak(emp, optTime - 25, attempts + 1)
                else:
                    print("Could not find suitable break.")
                    return -1
        else:
            if attempts == 4:
                ##begin looking for slot before optimal time
                return self.assignRestBreak(emp, optTime - 75, attempts + 1)
            elif attempts < 8:
                return self.assignRestBreak(emp, optTime - 25, attempts + 1)
            else:
                print("Could not find suitable break.")
                return -1
    
    def assignMealBreak(self, emp, optTime, attempts):
        empStartTime = emp.getStartTime()
        breakSlot = self.slotsIndexes.get(optTime)
        empSA = emp.getAttribute()
        empMarker = 1
        if empSA == 'Pricer':
            empMarker = 2
            print("Pricer")
            
        print("Looking for lunch for " + emp.getName())
        
        if optTime <= empStartTime + 450:
            print("before 5 hrs")
            ##Checking break isn't scheduled within 1 hour of end time
            if (int(self.breakArr[breakSlot]) == 0) and (int(self.breakArr[breakSlot+1]) == 0):
                ##found suitable rest break
                print("Found totally open lunch")
                self.breakArr[breakSlot] = empMarker
                self.breakArr[breakSlot+1] = empMarker
                print(optTime)
                return optTime
            elif ((int(self.breakArr[breakSlot]) == 0) and (int(self.breakArr[breakSlot+1]) == 1)) or ((int(self.breakArr[breakSlot]) == 1) and (int(self.breakArr[breakSlot+1]) == 0)): 
                print("Found semi-Open")
                if empMarker == 2:
                    ##found suitable rest break
                    print("Found overlapping time")
                    self.breakArr[breakSlot] = empMarker
                    self.breakArr[breakSlot+1] = empMarker
                    print(optTime)
                    return optTime
                else:
                    if attempts < 4:
                        ##look for slot after optimal time
                        return self.assignMealBreak(emp, optTime + 25, attempts + 1)
                    elif attempts == 4:
                        ##begin looking for slot before optimal time
                        return self.assignMealBreak(emp, optTime - 75, attempts + 1)
                    elif attempts < 8:
                        return self.assignMealBreak(emp, optTime - 25, attempts + 1)
                    else:
                        print("Could not find suitable lunch.")
                        return -1
            elif ((int(self.breakArr[breakSlot]) == 0) and (int(self.breakArr[breakSlot+1]) == 2)) or ((int(self.breakArr[breakSlot]) == 2) and (int(self.breakArr[breakSlot+1]) == 0)): 
                print("Found semi-Open")
                if empMarker == 1:
                    ##found suitable rest break
                    print("Found overlapping time")
                    self.breakArr[breakSlot] = empMarker
                    self.breakArr[breakSlot+1] = empMarker
                    print(optTime)
                    return optTime
                else:
                    if attempts < 4:
                        ##look for slot after optimal time
                        return self.assignMealBreak(emp, optTime + 25, attempts + 1)
                    elif attempts == 4:
                        ##begin looking for slot before optimal time
                        return self.assignMealBreak(emp, optTime - 75, attempts + 1)
                    elif attempts < 8:
                        return self.assignMealBreak(emp, optTime - 25, attempts + 1)
                    else:
                        print("Could not find suitable lunch.")
                        return -1
            else:
                print("No above cases")
                if attempts < 4:
                    ##look for slot after optimal time
                    return self.assignMealBreak(emp, optTime + 25, attempts + 1)
                elif attempts == 4:
                    ##begin looking for slot before optimal time
                    return self.assignMealBreak(emp, optTime - 75, attempts + 1)
                elif attempts < 8:
                    return self.assignMealBreak(emp, optTime - 25, attempts + 1)
                else:
                    print("Could not find suitable lunch.")
                    return -1
        else:
            if attempts == 4:
                ##begin looking for slot before optimal time
                return self.assignMealBreak(emp, optTime - 75, attempts + 1)
            elif attempts < 8:
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
        
        if self.name == "Other":
            if restBreaks == 0 and mealBreaks == 0:
                return
            
            if restBreaks == 1:
                break1 = startTime + 150
            elif restBreaks > 1:
                break1 = startTime + 200
            
            if break1 == -1:
                    break1 = startTime + 200
                
            if mealBreaks > 0:
                if restBreaks == 0:
                    lunch = startTime + 250
                elif restBreaks == 1:
                    ##person is working ~6 Hours
                    lunch = break1 + 150
                    if lunch == -1:
                        lunch = break1 + 150
                elif break1 != -1:
                    lunch = break1 + 200
                    if lunch == -1:
                        lunch = break1 + 200
                else:
                    lunch = -1
                
            if restBreaks >= 2:
                if lunch != -1:
                    break2 = lunch + 200
                    if break2 == -1:
                        break2 = lunch + 200
                else:
                    break2 = startTime + 600
                    if break2 == -1:
                        break2 = startTime + 600
                
            break1 = toHM(break1)
            lunch = toHM(lunch)
            break2 = toHM(break2)
            emp.assignBreaks(break1, lunch, break2)
        
        print("Name: " + emp.name + " Start: " + str(startTime))
        
        if restBreaks == 0 and mealBreaks == 0:
            return
        
        if restBreaks == 1:
            break1 = self.assignRestBreak(emp, startTime + 150, 0)
            if break1 == -1:
                break1 = startTime + 150
        elif restBreaks > 1:
            break1 = self.assignRestBreak(emp, startTime + 200, 0)
            if break1 == -1:
                break1 = startTime + 200
            
        if mealBreaks > 0:
            if restBreaks == 0:
                lunch = self.assignMealBreak(emp, startTime + 250, 0)
                if lunch == -1:
                    lunch = startTime + 250
            elif restBreaks == 1:
                ##person is working ~6 Hours
                lunch = self.assignMealBreak(emp, break1 + 150, 0)
                if lunch == -1:
                    lunch = break1 + 150
            elif break1 != -1:
                lunch = self.assignMealBreak(emp, break1 + 200, 0)
                if lunch == -1:
                    lunch = break1 + 200
            else:
                lunch = -1
            
        if restBreaks >= 2:
            if lunch != -1:
                break2 = self.assignRestBreak(emp, lunch + 200, 0)
                if break2 == -1:
                    break2 = lunch + 200
            else:
                break2 = self.assignRestBreak(emp, startTime + 600, 0)
                if break2 == -1:
                    break2 = startTime + 600
            
        break1 = toHM(break1)
        lunch = toHM(lunch)
        break2 = toHM(break2)
        emp.assignBreaks(break1, lunch, break2)
        
    def getName(self):
        return self.name
        

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
    
    if time <= 12:
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
    
    if pm and (time < 1200):
        hours = hours + 1200
    
    return hours + minutes
        
