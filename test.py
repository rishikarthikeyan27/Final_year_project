import tkinter as tk
from PIL import ImageTk, Image
import random

class Dog:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('1000x650')
        self.puppy = ImageTk.PhotoImage(Image.open('images/puppy.png').resize((80, 50), Image.ANTIALIAS))
        self.puppy_button = tk.Button(self.win, text = "Create Puppies", command = self.create_label)
        self.bin = ImageTk.PhotoImage(Image.open('images/bin.png').resize((80, 50), Image.ANTIALIAS))
        self.bin_label = tk.Label(self.win, text = "bin", image = self.bin)
        self.bin_label.place(height = 50, width = 80, x= 0, y=0)
        self.puppy_button.pack()

    def move(self, e):
        print (e.x , e.y)
        x = self.win.winfo_pointerx() - self.win.winfo_rootx()
        y = self.win.winfo_pointery() - self.win.winfo_rooty()
        e.widget.place(height = 80, width = 50, x=x,y=y,anchor='center')
        print(' X : '+ str(e.x) +' and '+ 'Y : ' + str(e.y))

    def create_label(self):
        self.puppy_label = tk.Label(self.win, image = self.puppy, text = str(random.randint(1,3)))
        self.puppy_label.place(height = 80, width = 50, x= random.randint(300,400), y = random.randint(300, 400))
        self.puppy_label.bind('<B1-Motion>', self.move)
        return
    
    def delete(self, e):
        e.widget.destroy()
        
    
lab = Dog()
lab.win.mainloop()