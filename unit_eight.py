# James Bankole 11/4/16 unit 8.
# This program generates an awesome functional calculator.

import tkinter

root = tkinter.Tk()

root.title("My Awesome Calculator!")


def displayNine():
    """These functions display the numbers that the user selects and evaluates/displays the answer to the equation
    they input."""
    pie = textbox.get()
    pie += "9"
    textbox.set(pie)


def displayEight():
    pie = textbox.get()
    pie += "8"
    textbox.set(pie)


def displaySeven():
    pie = textbox.get()
    pie += "7"
    textbox.set(pie)


def displaySix():
    pie = textbox.get()
    pie += "6"
    textbox.set(pie)


def displayFive():
    pie = textbox.get()
    pie += "5"
    textbox.set(pie)


def displayFour():
    pie = textbox.get()
    pie += "4"
    textbox.set(pie)


def displayThree():
    pie = textbox.get()
    pie += "3"
    textbox.set(pie)


def displayTwo():
    pie = textbox.get()
    pie += "2"
    textbox.set(pie)


def displayOne():
    pie = textbox.get()
    pie += "1"
    textbox.set(pie)


def displayZero():
    pie = textbox.get()
    pie += "0"
    textbox.set(pie)


def displaySquared():
    pie = float(textbox.get())
    piee = pie * pie
    textbox.set(piee)


def displayPlus():
    pie = textbox.get()
    pie += "+"
    textbox.set(pie)


def displayMinus():
    pie = textbox.get()
    pie += "-"
    textbox.set(pie)


def displayDivision():
    pie = textbox.get()
    pie += "/"
    textbox.set(pie)


def displayMultiply():
    pie = textbox.get()
    pie += "*"
    textbox.set(pie)


def displayDecimal():
    pie = textbox.get()
    pie += "."
    textbox.set(pie)


def displayClear():
    pie = textbox.get()
    pie = ""
    textbox.set(pie)


def getAnswer():
    pie = textbox.get()
    piee = eval(pie)
    textbox.set(piee)


textbox = tkinter.StringVar()
textbox.set("")

calcBox = tkinter.Entry(root, textvariable = textbox)
calcBox.grid(row= 1, column = 1, columnspan = 3)

numberNine = tkinter.Button(root, text= "  9  ", command= displayNine)
numberNine.grid(row=2, column=3)

numberEight = tkinter.Button(root, text="  8  ", command= displayEight)
numberEight.grid(row=2, column=2)

numberSeven = tkinter.Button(root, text="  7  ", command= displaySeven)
numberSeven.grid(row=2, column=1)

numberSix = tkinter.Button(root, text="  6  ", command= displaySix)
numberSix.grid(row=3, column=3)

numberFive = tkinter.Button(root, text="  5  ", command=displayFive)
numberFive.grid(row=3, column=2)

numberFour = tkinter.Button(root, text="  4  ", command=displayFour)
numberFour.grid(row=3, column=1)

numberThree = tkinter.Button(root, text="  3  ", command=displayThree)
numberThree.grid(row=4, column=3)

numberTwo = tkinter.Button(root, text="  2  ", command=displayTwo)
numberTwo.grid(row=4, column=2)

numberOne = tkinter.Button(root, text="  1  ", command= displayOne)
numberOne.grid(row=4, column=1)

numberZero = tkinter.Button(root, text="  0  ", command= displayZero)
numberZero.grid(row=5, column=1)

numberPlus = tkinter.Button(root, text="  +  ", command= displayPlus)
numberPlus.grid(row=2, column=4)

numberMinus = tkinter.Button(root, text="  -  ", command= displayMinus)
numberMinus.grid(row=3, column=4)

numberDivision = tkinter.Button(root, text="  /  ", command= displayDivision)
numberDivision.grid(row=4, column=4)

numberMultiply = tkinter.Button(root, text="  *  ", command= displayMultiply)
numberMultiply.grid(row=5, column=4)

numberDecimal = tkinter.Button(root, text= "  .  ", command= displayDecimal)
numberDecimal.grid(row=5, column=2)

numberSquared = tkinter.Button(root, text=" x^2 ", command= displaySquared)
numberSquared.grid(row=5, column=3)

numberEqual = tkinter.Button(root, text= "Enter", command= getAnswer)
numberEqual.grid(row=6, column=3)

numberClear = tkinter.Button(root, text="Clear", command= displayClear)
numberClear.grid(row=1, column=4)

root.mainloop()
