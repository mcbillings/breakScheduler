###This is a program that takes a day's schedule and schedules breaks according to California law

##import files/modules
from employee import *
from breakScheduler import *
from tkinter import *
from tkinter import ttk, simpledialog
import csv
import ctypes

try: # Windows 8.1 and later
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception as e:
    pass
try: # Before Windows 8.1
    ctypes.windll.user32.SetProcessDPIAware()
except: # Windows 8 or before
    pass


##variable/list declairations
##Employee arrays
empObjs = []
breakObjs = []

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

##Break Objs by department
global cBreaks
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

##setting up window
root = Tk()
root.state("iconic")

##getting number of emps
numEmps = simpledialog.askinteger("Enter number of Employees", "Enter number of Employees")
root.state("zoomed")

rows = 0

##setting up employee section of the window
global empsNames
empsNames = []
empsDepts = []
empsStart = []
empsEnd = []
empsSPM = []
empsEPM = []

empsFrame = ttk.Frame(root)
empsCanvas = Canvas(empsFrame)
empsScrollbar = ttk.Scrollbar(empsFrame, orient="vertical", command=empsCanvas.yview)
empsScrollableFrame = ttk.Frame(empsCanvas)


empsScrollableFrame.bind(
    "<Configure>",
    lambda e: empsCanvas.configure(
        scrollregion=empsCanvas.bbox("all")
        )
    )

empsCanvas.create_window((0, 0), window=empsScrollableFrame, anchor="nw")
empsCanvas.configure(yscrollcommand=empsScrollbar.set)

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

sWidth = root.winfo_screenwidth()


for i in range(numEmps):
    empName = Entry(empsScrollableFrame, width = int(sWidth * 1.5/96))
    empsNames.append(empName)
    empName.grid(row = i+1, column = 0)
    
    empDept = StringVar()
    empDepartment = OptionMenu(empsScrollableFrame, empDept, *departmentsList)
    empDepartment.config(width = int(sWidth * 1/96))
    empsDepts.append(empDept)
    empDepartment.grid(row = i+1, column = 1)
    
    empStart = Entry(empsScrollableFrame, width = int(sWidth * 0.5/96))
    empsStart.append(empStart)
    empStart.grid(row = i+1, column = 2)
    
    s = IntVar(value = 0)
    empSPM = Checkbutton(empsScrollableFrame, variable = s)
    empsSPM.append(s)
    empSPM.grid(row = i + 1, column = 3)
    
    empEnd = Entry(empsScrollableFrame, width = int(sWidth * 0.5/96))
    empsEnd.append(empEnd)
    empEnd.grid(row = i+1, column = 4)
    
    e = IntVar(value = 1)
    empEPM = Checkbutton(empsScrollableFrame, variable = e)
    empsEPM.append(e)
    empEPM.grid(row = i + 1, column = 5)
    
    
Label(empsScrollableFrame, text = "Name").grid(row = 0, column = 0)
Label(empsScrollableFrame, text = "Department").grid(row = 0, column = 1)
Label(empsScrollableFrame, text = "Start").grid(row = 0, column = 2)
Label(empsScrollableFrame, text = "PM?").grid(row = 0, column = 3)
Label(empsScrollableFrame, text = "End").grid(row = 0, column = 4)
Label(empsScrollableFrame, text = "PM?").grid(row = 0, column = 5)
  
def _on_mousewheel(event):
    empsCanvas.yview_scroll(int(-1*event.delta/120), "units")  

empsCanvas.bind_all("<MouseWheel>", _on_mousewheel)
  
  
empsFrame.place(relheight = 5/7, relwidth = 3/8)
empsCanvas.pack(side = "left", fill="both", expand=True)
empsScrollbar.pack(side = "right", fill = "y")


nameWidth = 15
timeWidth = 10

##SCHEDULE SET UP
scheduleFrame = Frame(root)
for col in range(5):
    for row in range(33):
        if col == 0 or col == 5:
            Label(scheduleFrame, width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = row, column = col)
            Label(scheduleFrame, width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = row, column = col + 6)
        else:
            Label(scheduleFrame, width = timeWidth, borderwidth = 1, relief = 'solid').grid(row = row, column = col)
            Label(scheduleFrame, width = timeWidth, borderwidth = 1, relief = 'solid').grid(row = row, column = col + 6)
        

##class labels
Label(scheduleFrame, text = "Managers", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 0, column = 0)
Label(scheduleFrame, text = "Cashiers", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 7, column = 0)
Label(scheduleFrame, text = "ACC", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 16, column = 0)
Label(scheduleFrame, text = "Shoes", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 22, column = 0)
Label(scheduleFrame, text = "New Goods", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 24, column = 0)
Label(scheduleFrame, text = "Books/Jewlery", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 26, column = 0)
Label(scheduleFrame, text = "Soft Production", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 0, column = 6)
Label(scheduleFrame, text = "Wares Production", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 6, column = 6)
Label(scheduleFrame, text = "Apparel Stockers", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 11, column = 6)
Label(scheduleFrame, text = "Wares Stockers", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 18, column = 6)
Label(scheduleFrame, text = "Other", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 27, column = 6)
Label(scheduleFrame, text = "Warehouse", width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = 31, column = 6)

