import tkinter as tk
import tkinter.ttk as ttk
win = tk.Tk()
from PIL import ImageTk, Image
import random

#Create window
win.geometry('1000x650')
win.configure(bg = 'black')

#Functions
def display_crossection_picture(c):
    if(c == "Rectangular"):
        #add Rectangle cross section picture
        img = Image.open('images/r.png').resize((60, 60), Image.ANTIALIAS)
        img = img
        resized_image = ImageTk.PhotoImage(img)
        win.resized_image = resized_image
        print('width : ' + str(resized_image.width()), 'height : ' + str(resized_image.height()))
        img_label = tk.Label(win, width = 60, height = 60)
        img_label.configure(image = resized_image)
        img_label.update()
        print("hello")
        img_label.place(x= 100, y=400)
        # img_canvas.create_image(40, 30, image = resized_image, tag = "R")
    if(c == "I"):
        #add I cross section picture
        img = Image.open('images/i_beam.png').resize((60, 60), Image.ANTIALIAS)
        img = img
        resized_image = ImageTk.PhotoImage(img)
        win.resized_image = resized_image
        img_canvas = tk.Canvas(win, width = resized_image.width(), height = resized_image.height())
        print('width : ' + str(resized_image.width()), 'height : ' + str(resized_image.height()))
        img_canvas.place(x= 100, y=400)  
        img_canvas.create_image(40, 30, image = resized_image, tag = "I")
    if(c == "T"):
        #add T cross section picture
        img = Image.open('images/t.png').resize((60, 60), Image.ANTIALIAS)
        img = img
        resized_image = ImageTk.PhotoImage(img)
        win.resized_image = resized_image
        img_canvas = tk.Canvas(win, width = resized_image.width(), height = resized_image.height())
        print('width : ' + str(resized_image.width()), 'height : ' + str(resized_image.height()))
        img_canvas.place(x= 100, y=400)  
        img_canvas.create_image(40, 30, image = resized_image, tag = "T")
    if(c == "C"):
        #add C cross section picture
        img = Image.open('images/c.png').resize((60, 60), Image.ANTIALIAS)
        img = img
        resized_image = ImageTk.PhotoImage(img)
        win.resized_image = resized_image
        img_canvas = tk.Canvas(win, width = resized_image.width(), height = resized_image.height()+2)
        print('width : ' + str(resized_image.width()), 'height : ' + str(resized_image.height()))
        img_canvas.place(x= 100, y=400)  
        img_canvas.create_image(40, 30, image = resized_image, tag = "C")
    if(c == "O"):
        #add O cross section picture
        img = Image.open('images/o.png').resize((60, 60), Image.ANTIALIAS)
        img = img
        resized_image = ImageTk.PhotoImage(img)
        win.resized_image = resized_image
        img_canvas = tk.Canvas(win, width = resized_image.width(), height = resized_image.height())
        print('width : ' + str(resized_image.width()), 'height : ' + str(resized_image.height()))
        img_canvas.place(x= 100, y=400)  
        img_canvas.create_image(28, 32, image = resized_image, tag = "O")

def master_crossection_function(choice):
    display_crossection_picture(choice) # Displays crossection picture

def create_up_arrow():
    point_force_up_lab = tk.Label(win,image = resized_arrow_up, bg = '#006665')
    point_force_up_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
    return
def create_down_arrow():
    point_force_down_lab = tk.Label(win,image = resized_arrow, bg = '#006665')
    point_force_down_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
    return
def create_moment_ac():
    moment_ac_lab = tk.Label(win,image = resized_moment_a_clock, bg = '#006665')
    moment_ac_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
    return
def create_moment_c():
    moment_c_lab = tk.Label(win,image = resized_moment_clock, bg = '#006665')
    moment_c_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
    return
def create_uniform_load():
    uniform_load_lab = tk.Label(win,image = resized_g_uniform, bg = '#006665')
    uniform_load_lab.place(height = 40, width = 80, x=random.randrange(300,400), y=random.randrange(40,100))
    return
def create_nonuniform_load():
    point_force_down = tk.Label(win,image = resized_g_nonuniform, bg = '#006665')
    point_force_down.place(height = 40, width = 80, x=random.randrange(300,400), y=random.randrange(40,100))
    return


    
#Create Frames
frame1 = tk.Frame(master=win, width=280, height=630, bg='#006665')
frame1.pack(fill=tk.BOTH, padx=10, pady=15,side=tk.LEFT, expand=False)
frame2 = tk.Frame(master=win, width=680, height=315, bg="#006665")
frame2.pack(fill=tk.Y, padx=5, pady=15,side=tk.TOP, expand=False)
frame3 = tk.Frame(master=win, width=680, height=315, bg="#006665")
frame3.pack(fill=tk.Y, padx=5, pady=15,side=tk.BOTTOM, expand=False)


