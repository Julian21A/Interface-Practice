from tkinter import *
from datetime import datetime

App = Tk()
App.title('Age Calculator')
App.geometry('230x180')
App['background'] = 'silver'
App.iconbitmap(r'C:\Users\hp\PycharmProjects\pythonProject\Age Calculator.ico')

enter = Label(App, text='Enter Your DOB', font=('Times', 12), foreground='white', background='Silver')
enter.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

dayL = Label(App, text='Day:', font=('Times', 12), foreground='white', background='silver')
inpDay = Entry(App, background='gray', foreground='white', width=2,)

monthL = Label(App, text='Month:', font=('Times', 12), foreground='white', background='silver')
inpMonth = Entry(App, background='gray', foreground='white', width=2)

yearL = Label(App, text='Year:', font=('Times', 12), foreground='white', background='silver')
inpYear = Entry(App, background='gray', foreground='white', width=4)


inpDay.grid(row=1, column=1, columnspan=1, padx=0, pady=5)
dayL.grid(row=1, column=0, padx=0, pady=5)
inpMonth.grid(row=1, column=3, columnspan=1, padx=5, pady=5)
monthL.grid(row=1, column=2, padx=0, pady=5)
inpYear.grid(row=1, column=5, columnspan=1, padx=5, pady=5)
yearL.grid(row=1, column=4, padx=0, pady=5)


def find_days():
    day = int(inpDay.get())
    mon = int(inpMonth.get())
    yea = int(inpYear.get())
    dob = datetime(day=day, month=mon, year=yea)

    act_time = datetime.now()
    time_diff = act_time - dob

    dys = Label(App, text=('You lived '+str(time_diff.days)+' days.'), relief='groove',
                background='gray', foreground='white')
    dys.grid(row=3, column=0, columnspan=6, padx=0, pady=5)


def find_secs():
    day = int(inpDay.get())
    mon = int(inpMonth.get())
    yea = int(inpYear.get())
    dob = datetime(day=day, month=mon, year=yea)

    act_time = datetime.now()
    time_diff = act_time - dob

    dys = Label(App, text=('You lived '+str(time_diff.total_seconds())+' seconds.'), relief='groove',
                background='gray', foreground='white')
    dys.grid(row=4, column=0, columnspan=6, padx=0, pady=5)


T_daysB = Button(App, text='Total Days', command=find_days, background='gray', foreground='white')
T_daysB.grid(row=2, column=0, columnspan=3, padx=0, pady=5)

T_secB = Button(App, text='Total Secs', command=find_secs, background='gray', foreground='white')
T_secB.grid(row=2, column=3, columnspan=3, padx=0, pady=5)

App.mainloop()