scheduleFrame.place(relwidth = 5/8, relx = 7/16, rely = 0.5/16, relheight = 6/7)

##Options Set up
optionsFrame = ttk.Frame(root)


def addEmp():
    i = len(empsNames)
    empName = Entry(empsScrollableFrame, width = int(sWidth * 1.5/96))
    empsNames.append(empName)
    empName.grid(row = i+1, column = 0)
    
    empDept = StringVar()
    empDepartment = OptionMenu(empsScrollableFrame, empDept, *departmentsList)
    empDepartment.config(width = int(sWidth * 1/96))
    empsDepts.append(empDept)
    empDepartment.grid(row = i+1, column = 1)
    
    empStart = Entry(empsScrollableFrame, width = int(sWidth * 0.5/96))
    empsStart.append(empStart)
    empStart.grid(row = i+1, column = 2)
    
    s = IntVar()
    empSPM = Checkbutton(empsScrollableFrame, variable = s)
    empsSPM.append(s)
    empSPM.grid(row = i + 1, column = 3)
    
    empEnd = Entry(empsScrollableFrame, width = int(sWidth * 0.5/96))
    empsEnd.append(empEnd)
    empEnd.grid(row = i+1, column = 4)
    
    e = IntVar()
    empEPM = Checkbutton(empsScrollableFrame, variable = e)
    empsEPM.append(e)
    empEPM.grid(row = i + 1, column = 5)
    
    empsFrame.place(relheight = 5/7, relwidth = 3/8)
    empsCanvas.pack(side = "left", fill="both", expand=True)
    empsScrollbar.pack(side = "right", fill = "y")

Button(optionsFrame, text = "Schedule", command = lambda: initEmps(empsNames, empsDepts, empsStart, empsSPM, empsEnd, empsEPM, breakObjs, empObjs)).place(relx = 1/12, rely = 1/12, relwidth = 1/12, relheight = 1/3)
Button(optionsFrame, text = "Add Employee", command = addEmp).place(relx = 4/12, rely = 1/12, relwidth = 1/12, relheight = 1/3)
Button(optionsFrame, text = "Add Date").place(relx = 9/12, rely = 1/12, relwidth = 1/12, relheight = 1/3)

optionsFrame.place(relwidth = 1, relheight = 1/7, relx = 0, rely = 6/7)

def initEmps(names, depts, start, sPM, end, ePM, breakObjs, empObjs):
    for i in range(numEmps):       
        if (len(names[i].get()) == 0 or len(start[i].get()) == 0 or len(end[i].get()) == 0 or len(depts[i].get()) == 0):
            pass
        else:
            ##converting Time
            startConverted = toHP(int(start[i].get()), int(sPM[i].get()))
            endConverted = toHP(int(end[i].get()), int(ePM[i].get()))
            
            empObj = Employees(str(names[i].get()), startConverted, endConverted, str(depts[i].get()))
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
            Label(scheduleFrame, text = empObj.getName(), width = nameWidth, borderwidth = 1, relief = 'solid').grid(row = emp + breakObjs[dept].dispRow + 1, column = breakObjs[dept].dispCol)
            Label(scheduleFrame, text = str(toHM(empObj.getStartTime())) + "-"+ str(toHM(empObj.getEndTime())), width = 10, borderwidth = 1, relief = 'solid').grid(row = emp + breakObjs[dept].dispRow + 1, column = breakObjs[dept].dispCol + 1)
            Label(scheduleFrame, text = empObj.getRestBreak1(), width = timeWidth, borderwidth = 1, relief = 'solid').grid(row = emp + breakObjs[dept].dispRow + 1, column = breakObjs[dept].dispCol + 2)
            Label(scheduleFrame, text = empObj.getMealBreak(), width = timeWidth, borderwidth = 1, relief = 'solid').grid(row = emp + breakObjs[dept].dispRow + 1, column = breakObjs[dept].dispCol + 3)
            Label(scheduleFrame, text = empObj.getRestBreak2(), width = timeWidth, borderwidth = 1, relief = 'solid').grid(row = emp + breakObjs[dept].dispRow + 1, column = breakObjs[dept].dispCol + 4)

    for i in range(len(breakObjs)):
        breakObjs[i].emps.clear()
        breakObjs[i].breakArr.clear()
    
    for i in range(len(names)):
        print(names[i].get())

    scheduleFrame.place(relwidth = 5/8, relx = 7/16, rely = 0.5/16, relheight = 6/7)
    
                   
                   

root.mainloop()