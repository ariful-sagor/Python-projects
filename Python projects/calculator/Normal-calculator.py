# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:47:27 2020

@author: Asus
"""


from tkinter import *
import tkinter.messagebox 

root= Tk()
root.title("A Simple calculator")
root.resizable(width=False,height= False)

e= Entry(root,width=40,borderwidth=10)
e.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

def button_click(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    
def button_clear():
    e.delete(0,END)
    
def button_add():
    first_number= e.get()
    global f_num
    global math
    math= "addition"
    f_num= int(first_number)
    
    e.delete(0,END)
    
def button_equal():
    second_number= e.get()
    e.delete(0,END)
    if math== "addition":
        e.insert(0, f_num + int(second_number))
        
    if math== "subtraction":
        e.insert(0, f_num - int(second_number))
        
        
    if math== "multiplication":
        e.insert(0, f_num * int(second_number))
        
    if math== "division":
        e.insert(0, f_num / int(second_number))
    
def button_mul():
    first_number= e.get()
    global f_num
    global math
    math= "multiplication"
    f_num= int(first_number)
    
    e.delete(0,END)


def button_div():
    first_number= e.get()
    global f_num
    global math
    math= "division"
    f_num= int(first_number)
    
    e.delete(0,END)



def button_min():
    first_number= e.get()
    global f_num
    global math
    math= "subtraction"
    f_num= int(first_number)
    
    e.delete(0,END)
    

# Define buttons
    
button1= Button(root,text="1",padx=40,pady=20,command= lambda: button_click(1))
button2= Button(root,text="2",padx=40,pady=20,command= lambda: button_click(2))
button3= Button(root,text="3",padx=40,pady=20,command= lambda: button_click(3))
button4= Button(root,text="4",padx=40,pady=20,command= lambda: button_click(4))
button5= Button(root,text="5",padx=40,pady=20,command= lambda: button_click(5))
button6= Button(root,text="6",padx=40,pady=20,command= lambda: button_click(6))
button7= Button(root,text="7",padx=40,pady=20,command= lambda: button_click(7))
button8= Button(root,text="8",padx=40,pady=20,command= lambda: button_click(8))
button9= Button(root,text="9",padx=40,pady=20,command= lambda: button_click(9))
button0= Button(root,text="0",padx=40,pady=20,command= lambda: button_click(0))

button_equal= Button(root,text="=",padx=40,pady=20,command= button_equal)
button_clear= Button(root,text="C",padx=40,pady=20,command= button_clear)

button_add= Button(root, text="+",padx=40,pady=20,command= button_add)
button_min= Button(root,text="-",padx=40,pady=20,command= button_min)
button_mul= Button(root,text="*",padx=40,pady=20,command= button_mul)
button_div= Button(root,text="/",padx=40,pady=20,command= button_div)
# Display buttons


button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_clear.grid(row=1,column=4)
button_add.grid(row=1,column=5)


button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_min.grid(row=2,column=5)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button_mul.grid(row=3,column=5)

button_clear.grid(row=4,column=0)
button_equal.grid(row=4,column=2)
button0.grid(row=4,column=1)
button_div.grid(row=4,column=5)



root.mainloop()
