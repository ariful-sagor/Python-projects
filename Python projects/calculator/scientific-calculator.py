# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:12:23 2020

@author: Asus
"""

from tkinter import *
import math

root= Tk()
root.title("Scientific Calculator")
root.iconbitmap("C:/Users/Asus/Pictures/cal1.ico")

mytitle= Label(root,text="Personal Calculator",font="bold")
mytitle.grid(row=0,column=4,columnspan=3)


e= Entry(root,width=60,borderwidth=10)
e.grid(row=0,column=0,columnspan=4,pady=15)
root.resizable(width=False,height=False)
root.configure(bg="grey")



'''
def click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number)) 
    
'''

def click(number):
    current=e.get()
    
    current_2 = str(number)
    if number:
        e.delete(0,END)
        e.insert(0,str(current)+str(number))
        
    elif current_2== "0":
        e.delete(0,END)
        e.insert(0,str(current)+str(number))
        
        
    else:
        if current_2 == '.':
            if current_2 in current:
                return
        current_2 = current + current_2
        return current_2


def equal():
    second_number= e.get()
    e.delete(0,END)
    if mat== "add":
        e.insert(0, first_num + float(second_number))
        
    if mat== "sub":
        e.insert(0,  first_num - float(second_number))
        
        
    if mat== "mul":
        e.insert(0, first_num  * float(second_number))
        
    if mat== "div":
        e.insert(0, first_num  / float(second_number))
        
    if mat== "expo":
        e.insert(0, math.exp(first_num))
        
    if mat== "tan":
        e.insert(0, math.tan(first_num))
        
    if mat== "cos":
        e.insert(0, math.cos(first_num))
        
    if mat== "sin":
        e.insert(0, math.sin(first_num))
        
    if mat== "log":
        e.insert(0, math.log(first_num,10))
        
    if mat== "ln":
        e.insert(0, math.log(first_num))
        
    if mat== "fact":
        e.insert(0, math.factorial(first_num))
        
    if mat== "sqrt":
        e.insert(0, first_num ** (1/2))
        
    if mat== "sqrt1":
        e.insert(0, first_num ** (1/ float(second_number)))
        
    if mat== "power":
        e.insert(0, first_num ** float(second_number))
        
    if mat== "power10":
        e.insert(0, first_num * (10 ** float(second_number)))
        
    if mat== "square":
        e.insert(0, first_num ** 2)
        
    if mat== "asin":
        e.insert(0, math.asin(first_num))
        
    if mat== "acos":
        e.insert(0, math.acos(first_num))
        
    if mat== "atan":
        e.insert(0, math.atan(first_num))
        
    if mat== "inv":
        e.insert(0, 1/(first_num))
        

def add():
    global first_num
    first_num= float(e.get())
    global mat
    mat= "add"
    
    e.delete(0,END)


def sub():
    global first_num
    first_num= float(e.get())
    global mat
    mat= "sub"
    
    e.delete(0,END)


def mul():
    global first_num
    first_num= float(e.get())
    global mat
    mat= "mul"
    
    e.delete(0,END)


def div():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "div"
    
    e.delete(0,END)


def ac():
    e.delete(0,END)
    

def sin():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "sin"
    e.delete(0,END)

def cos():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "cos"
    e.delete(0,END)

def tan():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "tan"
    e.delete(0,END)

def sin1():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "asin"
    e.delete(0,END)

def cos1():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "acos"
    e.delete(0,END)

def tan1():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "atan"
    e.delete(0,END)

def ln():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "ln"
    e.delete(0,END)

def log():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "log"
    e.delete(0,END)

def expo():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "expo"
    e.delete(0,END)

def sqrt():
    global first_num
    first_num= float(e.get())
    global mat
    mat= "sqrt"
    e.delete(0,END)

def square():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "square"
    e.delete(0,END)
    
def power():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "power"
    e.delete(0,END)
        
def fact():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "fact"
    e.delete(0,END)
    
def inv():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "inv"
    e.delete(0,END) 
        
def sqrt1():
    global first_num
    first_num= float(e.get())
    global mat
    mat= "sqrt1"
    e.delete(0,END)
        
def plus_minus():
    current = -(float(e.get())) 
    e.delete(0, END)
    e.insert(0, current)
    
def but10x():
    global first_num
    global mat
    first_num= float(e.get())
    mat= "power10"
    e.delete(0,END)
       
    

# Define button 1-0
button1= Button(root,text="1",padx=45,pady=20,bg="light green",command= lambda: click(1))
button2= Button(root,text="2",padx=47,pady=20,bg="light green",command= lambda: click(2))
button3= Button(root,text="3",padx=45,pady=20,bg="light green",command= lambda: click(3))
button4= Button(root,text="4",padx=45,pady=20,bg="light green",command= lambda: click(4))
button5= Button(root,text="5",padx=47,pady=20,bg="light green",command= lambda: click(5))
button6= Button(root,text="6",padx=45,pady=20,bg="light green",command= lambda: click(6))
button7= Button(root,text="7",padx=45,pady=20,bg="light green",command= lambda: click(7))
button8= Button(root,text="8",padx=47,pady=20,bg="light green",command= lambda: click(8))
button9= Button(root,text="9",padx=45,pady=20,bg="light green",command= lambda: click(9))
button0= Button(root,text="0",padx=47,pady=20,bg="light green",command= lambda: click(0))

# Define button +,-,*,/
button_add= Button(root,text="+",bg="light blue",padx=47,pady=20,command= add)
button_sub= Button(root,text="_",bg="light blue",padx=48,pady=20,command= sub)
button_mul= Button(root,text="×",bg="light blue",padx=47,pady=20,command= mul)
button_div= Button(root,text="÷",bg="light blue",padx=47,pady=20,command= div)


#define button of trigonometric function
button_sin= Button(root,text="sin",bg="light yellow",padx=40,pady=20,command= sin)
button_cos= Button(root,text="cos",bg="light yellow",padx=40,pady=20,command= cos)
button_tan= Button(root,text="tan",bg="light yellow",padx=40,pady=20,command= tan)

button_sin1= Button(root,text="sin^-1",bg="light yellow",padx=30,pady=20,command= sin1)
button_cos1= Button(root,text="cos^-1",bg="light yellow",padx=30,pady=20,command= cos1)
button_tan1= Button(root,text="tan^-1",bg="light yellow",padx=30,pady=20,command= tan1)


#define log functions

button_log= Button(root,text="log",bg="light yellow",padx=40,pady=20,command=log)
button_ln= Button(root,text="ln",bg="light yellow",padx=45,pady=20,command= ln)
button_e= Button(root,text="e",bg="light yellow",padx=44,pady=20,command= expo)


#define math functions

button_sqrt= Button(root,text="√",bg="light yellow",padx=45,pady=20,command= sqrt)
button_pi= Button(root,text="π",bg="light yellow",padx=43,pady=20,command= lambda: click(3.141592653589))
button_x2= Button(root,text="x²",bg="light yellow",padx=45,pady=20,command= square) 
button_xn= Button(root,text="x^n",bg="light yellow",padx=38,pady=20,command= power)

button_dot= Button(root,text=".",bg="light yellow",padx=48,pady=20,command=lambda: click("."))
button_fact= Button(root,text="!",bg="light yellow",padx=45,pady=20,command= fact)
button_plus_minus= Button(root,text="+/-",bg="light yellow",padx=40,pady=20,command= plus_minus)
button10x= Button(root,text="× 10^x",bg="light yellow",padx=33,pady=20,command= but10x)



# Define extra buttons

button_ac= Button(root,text="AC",bg="white",padx=43,pady=20,command= ac)
button_equal= Button(root,text="=",bg="silver",padx=104,pady=20,command= equal)

button_inv= Button(root,text="1/x",bg="light yellow",padx=38,pady=20,command= inv)
button_sqrt1= Button(root,text="n^√",bg="light yellow",padx=38,pady=20,command= sqrt1)





# Place all button in calculator

button1.grid(row=5,column=2,padx=3,pady=2)
button2.grid(row=5,column=3,padx=3,pady=2)
button3.grid(row=5,column=4,padx=3,pady=2)
button4.grid(row=4,column=2,padx=3,pady=2)
button5.grid(row=4,column=3,padx=3,pady=2)
button6.grid(row=4,column=4,padx=3,pady=2)
button7.grid(row=3,column=2,padx=3,pady=2)
button8.grid(row=3,column=3,padx=3,pady=2)
button9.grid(row=3,column=4,padx=3,pady=2)
button0.grid(row=6,column=2)

button_add.grid(row=3,column=5,padx=3,pady=2)
button_sub.grid(row=4,column=5,padx=3,pady=2)
button_mul.grid(row=5,column=5,padx=3,pady=2)
button_div.grid(row=6,column=5,padx=3,pady=2)

button_sin.grid(row=1,column=0,padx=3,pady=2)
button_cos.grid(row=1,column=1,padx=3,pady=2)
button_tan.grid(row=1,column=2,padx=3,pady=2)
button_sin1.grid(row=2,column=0,padx=3,pady=2)
button_cos1.grid(row=2,column=1,padx=3,pady=2)
button_tan1.grid(row=2,column=2,padx=3,pady=2)

button_log.grid(row=2,column=4,padx=3,pady=2)
button_ln.grid(row=2,column=3,padx=3,pady=2)
button_e.grid(row=5,column=0,padx=3,pady=2)


button_sqrt.grid(row=3,column=1,padx=3,pady=2)
button_pi.grid(row=3,column=0,padx=3,pady=2)
button_x2.grid(row=1,column=3,padx=3,pady=2)
button_xn.grid(row=1,column=4,padx=3,pady=2)


button_dot.grid(row=6,column=1)
button_fact.grid(row=6,column=0)
button_plus_minus.grid(row=5,column=1,padx=3,pady=2)

button_ac.grid(row=1,column=5)
button_equal.grid(row=6,column=3,columnspan=2)

button_inv.grid(row=4,column=0)
button_sqrt1.grid(row=4,column=1)
button10x.grid(row=2,column=5)


root.mainloop()