#Arrow down button
arrow = Image.open('images/arrow.png').resize((20, 20), Image.ANTIALIAS)
resized_arrow = ImageTk.PhotoImage(arrow)
win.resized_arrow = resized_arrow
point_force_down = tk.Button(win, text = "Point Force", image = resized_arrow, bg = 'black', command = create_down_arrow)
point_force_down.place(height = 40, width = 80, x=70, y=50)


#Arrow up button
arrow_up = Image.open('images/arrow_up.png').resize((20,20), Image.ANTIALIAS)
resized_arrow_up = ImageTk.PhotoImage(arrow_up)
win.resized_arrow = resized_arrow
point_force_up = tk.Button(win, text = "Point Force", image = resized_arrow_up, bg = 'black',command = create_up_arrow)
point_force_up.place(height = 40, width = 80, x=70, y=90)

#Anticlockwise Moment button
moment_a_clock = Image.open('images/moment_anticlockwise.png').resize((20,20), Image.ANTIALIAS)
resized_moment_a_clock = ImageTk.PhotoImage(moment_a_clock)
win.moment_a_clock = resized_moment_a_clock
Moment_ac = tk.Button(win, image = resized_moment_a_clock, bg = 'black',command = create_moment_ac)
Moment_ac.place(height = 40, width = 80, x=150, y=50)

#Clockwise Moment button
moment_clock = Image.open('images/moment_clockwise.png').resize((20,20), Image.ANTIALIAS)
resized_moment_clock = ImageTk.PhotoImage(moment_clock)
win.resized_moment_clock = resized_moment_clock
Moment_c = tk.Button(win, image = resized_moment_clock, bg = 'black',command = create_moment_c)
Moment_c.place(height = 40, width = 80, x=150, y=90)

#Uniform Distributed Load button
uniform = Image.open('images/uniform.png').resize((80,50), Image.ANTIALIAS)
resized_uniform = ImageTk.PhotoImage(uniform)
win.resized_uniform = resized_uniform
Uniform = tk.Button(win, image = resized_uniform, bg = 'black',command = create_uniform_load)
Uniform.place(height = 40, width = 80, x=70, y=130)

#Nonuniformly Distributed Load button
nonuniform = Image.open('images/nonuniform.png').resize((80,50), Image.ANTIALIAS)
resized_nonuniform = ImageTk.PhotoImage(nonuniform)
win.resized_nonuniform = resized_nonuniform
Non_Uniform = tk.Button(win, image = resized_nonuniform, bg = 'black',command = create_nonuniform_load)
Non_Uniform.place(height = 40, width = 80, x=150, y=130)

#Creating uniform and nonuniformly distributed load
g_uniform = Image.open('images/green_uniform_distributed_load.png').resize((80,50), Image.ANTIALIAS)
resized_g_uniform = ImageTk.PhotoImage(g_uniform)
win.resized_g_uniform = resized_g_uniform

g_nonuniform = Image.open('images/green_nonuniform_distributed_load.png').resize((80,50), Image.ANTIALIAS)
resized_g_nonuniform = ImageTk.PhotoImage(g_nonuniform)
win.resized_g_nonuniform = resized_g_nonuniform

#Simple Support
simple_support = Image.open('images/simple_support.png').resize((60,50), Image.ANTIALIAS)
resized_simple_support = ImageTk.PhotoImage(simple_support)
win.resized_simple_support = resized_simple_support
SimpleSupport = tk.Button(win, image = resized_simple_support, bg = 'black')
SimpleSupport.place(height = 40, width = 80, x=70, y=250)

#Fixed Support
fixed_support = Image.open('images/fixed_support.png').resize((60,50), Image.ANTIALIAS)
resized_fixed_support = ImageTk.PhotoImage(fixed_support)
win.resized_fixed_support = resized_fixed_support
FixedSupport = tk.Button(win, image = resized_fixed_support, bg = 'black')
FixedSupport.place(height = 40, width = 80, x=150, y=250)

#Crossection Drop Down
varList = tk.StringVar(win)
varList.set("Force Type")
force_type = ttk.OptionMenu(win, varList, "Cross section",'Rectangular', 'I', 'T', 'C', 'O', command = master_crossection_function)
force_type.place(height=40, width=120, x= 80, y=340)

#Create the beam picture
beam_img = Image.open('images/beam.png').resize((400, 50), Image.ANTIALIAS)
beam_img = beam_img
resized_beam_image = ImageTk.PhotoImage(beam_img)
win.resized_image = resized_beam_image
beam_lab = tk.Label(win, width = 400, height = 50, image = resized_beam_image, bg = 'black')
beam_lab.place(x=480, y = 200)

#Bin
bin_img = Image.open('images/bin.png').resize((50, 50), Image.ANTIALIAS)
resized_bin_image = ImageTk.PhotoImage(bin_img)
win.resized_bin_image = resized_bin_image
bin_label= tk.Label(win, width = 50, height = 50, image = resized_bin_image, bg = '#006665')
bin_label.place(x=910, y = 30)


win.mainloop()

