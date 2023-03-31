# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:03:58 2023

@author: grace
"""

import tkinter
from tkinter import *
from tkinter import ttk
from matplotlib.figure import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

def plot (): #creating a basic plot on the first page
# will update with time-average after figuring that out
    fig = Figure(figsize = (5, 5), dpi = 100)
    y = range(10)
    plot1 = fig.add_subplot(111)
    plot1.plot(y)
    
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    main_graph = FigureCanvasTkAgg()
    
def openNewWindow():
    indiv_readouts = Tk()
    indiv_readouts.title("INDIVIDUAL ICP READOUTS")
    indiv_readouts.geometry("500x500")
    back_button = Button(indiv_readouts, text = "Main Menu", 
                         command = mainMenu(indiv_readouts))
    back_button.pack(anchor = 'c')
    
def mainMenu(currentwindow):
    currentwindow.destroy()
    

    

root = Tk() #inidializing the first window
root.title("GAMIX ICP MONITOR")
root.geometry("500x500") # setting geometry
next_button = Button(root, text = "Individual ICP Readouts", 
                     command = openNewWindow)
next_button.pack(anchor = 's')
                     
#creating a label just as a rough draft
plot_label = Label(root, text = "test plot").pack(anchor = 'n')
#creating actual plot
root_plot = plot()



#creating "Next" button
mainloop()
