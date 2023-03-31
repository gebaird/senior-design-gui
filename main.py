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




def plot ():
    fig = Figure(figsize = (5, 5), dpi = 100)
    y = range(10)
    plot1 = fig.add_subplot(111)
    plot1.plot(y)
    
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    main_graph = FigureCanvasTkAgg()

root = Tk(className = "GAMIX ICP MONITOR",)
root.geometry("500x500")
plot_label = Label(height = 2, width = 10, text = "test plot", 
                   background = 'magenta', pady = 1, padx = 10).pack()
root_plot = plot()

root.mainloop()

