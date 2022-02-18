###This is a program that takes a day's schedule and schedules breaks according to California law

##import files/modules
from employee import *
from breakScheduler import *
import csv

##variable/list declairations
##Employee arrays
empObjs = []

##Break Objs by department
cBreaks = breakSlots(53, "Cashier")
spBreaks = breakSlots(35, "Soft Production")
ssBreaks = breakSlots(53, "Soft Stocking")
hpBreaks = breakSlots(35, "Hard Production")
hsBreaks = breakSlots(53, "Hard Stocking")
accBreaks = breakSlots(53, "ACC")
shBreaks = breakSlots(35, "Shoes")
ngBreaks = breakSlots(35, "New Goods")
bjBreaks = breakSlots(35, "Books/Jewlery")
wBreaks = breakSlots(35, "Warehouse")
oBreaks = breakSlots(53, "Other")
test = breakSlots(53, "Test")

##dictionary mapping lists to departments
departments = {"Cashier": cBreaks,
               "Soft Production": spBreaks,
               "Soft Stocking": ssBreaks,
               "Hard Production": hpBreaks,
               "Hard Stocking": hsBreaks,
               "ACC": accBreaks,
               "Shoes": shBreaks,
               "New Goods": ngBreaks,
               "Books/Jewlery": bjBreaks,
               "Warehouse": wBreaks,
               "Other": oBreaks,
               "Test": test}

def initEmps(inputFile):
    ##reading emps from csv file into employee objects
    with open(inputFile, newline='') as empfile:
        emplines = csv.reader(empfile)
        for emp in emplines:
            empObj = Employees(str(emp[0]), int(emp[1]), int(emp[2]), str(emp[3]))
            empObjs.append(empObj)

def insertionSort(arr):
    ##Using this since employees in a given day will be around 21-35
    ##will also assign each employee to their department since we're already iterating over
    ##every item
    for i in range(1, len(arr)):
        ##Sorting Stuff
        key = arr[i].getStartTime()
        keyObj = arr[i]
        
        j = i-1
        while j >= 0 and key < arr[j].getStartTime():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = keyObj


inputFile = input("Please specify input file\n")

initEmps(inputFile)
insertionSort(empObjs)

breakObjs=[cBreaks, spBreaks, ssBreaks, hpBreaks, hsBreaks, accBreaks,
           shBreaks, ngBreaks, bjBreaks, wBreaks, oBreaks, test]

for i in range(len(empObjs)):
    ##Adding to Department's Object array
    empDept = empObjs[i].getDepartment()
    deptClass = departments.get(empDept)
    
    deptClass.emps.append(empObjs[i])

schedule = open(r"output.csv", "w")

for i in range(len(breakObjs)):
    schedule.write('\n')
    schedule.write(breakObjs[i].name)
    schedule.write('\n')
    for j in range(len(breakObjs[i].emps)):
        breakObjs[i].assignBreaks(breakObjs[i].emps[j])
        schedule.write(breakObjs[i].emps[j].writeToFile())
        
schedule.close()
        
