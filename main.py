###This is a program that takes a day's schedule and schedules breaks according to California law

##Author: Mikayla Billings-Alston

######################################################
######################################################
##-------------BREAK SCHEDULER----------------------##
######################################################
######################################################

##import files/modules
from employee import *
from breakScheduler import *
from tkinter import *
from tkinter import ttk, simpledialog
from Pmw import ScrolledFrame
import csv
import ctypes


##variable/list declairations
##Employee arrays
empObjs = []
breakObjs = []

def insertionSort(arr):
    ##Using insertion sort since employees in a given day will be around 21-35
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

##Break Objs by department
cBreaks = breakSlots(53, "Cashier", 7, 0)
spBreaks = breakSlots(35, "Soft Production", 0, 6)
ssBreaks = breakSlots(53, "Soft Stocking", 11, 6)
hpBreaks = breakSlots(35, "Hard Production", 6, 6)
hsBreaks = breakSlots(53, "Hard Stocking" , 18, 6)
accBreaks = breakSlots(53, "ACC", 16, 0)
shBreaks = breakSlots(35, "Shoes", 22, 0)
ngBreaks = breakSlots(35, "New Goods", 24, 0)
bjBreaks = breakSlots(35, "Books/Jewlery", 26, 0)
wBreaks = breakSlots(35, "Warehouse", 31, 6)
oBreaks = breakSlots(53, "Other", 27, 6)
test = breakSlots(53, "Test", 100, 100)

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

#################################
##----------ROOT SETUP---------##
#################################
root = Tk()
root.state("iconic")

##getting number of emps
numEmps = simpledialog.askinteger("Enter number of Employees", "Enter number of Employees")
root.state("zoomed")

#Grid configuration
Grid.columnconfigure(root, 0, weight = 4)
Grid.columnconfigure(root, 1, weight = 3)

Grid.rowconfigure(root, 0, weight = 2)
Grid.rowconfigure(root, 1, weight = 15)
Grid.rowconfigure(root, 2, weight = 3)
Grid.rowconfigure(root, 3, weight = 1)

def addEmp():
    i = len(empsNames)
    global numEmps
    numEmps += 1
    empName = Entry(empsFrame)
    empsNames.append(empName)
    empName.grid(row = i+1, column = 0, sticky = 'ew')
    
    empDept = StringVar()
    empDepartment = OptionMenu(empsFrame, empDept, *departmentsList)
    empsDepts.append(empDept)
    empDepartment.grid(row = i+1, column = 1, sticky = 'ew')
    
    empStart = Entry(empsFrame, width = 10)
    empsStart.append(empStart)
    empStart.grid(row = i+1, column = 2, sticky = 'ew')
    
    s = IntVar(value = 0)
    empSPM = Checkbutton(empsFrame, variable = s)
    empsSPM.append(s)
    empSPM.grid(row = i + 1, column = 3)
    
    empEnd = Entry(empsFrame, width = 10)
    empsEnd.append(empEnd)
    empEnd.grid(row = i+1, column = 4, sticky = 'ew')
    
    e = IntVar(value = 1)
    empEPM = Checkbutton(empsFrame, variable = e)
    empsEPM.append(e)
    empEPM.grid(row = i + 1, column = 5)
    
    b = IntVar(value = 0)
    empBackup = Checkbutton(empsFrame, variable = b)
    empsBackup.append(b)
    empBackup.grid(row = i + 1, column = 6)
    
    empSpec = StringVar()
    empSpecial = OptionMenu(empsFrame, empSpec, *specialList)
    empsSpecial.append(empSpec)
    empSpecial.grid(row = i+1, column = 7, sticky = 'ew')
    
    scrollableFrame.grid(row = 1, column = 0, sticky = 'nsew')


#################################
##--------LABEL SETUP----------##
#################################

Label(root, text = "Break Scheduler", font = ("Arial", 20)).grid(row = 0, column = 0, sticky = 'w')
Label(root, text = "Date: ", font = ("Arial", 20)).grid(row = 0, column = 1, sticky = 'w')

#################################
##--------EMPLOYEE SETUP-------##
#################################

#Employee arrays used to populate employee objects after being entered
empsNames = []
empsDepts = []
empsStart = []
empsEnd = []
empsSPM = []
empsEPM = []
empsBackup = []
empsSpecial = []

#Frame for all input fields
scrollableFrame = ScrolledFrame(root, horizflex = 'expand')
empsFrame = scrollableFrame.interior()


#Lists to be used with dropdown menus
departmentsList = ["Cashier",
               "Soft Production",
               "Soft Stocking",
               "Hard Production",
               "Hard Stocking",
               "ACC",
               "Shoes",
               "New Goods",
               "Books/Jewlery",
               "Warehouse",
               "Other"]

