from tkinter import *
from random import randint

di_no = {
    0: '🎲',
    1: '⚀',
    2: '⚁',
    3: '⚂',
    4: '⚃',
    5: '⚄',
    6: '⚅'
}

App = Tk()
App.title('Dice Roller')
App.geometry('410x220')
App['background'] = 'gray'
App.iconbitmap(r'C:\Users\hp\PycharmProjects\pythonProject\DiceRoll.ico')

dice = Label(App, text=di_no[0], font=('Times', 80), foreground='white', background='gray')
dice.grid(row=0, column=0, columnspan=4, padx=25, pady=5)


no_choice = IntVar()
chk1 = Checkbutton(App, relief='groove', text='1', variable=no_choice, onvalue=1, offvalue=0, background='gray')
chk1.grid(row=1, column=0, padx=35, pady=5)
chk2 = Checkbutton(App, relief='groove', text='2', variable=no_choice, onvalue=2, offvalue=0, background='gray')
chk2.grid(row=1, column=1, padx=35, pady=5)
chk3 = Checkbutton(App, relief='groove', text='3', variable=no_choice, onvalue=3, offvalue=0, background='gray')
chk3.grid(row=1, column=2, padx=35, pady=5)
chk4 = Checkbutton(App, relief='groove', text='4', variable=no_choice, onvalue=4, offvalue=0, background='gray')
chk4.grid(row=1, column=3, padx=35, pady=5)


def roll():
    i1 = randint(1, 6)
    i2 = randint(1, 6)
    i3 = randint(1, 6)
    i4 = randint(1, 6)

    last_try = StringVar()

    msg = Label(App, textvariable=last_try, font=('Times', 80), foreground='white', background='gray')
    msg.grid(row=0, column=0, columnspan=4, padx=0, pady=5)

    if no_choice.get() == 1:
        last_try.set(di_no[i1])
        msg['text'] = last_try
        dice.grid_forget()

    elif no_choice.get() == 2:
        last_try.set(di_no[i1]+di_no[i2])
        msg['text'] = last_try
        dice.grid_forget()

    elif no_choice.get() == 3:
        last_try.set(di_no[i1]+di_no[i2]+di_no[i3])
        msg['text'] = last_try
        dice.grid_forget()

    elif no_choice.get() == 4:
        last_try.set(di_no[i1]+di_no[i2]+di_no[i3]+di_no[i4])
        msg['text'] = last_try
        dice.grid_forget()

    else:
        last_try.set(di_no[0])
        msg['text'] = last_try
        dice.grid_forget()


rollB = Button(App, text=' Roll ', command=roll, background='silver')
rollB.grid(row=3, column=0, columnspan=2, padx=25, pady=5)
clearB = Button(App, text='Clear', command=roll, background='silver')
clearB.grid(row=3, column=2, columnspan=2, padx=25, pady=5)

App.mainloop()
