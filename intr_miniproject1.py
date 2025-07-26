#mini project 1
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random as r
import string

win=tk.Tk()
win.geometry("300x300")

notebook=ttk.Notebook(win)
notebook.pack()

#TAB 1 - CALCULATOR
frame1=ttk.Frame(notebook)
notebook.add(frame1,text="Tab 1")
def button_click(number):
    current = e1.get()
    e1.delete(0, tk.END)
    e1.insert(0, str(current) + str(number))
    
def backspace():
    e1.delete(len(e1.get())-1,tk.END)

def delete():
    e1.delete(0,tk.END)

def cal():
    result = eval(e1.get())
    e1.delete(0, tk.END)
    e1.insert(0, result)
  
e1=tk.Entry(frame1,width=25,borderwidth=4)
b1=tk.Button(frame1,text="1",padx=10,pady=10,command=lambda: button_click(1))
b2=tk.Button(frame1,text="2",padx=10,pady=10,command=lambda: button_click(2))
b3=tk.Button(frame1,text="3",padx=10,pady=10,command=lambda: button_click(3))
b4=tk.Button(frame1,text="4",padx=10,pady=10,command=lambda: button_click(4))
b5=tk.Button(frame1,text="5",padx=10,pady=10,command=lambda: button_click(5))
b6=tk.Button(frame1,text="6",padx=10,pady=10,command=lambda: button_click(6))
b7=tk.Button(frame1,text="7",padx=10,pady=10,command=lambda: button_click(7))
b8=tk.Button(frame1,text="8",padx=10,pady=10,command=lambda: button_click(8))
b9=tk.Button(frame1,text="9",padx=10,pady=10,command=lambda: button_click(9))
b10=tk.Button(frame1,text="0",padx=10,pady=10,command=lambda: button_click(0))
b11=tk.Button(frame1,text="+",padx=10,pady=10,command=lambda: button_click("+"))
b12=tk.Button(frame1,text="-",padx=10,pady=10,command=lambda: button_click("-"))
b13=tk.Button(frame1,text="x",padx=10,pady=10,command=lambda: button_click("*"))
b14=tk.Button(frame1,text="/",padx=10,pady=10,command=lambda: button_click("/"))
b15=tk.Button(frame1,text="backspace",padx=6,pady=10,command=backspace)
b16=tk.Button(frame1,text="clear",padx=21,pady=10,command=delete)
b17=tk.Button(frame1,text="=",padx=28,pady=10,command=cal)

e1.grid(row=0,column=0,columnspan=4)
b1.grid(row=3,column=0,)
b2.grid(row=3,column=1,)
b3.grid(row=3,column=2,)
b4.grid(row=2,column=0,)
b5.grid(row=2,column=1,)
b6.grid(row=2,column=2,)
b7.grid(row=1,column=0,)
b8.grid(row=1,column=1,)
b9.grid(row=1,column=2,)
b10.grid(row=4,column=2,)
b11.grid(row=1,column=3,)
b12.grid(row=2,column=3,)
b13.grid(row=3,column=3,)
b14.grid(row=4,column=3,)
b15.grid(row=4,column=0,columnspan=2,)
b16.grid(row=5,column=0,columnspan=2,)
b17.grid(row=5,column=2,columnspan=2,)



#TAB 2 - NUMBER GUESSING GAME
frame2=ttk.Frame(notebook)
notebook.add(frame2,text="Tab 2")

def play() :
    global random_number,attempt
    random_number=r.randint(1,100)
    print(random_number)#for checking
    attempt=0
    tries_l.config(text=attempt)
    hint_l.config(text="Hints will appear here.")
    info_l.config(text='')
    guess_e.grid(row=0,column=1,sticky='w',columnspan=2)
    result_l.config(text="")

def guess():
    global attempt
    if guess_e.get()=='' or int(guess_e.get()) not in range(1,101):
        hint_l.config(text="Please enter a vaild number")
    else:
        attempt+=1
        guessed=int(guess_e.get())
        guess_e.delete(0,tk.END)
        if guessed==random_number:
            tries_l.config(text=attempt)
            hint_l.config(text="")
            result_l.config(text= f"Congratulations!! \nYou guessed the number in {attempt} attempt(s)\nThanks for playing :D")
        elif guessed<random_number:
            tries_l.config(text=attempt)
            hint_l.config(text="Try greater number")
        elif guessed>random_number:
            tries_l.config(text=attempt)
            hint_l.config(text="Try smaller number")
def show():
    result_l.config(text=f"Thanks for playing :D\nBTW number was {random_number}")

info_l=tk.Label(frame2,text="Click 'Play' to start the game")
result_l=tk.Label(frame2,)
try_l=tk.Label(frame2,text="Attempts :")
tries_l=tk.Label(frame2,)
hint_l=tk.Label(frame2,)
guess_l=tk.Label(frame2,text="Guess the number :")
guess_e=tk.Entry(frame2,width=15)
guess_b=tk.Button(frame2,text="Guess",command=guess)
play_b=tk.Button(frame2,text="Play",command=play)
show_b=tk.Button(frame2,text="Show",command=show)

guess_l.grid(row=0,column=0,columnspan=1)
info_l.grid(row=0,column=1,sticky='w',columnspan=2)
play_b.grid(row=1,column=0,sticky='e')
guess_b.grid(row=1,column=1)
show_b.grid(row=1,column=2)
try_l.grid(row=2,column=0,sticky='e')
tries_l.grid(row=2,column=1,sticky='w')
hint_l.grid(row=3,column=0,columnspan=3)
result_l.grid(row=4,column=0,columnspan=3)



#TAB 3-PASSWORD GENERATOR
frame3=ttk.Frame(notebook)
notebook.add(frame3,text="Tab 3")

def generate_password():
    length = int(length_e.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(r.choice(characters) for i in range(length))
    generated_password_l.config(text=password)

length_e=tk.Entry(frame3,width=10)
generate_b = tk.Button(frame3, text="Generate Password", command=generate_password)
generated_password_l = tk.Label(frame3, text="")
password_l=tk.Label(frame3,text="Length of password :")

password_l.grid(row=0,column=0,sticky='w')
length_e.grid(row=0,column=1,sticky='w')
generated_password_l.grid(row=1,column=0,columnspan=2)
generate_b.grid(row=2,column=0,columnspan=2)



win.mainloop()