from tkinter import *
import backend
import os
import sys

root = Tk()
root.geometry('900x600')
root.title('Brightness Control')
program_directory = sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "brightness.png")))

vertical = Scale(root, from_=100, to=0, width=14, length=390)
vertical.pack()
vertical.set(100)
vertical.place(x=200, y=70)

vertical2 = Scale(root, from_=100, to=0, width=15, length=390)
vertical2.set(100)
vertical2.place(x=700, y=70)

night_light = Label(root, text='Night Light:', font="Helvetica 14 bold")
primary = Label(root, text='Primary:', font="Helvetica 14 bold")
secondary = Label(root, text='Secondary:', font="Helvetica 14 bold")
primary.place(x=200, y=35)
secondary.place(x=700, y=35)


def slide():
    # my_label = Label(root, text=str(vertical.get())).pack()
    backend.brightness(str(vertical.get()), display=0)
    backend.brightness(str(vertical2.get()), display=1)
    # brightness_level = vertical.get()


def Simpletoggle():
    if toggle_button.config('text')[-1] == 'ON':
        backend.enable_night_light()
        toggle_button.config(text='OFF')
    else:
        backend.disable_night_light()
        toggle_button.config(text='ON')


toggle_button = Button(text="ON", width=10, height=2, command=Simpletoggle)
toggle_button.place(x=50, y=530)
night_light.place(x=53, y=500)

apply = Button(root, text='Apply', width=22, height=2, command=slide)
apply.place(x=630, y=520)
root.mainloop()