specialList = ["None",
               "Pricer",
               "Clean",
               "Fitting Room"]

#Grid configuration
Grid.columnconfigure(empsFrame, index = 0, weight = 9)
Grid.columnconfigure(empsFrame, index = 1, weight = 12)
Grid.columnconfigure(empsFrame, index = 2, weight = 2)
Grid.columnconfigure(empsFrame, index = 4, weight = 2)
Grid.columnconfigure(empsFrame, index = 7, weight = 5)


for i in range(numEmps):
    #Populating input area with input fields
    addEmp()
    numEmps -= 1
    
#Labels for input fields
Label(empsFrame, text = "Name").grid(row = 0, column = 0, sticky = 'w')
Label(empsFrame, text = "Department").grid(row = 0, column = 1, sticky = 'w')
Label(empsFrame, text = "Start").grid(row = 0, column = 2, sticky = 'w')
Label(empsFrame, text = "PM?").grid(row = 0, column = 3, sticky = 'w')
Label(empsFrame, text = "End").grid(row = 0, column = 4, sticky = 'w')
Label(empsFrame, text = "PM?").grid(row = 0, column = 5, sticky = 'w')
Label(empsFrame, text = "Backup?").grid(row = 0, column = 6, sticky = 'w')
Label(empsFrame, text = "Special Attribute").grid(row = 0, column = 7, sticky = 'w')
  
#binding mousewheel to employee input frame
def _on_mousewheel(event):
    scrollableFrame.yview(mode = 'scroll', value = int(-1*event.delta/120))  

scrollableFrame.bind_all("<MouseWheel>", _on_mousewheel)

#Griding frame to screen
scrollableFrame.grid(row = 1, column = 0, sticky = 'nsew')


#################################
##--------SCHEDULE SETUP-------##
#################################
scheduleFrame = Frame(root)

Grid.columnconfigure(scheduleFrame, 0, weight = 6)
Grid.columnconfigure(scheduleFrame, 1, weight = 2)
Grid.columnconfigure(scheduleFrame, 2, weight = 2)
Grid.columnconfigure(scheduleFrame, 3, weight = 2)
Grid.columnconfigure(scheduleFrame, 4, weight = 2)
Grid.columnconfigure(scheduleFrame, 6, weight = 6)
Grid.columnconfigure(scheduleFrame, 7, weight = 2)
Grid.columnconfigure(scheduleFrame, 8, weight = 2)
Grid.columnconfigure(scheduleFrame, 9, weight = 2)
Grid.columnconfigure(scheduleFrame, 10, weight = 2)

for col in range(5):
    for row in range(33):
        Grid.rowconfigure(scheduleFrame, index = row, weight = 1)
        if col == 0 or col == 5:
            Label(scheduleFrame, borderwidth = 1, relief = 'solid').grid(row = row, column = col, sticky = 'nsew')
            Label(scheduleFrame, borderwidth = 1, relief = 'solid').grid(row = row, column = col + 6, sticky = 'nsew')
        else:
            Label(scheduleFrame, borderwidth = 1, relief = 'solid').grid(row = row, column = col, sticky = 'nsew')
            Label(scheduleFrame, borderwidth = 1, relief = 'solid').grid(row = row, column = col + 6, sticky = 'nsew')
        

##class labels
Label(scheduleFrame, text = "Managers",  borderwidth = 1, relief = 'solid').grid(row = 0, column = 0, sticky = 'nsew')
Label(scheduleFrame, text = "Cashiers",  borderwidth = 1, relief = 'solid').grid(row = 7, column = 0, sticky = 'nsew')
Label(scheduleFrame, text = "ACC", borderwidth = 1, relief = 'solid').grid(row = 16, column = 0, sticky = 'nsew')
Label(scheduleFrame, text = "Shoes", borderwidth = 1, relief = 'solid').grid(row = 22, column = 0, sticky = 'nsew')
Label(scheduleFrame, text = "New Goods", borderwidth = 1, relief = 'solid').grid(row = 24, column = 0, sticky = 'nsew')
Label(scheduleFrame, text = "Books/Jewlery", borderwidth = 1, relief = 'solid').grid(row = 26, column = 0, sticky = 'nsew')
Label(scheduleFrame, text = "Soft Production", borderwidth = 1, relief = 'solid').grid(row = 0, column = 6, sticky = 'nsew')
Label(scheduleFrame, text = "Wares Production", borderwidth = 1, relief = 'solid').grid(row = 6, column = 6, sticky = 'nsew')
Label(scheduleFrame, text = "Apparel Stockers", borderwidth = 1, relief = 'solid').grid(row = 11, column = 6, sticky = 'nsew')
Label(scheduleFrame, text = "Wares Stockers", borderwidth = 1, relief = 'solid').grid(row = 18, column = 6, sticky = 'nsew')
Label(scheduleFrame, text = "Other", borderwidth = 1, relief = 'solid').grid(row = 27, column = 6, sticky = 'nsew')
Label(scheduleFrame, text = "Warehouse", borderwidth = 1, relief = 'solid').grid(row = 31, column = 6, sticky = 'nsew')

