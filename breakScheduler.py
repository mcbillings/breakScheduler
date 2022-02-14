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
                elif attemps == 3:
                    ##begin looking for slot before optimal time
                    return self.assignRestBreak(emp, optTime - 75, attempts + 1)
                elif attempts < 5:
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
                elif attempts < 6:
                    return self.assignMealBreak(emp, optTime - 25, attempts + 1)
                else:
                    print("Could not find suitable break.")
                    return -1
        else:
            if attempts == 3:
                ##begin looking for slot before optimal time
                return self.assignMealBreak(emp, optTime - 75, attempts + 1)
            elif attempts < 6:
                return self.assignMealBreak(emp, optTime - 25, attempts + 1)
            else:
                print("Could not find suitable break.")
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
            
        emp.assignBreaks(break1, lunch, break2)
        
    
