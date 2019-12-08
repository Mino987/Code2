from tkinter import *
import datetime
from tkinter import *
from PIL import ImageTk,Image

root=Tk()

canvas=Canvas(root,width=210,height=180)



image=ImageTk.PhotoImage(Image.open("ocean.png"))




canvas.create_image(0,0,anchor=NW,image=image)


canvas.pack()




root.mainloop()

win=Tk()
win.title("Client Name")
win.geometry("500x380")

    
win.configure(background='lightblue')

x = datetime.datetime.now()
l1 = Label(win, text = (x.strftime("%B"),x.strftime("%d")),anchor='nw')
l1.place(x = 0, y = 0)
l1.config(font=("Courier", 30))

x = datetime.datetime.now()
l2 = Label(win, text = (x.strftime("%I"),":",x.strftime("%M")))
l2.place(x = 363, y = 0)
l2.config(font=("Courier", 30))

mb = Menubutton(text="Select")
mb.menu = Menu(mb)
mb ["menu"] = mb.menu


mb.menu.add_command(label="Ocean", command=lambda: print("What did the ocean say to the pirate? Nothing, it just waved..."))

mb.pack()



import tkinter as tk

counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()



 
root = tk.Tk()
root.title("Timer")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()



def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries



from tkinter import *
import tkinter as tk

import tkinter as tk

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = tk.Tk()
tk.Label(master, 
         text="Rate App 1-10").grid(row=0)
tk.Label(master, 
         text="First/Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


tk.Button(master, 
          text='Press Here to play Ocean Noise', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)

tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()




from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("Ocean_Waves-Mike_Koenig-980635527.wav")
play(song)