scheduleFrame.grid(row = 1, column = 1, sticky = 'nsew', padx = 10)

#################################
##--------OPTIONS SETUP--------##
#################################

optionsFrame = ttk.Frame(root)
    
Grid.columnconfigure(optionsFrame, 0, weight = 2)
Grid.columnconfigure(optionsFrame, 1, weight = 2)
Grid.columnconfigure(optionsFrame, 2, weight = 10)
Grid.columnconfigure(optionsFrame, 3, weight = 2)


Button(optionsFrame, text = "Schedule", command = lambda: initEmps(empsNames, empsDepts, empsStart, empsSPM, empsEnd, empsEPM, breakObjs, empObjs)).grid(column = 1, row = 1)
Button(optionsFrame, text = "Add Employee", command = addEmp).grid(column = 0, row = 1)
Button(optionsFrame, text = "Add Date").grid(column = 3, row = 1)

optionsFrame.grid(row = 2, column = 0, columnspan = 2, sticky='nsew', pady = 5)

def initEmps(names, depts, start, sPM, end, ePM, breakObjs, empObjs):
    for i in range(numEmps):
        if (len(names[i].get()) == 0 or len(start[i].get()) == 0 or len(end[i].get()) == 0 or len(depts[i].get()) == 0):
            print("Something is empty.")
        else:
            print(str(names[i].get()) + " being handled")
            ##converting Time
            startConverted = toHP(int(start[i].get()), int(sPM[i].get()))
            endConverted = toHP(int(end[i].get()), int(ePM[i].get()))
            
            empObj = Employees(str(names[i].get()), startConverted, endConverted, str(depts[i].get()))
            print("empObj for " +str(names[i].get()) + " created")
            print(str(names[i].get()) + " dept = " + str(empObj.getDepartment()))
            empObjs.append(empObj)

    insertionSort(empObjs)
    
    for i in range(len(empObjs)):
        ##Adding to Department's Object array
        empDept = empObjs[i].getDepartment()
        deptClass = departments.get(empDept)
        deptClass.emps.append(empObjs[i])

    breakObjs=[cBreaks, spBreaks, ssBreaks, hpBreaks, hsBreaks, accBreaks,
               shBreaks, ngBreaks, bjBreaks, wBreaks, oBreaks, test]
    
    for dept in range(len(breakObjs)):
        for emp in range(len(breakObjs[dept].emps)):
            empObj = breakObjs[dept].emps[emp]
            breakObjs[dept].assignBreaks(empObj)
            Label(scheduleFrame, text = empObj.getName(), borderwidth = 1, relief = 'solid').grid(row = emp + breakObjs[dept].dispRow + 1, column = breakObjs[dept].dispCol, sticky = 'nsew')
            Label(scheduleFrame, text = str(toHM(empObj.getStartTime())) + "-"+ str(toHM(empObj.getEndTime())), borderwidth = 1, relief = 'solid').grid(row = emp + breakObjs[dept].dispRow + 1, column = breakObjs[dept].dispCol + 1, sticky = 'nsew')
            Label(scheduleFrame, text = empObj.getRestBreak1(), borderwidth = 1, relief = 'solid').grid(row = emp + breakObjs[dept].dispRow + 1, column = breakObjs[dept].dispCol + 2, sticky = 'nsew')
            Label(scheduleFrame, text = empObj.getMealBreak(), borderwidth = 1, relief = 'solid').grid(row = emp + breakObjs[dept].dispRow + 1, column = breakObjs[dept].dispCol + 3, sticky = 'nsew')
            Label(scheduleFrame, text = empObj.getRestBreak2(), borderwidth = 1, relief = 'solid').grid(row = emp + breakObjs[dept].dispRow + 1, column = breakObjs[dept].dispCol + 4, sticky = 'nsew')

    for i in range(len(breakObjs)):
        breakObjs[i].emps.clear()
        breakObjs[i].resetBreaks()
        
    empObjs.clear()

    scheduleFrame.grid(row = 1, column = 1, sticky = 'nsew', padx = 10)
    
                   
#################################
##---------CREDIT SETUP--------##
#################################
    
Label(root, text = "Built by Mikayla Billings-Alston, https://github.com/mcbillings/", font = ("Arial", 11)).grid(row = 3, column = 1, sticky = 'se')               

root.mainloop()