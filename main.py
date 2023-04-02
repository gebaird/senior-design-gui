"""
Created on Thu Mar 30 21:03:58 2023

@author: Grace Baird

Last update: 3/31/2023 8:38 PM

"""

import tkinter
from tkinter import *
from tkinter import ttk
from matplotlib.figure import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


def plot_main():  # creating a basic plot on the first page
    # will update with time-average after figuring that out
    fig = Figure(figsize=(2, 3), dpi=100)
    y = range(10)
    plot1 = fig.add_subplot(111)
    plot1.plot(y)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    main_graph = FigureCanvasTkAgg()

def new_plot(screen, offsetx, offsety):  # creating a basic plot on the first page
    # will update with time-average after figuring that out
    fig = Figure(figsize=(2, 2), dpi=100, facecolor= 'lightgreen')
    y = range(10)
    plot1 = fig.add_subplot(111)
    plot1.plot(y)

    canvas = FigureCanvasTkAgg(fig, master=screen)
    canvas.draw()
    canvas.get_tk_widget().place(relheight = 0.3, relwidth = 0.3, relx = 0.3* offsetx+0.05,
                              rely = 0.3*offsety + 0.03*(offsety+1))

def replot(offsetx, offsety):
    fig = Figure(figsize=(2, 2), dpi=100, facecolor='tomato')
    y = range(10)
    plot1 = fig.add_subplot(111)
    plot1.plot(y)
    canvas = FigureCanvasTkAgg(fig, master=indiv_readouts)
    canvas.draw()
    canvas.get_tk_widget().place(relheight=0.3, relwidth=0.3, relx=0.3 * offsetx + 0.05,
                                 rely=0.3 * offsety + 0.03 * (offsety + 1))

def graphButtons(master):
    addButton = Button(master, text = "Add", heigh = 1, width = 5, state = DISABLED ) #command = lambda: addValue()
    addButton.place(relx = 0.10, rely = 0.33)
    removeButton = Button(master, text = "Remove", height = 1, width = 10, command = lambda: removeValue(removeButton))
    removeButton.place(relx = 0.15, rely = 0.33)


def addValue(addButton, removeButton, xoff, yoff):
    removeButton['state'] = NORMAL
    addButton['state'] = DISABLED
    newreadout1 = new_plot(indiv_readouts, xoff, yoff)

def removeValue(addButton, removeButton, xoff, yoff):
    removeButton['state'] = DISABLED
    addButton['state'] = NORMAL
    newreadout1 = replot(xoff,yoff)


def openIndividualReadouts():
    root.withdraw()
    indiv_readouts.deiconify()


def mainMenu():  # deletes window when button is pushed after time
    indiv_readouts.after(0, indiv_readouts.withdraw())
    root.after(0, root.deiconify)


###############################################################################
root = NONE
indiv_readouts = NONE
root = Tk()  # inidializing the first window
root.title("GAMIX ICP MONITOR")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

# creating actual plot
root_plot = plot_main()
# creating a label just as a rough draft
plot_label = Label(root, text="test plot")
plot_label.pack(anchor="s")

next_button = Button(root, text="Individual ICP Readouts",
                     height = 1, width = 20,
                     command=openIndividualReadouts)
next_button.pack(side ="top")


####################################################################################################################
indiv_readouts = Toplevel(root)
indiv_readouts.withdraw()
indiv_readouts.title("INDIVIDUAL ICP READOUTS")
indiv_readouts.geometry("%dx%d" % (width, height))
mainMenu_button = Button(indiv_readouts, text="Main Menu",
                         heigh=1, width=10,
                         command=lambda: mainMenu())
# if you dont add the lambda it will assign the command value to the return
# from the mainMenu function which will immediately close the window
# the lambda function assigns a callable object which will only execute
# when given an input

mainMenu_button.pack(anchor="c")

readout1 = new_plot(indiv_readouts, 0, 0)
addButton1 = Button(indiv_readouts, text="Add", heigh=1, width=5, state=DISABLED,
                    command = lambda: addValue(addButton1, removeButton1, 0,0))
addButton1.place(relx=0.10, rely=0.33)
removeButton1 = Button(indiv_readouts, text="Remove", height=1, width=10,
                       command = lambda: removeValue(addButton1, removeButton1, 0, 0))
removeButton1.place(relx=0.15, rely=0.33)


readout2 = new_plot(indiv_readouts, 0, 1.5)
addButton2 = Button(indiv_readouts, text="Add", heigh=1, width=5, state=DISABLED,
                   command = lambda: addValue(addButton2, removeButton2, 0, 1.5))
addButton2.place(relx=0.10, rely=0.825)
removeButton2 = Button(indiv_readouts, text="Remove", height=1, width=10,
                       command = lambda: removeValue(addButton2, removeButton2, 0, 1.5))
removeButton2.place(relx=0.15, rely=0.825)


readout3 = new_plot(indiv_readouts, 1, 0)
addButton3 =Button(indiv_readouts, text="Add", heigh=1, width=5, state=DISABLED,
                   command = lambda: addValue(addButton3, removeButton3, 1, 0))
addButton3.place(relx=0.40, rely=0.33)
removeButton3 = Button(indiv_readouts, text="Remove", height=1, width=10,
                       command = lambda: removeValue(addButton3, removeButton3,1, 0))
removeButton3.place(relx=0.45, rely=0.33)


readout4 = new_plot(indiv_readouts, 1, 1.5)
addButton4 = Button(indiv_readouts, text="Add", heigh=1, width=5, state=DISABLED,
                   command = lambda: addValue(addButton4, removeButton4, 1, 1.5))
addButton4.place(relx=0.40, rely=0.825)
removeButton4 = Button(indiv_readouts, text="Remove", height=1, width=10,
                       command = lambda: removeValue(addButton4, removeButton4, 1, 1.5))
removeButton4.place(relx=0.45, rely=0.825)

readout5 = new_plot(indiv_readouts, 2, 0)
addButton5 = Button(indiv_readouts, text="Add", heigh=1, width=5, state=DISABLED,
                   command = lambda: addValue(addButton5, removeButton5, 2, 0))
addButton5.place(relx=0.70, rely=0.33)
removeButton5 = Button(indiv_readouts, text="Remove", height=1, width=10,
                       command = lambda: removeValue(addButton5, removeButton5, 2, 0))
removeButton5.place(relx=0.75, rely=0.33)


readout6 = new_plot(indiv_readouts, 2, 1.5)
addButton6 = Button(indiv_readouts, text="Add", heigh=1, width=5, state=DISABLED,
                   command = lambda: addValue(addButton6, removeButton6, 2, 1.5))
addButton6.place(relx=0.70, rely=0.825)
removeButton6 = Button(indiv_readouts, text="Remove", height=1, width=10,
                       command = lambda: removeValue(addButton6, removeButton6, 2, 1.5))
removeButton6.place(relx=0.75, rely=0.825)
mainloop()
