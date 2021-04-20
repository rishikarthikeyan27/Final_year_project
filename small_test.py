from beam_details import Beam
from sympy import symbols
from sympy.core import S, Symbol, diff, symbols
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk   
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import random
import calc_file as cf
import math
import time
import matplotlib.pyplot as plt

#Create window
win = tk.Tk()
win.geometry('1000x650')
win.configure(bg = 'black')

frame1 = tk.Frame(master=win, width=280, height=630, bg='#006665')
frame1.pack(fill=tk.BOTH, padx=10, pady=15,side=tk.LEFT, expand=False)
frame2 = tk.Frame(master=win, width=680, height=315, bg="#006665")
frame2.pack(fill=tk.Y, padx=5, pady=15,side=tk.TOP, expand=False)
frame3 = tk.Frame(master=win, width=680, height=315, bg="#006665")
frame3.pack(fill=tk.Y, padx=5, pady=15,side=tk.BOTTOM, expand=False)

entry = 3

#Graph init
graph_canvas = tk.Canvas(frame3, bg = '#006665',highlightthickness=0, highlightbackground="#006665")
graph_canvas.place(width = 440, height = 250, x = 40, y=10)
graph_canvas.create_line(0,125, 400, 125, fill = "black")
graph_canvas.create_line(0,0, 0, 250, fill = "black")

x = 0
y = 0

beam_length = 3.0

def is_negative(x):
    if x<0:
        return True

def graph():
    R1,R2, R3, R4 = symbols('R1, R2, R3, R4') #  
    b = Beam(beam_length, 200*(10**9), 400*(10**-6))
    b.apply_load(10, 0, 0, end = 3)
    # b.apply_load(10, 2.75, -1)

    b.apply_load(R1, 0, -1)
    b.apply_load(R2, 1, -1)
    b.apply_load(R3, 2, -1)
    b.apply_load(R4, 3, -1)
    # b.bc_deflection = [(0, 0), (8, 0)]
    b.bc_deflection = [(0, 0),(1,0), (2,0), (3,0)] #
    b.solve_for_reaction_loads(R1,R2, R3, R4) # 
    shear_force = b.realplot_shear_force()

    
    # plt.plot(shear_force)
    print("Lets what is there here : ", shear_force)
    # give_shear_force_list(shear_force)

mybutton = tk.Button(frame1, text = "Graph It!", command = graph)
mybutton.place(width = 70, height = 20, x = 40, y = 10)



win.mainloop()
