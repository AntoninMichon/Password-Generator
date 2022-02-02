# Program writen by Michon Antonin
# Python 3.9.7
########== You need tkinter module on your computer ==#######

#== On linux : 
# sudo apt install python3-tk

## Use pip on windows and mac [You can already use pip on linux, but package install is more easy]

from random import randint, choice
from tkinter import *


# Program :

def gen():
    """[Genere a random password]

    Args:
        sym ([String]): [All charactere who can be in password]

    Returns:
        [String]: [Password]
    """
    low_letter = "abcdefghijklmnop"
    high_letter = "ABCDEFGHIJKLMNOP"
    spec_chara = "%:/&()[]{}#$:"
    all = low_letter + high_letter + spec_chara
    
    password =  "".join(choice(all) for a in range(12))
    passw.delete(0, END)
    passw.insert(0, password)



# Tkinter :

win = Tk()  
win.title("Password Generator")
win.geometry("1280x720")    # For screen in 4/3 or resolution less than 720p, change this variable
win.config(background='#CF0063')

box = Frame(win, bg='#CF0063')

title = Label(box, text="Password Generator\nV1.0", font=("Arial", 30), bg='#CF0063', fg='#FFFFFF')
title.grid(row=0, column=0)


passw = Entry(box, text="Password Generator\nV1.0", font=("Arial", 30), bg='#CF0063', fg='#FFFFFF')
passw.grid(row=1, column=0)

arrow = Label(box, text="↑", font=("Arial", 50), bg='#CF0063', fg='#000000')
arrow.grid(row=2, column=0)

gen_passw = Button(box, text="Click here to genere a new password", font=("Arial", 30), bg='#FFFFFF', fg='#000000', command=gen)
gen_passw.grid(row=3, column=0)

credit = Label(box, text="Program writen by Michon Antonin, on Python 3.9.7", font=("Arial", 15), bg='#CF0063', fg='#FFFFFF')
credit.grid(row=4, column=0)

alt = Menu(win)
men = Menu(alt, tearoff=0)
men.add_command(label="New", command=gen)
men.add_command(label="Leave", command=win.quit)
alt.add_cascade(label="File", menu=men)

win.config(menu=alt)

box.pack(expand=YES)
win.mainloop()



## Ty for use my program ;

## Contact :
# Mail : antonin.michon@laposte.net
# Twitter : @anto_mch