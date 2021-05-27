# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:23:29 2021

@author: Ethan Miller

Uses base code in file SimpleCalculator.py supplied by the professor.

Basic structure including the use of tkinter for GUI and code for additional
functions and button behavior was supplied by the SimpleCalculator.py file
given by the professor.

"""


# importing Tkinter and math 
from tkinter import *
import math 

    
# calc class 
class calc: 

    def getandreplace(self): 

        """replace x with * and ÷ with /"""
        self.expression = self.e.get() 
        self.newtext=self.expression.replace('/','/') 
        self.newtext=self.newtext.replace('x','*') 


    def equals(self): 
        """when the equal button is pressed"""
        self.getandreplace() 
        try: 
            # evaluate the expression using the eval function 
            self.value= eval(self.newtext) 
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.e.delete(0,END) 
            self.e.insert(0,self.value) 

    def signchange(self):
        """when the +/- button is pressed, functionally changes sign"""
        self.getandreplace()
        try:
            self.value= eval(self.newtext)
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.signchangeval= self.value * -1
            self.e.delete(0,END) 
            self.e.insert(0,self.signchangeval) 
            
    def hex(self):
        """when the hex button is pressed, converts input to hexadecimal"""
        self.getandreplace()
        try:
            self.value= eval(self.newtext)
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.hexval= hex(self.value)
            self.e.delete(0,END) 
            self.e.insert(0,self.hexval)  
            
    def dec(self):
        """when the dec button is pressed, converts input to decimal"""
        try:
            self.value= eval(self.newtext)
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.decval= int(self.value)
            self.e.delete(0,END) 
            self.e.insert(0,self.decval) 
            
    def oct(self):
        """when the oct button is pressed, converts input to octal"""
        try:
            self.value= eval(self.newtext)
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.octval= oct(self.value)
            self.e.delete(0,END) 
            self.e.insert(0,self.octval)
            
        
    def bin(self):
        """when the bin button is pressed, converts input to binary"""
        try:
            self.value= eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.binval= bin(self.value)
            self.e.delete(0,END) 
            self.e.insert(0,self.binval)
        
    def squareroot(self): 
        """squareroot method"""
        self.getandreplace() 
        try: 
            # evaluate the expression using the eval function 
            self.value= eval(self.newtext) 
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.sqrtval=math.sqrt(self.value) 
            self.e.delete(0,END) 
            self.e.insert(0,self.sqrtval) 

    def square(self): 
        """square method"""
        self.getandreplace() 
        try: 
            #evaluate the expression using the eval function 
            self.value= eval(self.newtext) 
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.sqval=math.pow(self.value,2) 
            self.e.delete(0,END) 
            self.e.insert(0,self.sqval) 

    def clearall(self): 
            """when clear button is pressed,clears the text input area"""
            self.e.delete(0,END) 

    def clear1(self): 
            self.txt=self.e.get()[:-1] 
            self.e.delete(0,END) 
            self.e.insert(0,self.txt) 

    def action(self,argi): 
            """pressed button's value is inserted into the end of the text area"""
            self.e.insert(END,argi)

    def __init__(self,master): 
            """Constructor method"""
            master.title('Programmer Calculator')
            master.geometry() 
            self.e = Entry(master) 
            self.e.grid(row=0,column=0,columnspan=6,pady=5) 
            self.e.focus_set() #Sets focus on the input text area 

            # Generating Buttons 
            Button(master,text="=", width=11,height=3,fg="black", 
                bg="light blue",command=lambda:self.equals()).grid( 
                                    row=5, column=5,columnspan=2) 

            Button(master,text='AC', width=5, height=3, 
                        fg="black", bg="light yellow", 
            command=lambda:self.clearall()).grid(row=2, column=5) 

            Button(master,text='C',width=5,height=3, 
                fg="black",bg="light yellow", 
                command=lambda:self.clear1()).grid(row=2, column=6) 

            Button(master,text="+",width=5,height=3, 
                fg="black",bg="light gray", 
                command=lambda:self.action('+')).grid(row=5, column=3) 

            Button(master,text="x",width=5,height=3, 
                    fg="black",bg="light gray", 
                    command=lambda:self.action('x')).grid(row=3, column=3) 

            Button(master,text="-",width=5,height=3, 
                    fg="black",bg="light gray", 
                    command=lambda:self.action('-')).grid(row=4, column=3) 

            Button(master,text="÷",width=5,height=3, 
                fg="black",bg="light gray", 
                command=lambda:self.action('/')).grid(row=2, column=3) 

            Button(master,text=".",width=5,height=3, 
                fg="black",bg="silver", 
                command=lambda:self.action('.')).grid(row=5, column=2) 

            Button(master,text="7",width=5,height=3, 
                fg="black",bg="light blue", 
                command=lambda:self.action('7')).grid(row=2, column=0) 

            Button(master,text="8",width=5,height=3, 
                fg="black",bg="light blue", 
                command=lambda:self.action(8)).grid(row=2, column=1) 

            Button(master,text="9",width=5,height=3, 
                fg="black",bg="light blue", 
                command=lambda:self.action(9)).grid(row=2, column=2) 

            Button(master,text="4",width=5,height=3, 
                fg="black",bg="light blue", 
                command=lambda:self.action(4)).grid(row=3, column=0) 

            Button(master,text="5",width=5,height=3,
                fg="black",bg="light blue", 
                command=lambda:self.action(5)).grid(row=3, column=1) 

            Button(master,text="6",width=5,height=3, 
                fg="black",bg="light blue", 
                command=lambda:self.action(6)).grid(row=3, column=2) 

            Button(master,text="1",width=5,height=3, 
                fg="black",bg="light blue", 
                command=lambda:self.action(1)).grid(row=4, column=0) 

            Button(master,text="2",width=5,height=3, 
                fg="black",bg="light blue", 
                command=lambda:self.action(2)).grid(row=4, column=1) 

            Button(master,text="3",width=5,height=3, 
                fg="black",bg="light blue", 
                command=lambda:self.action(3)).grid(row=4, column=2) 

            Button(master,text="0",width=5,height=3, 
                fg="black",bg="light blue", 
                command=lambda:self.action(0)).grid(row=5, column=1) 

            Button(master,text="+/-",width=5,height=3, 
                fg="black",bg="silver", 
                command=lambda:self.signchange()).grid(row=5, column=0) 

            Button(master,text="(",width=5,height=3, 
                fg="black",bg="silver", 
                command=lambda:self.action('(')).grid(row=3, column=5) 

            Button(master,text=")",width=5,height=3, 
                fg="black",bg="silver", 
                command=lambda:self.action(')')).grid(row=3, column=6) 

            Button(master,text="sqrt",width=5,height=3, 
                fg="black",bg="silver", 
                command=lambda:self.squareroot()).grid(row=4, column=5) 

            Button(master,text="x²",width=5,height=3, 
                fg="black",bg="silver", 
                command=lambda:self.square()).grid(row=4, column=6) 

# Information about the use of bitwise operators was gathered from this link:
# https://www.geeksforgeeks.org/python-bitwise-operators/
# following code utilizes bitwise operations such as AND, OR, NOT, XOR, BSL, and BSR. 
            
            Button(master,text="AND",width=5,height=3, 
                fg="black",bg="pink", 
                command=lambda:self.action('&')).grid(row=1, column=0, pady=5)

            Button(master,text="OR",width=5,height=3, 
                fg="black",bg="pink", 
                command=lambda:self.action('|')).grid(row=1, column=1)
            
            Button(master,text="NOT",width=5,height=3, 
                fg="black",bg="pink", 
                command=lambda:self.action('~')).grid(row=1, column=2)

            Button(master,text="XOR",width=5,height=3, 
                fg="black",bg="pink", 
                command=lambda:self.action('^')).grid(row=1, column=3)
            
            Button(master,text="<<",width=5,height=3, 
                fg="black",bg="pink", 
                command=lambda:self.action('<<')).grid(row=1, column=5)
            
            Button(master,text=">>",width=5,height=3, 
                fg="black",bg="pink", 
                command=lambda:self.action('>>')).grid(row=1, column=6)

# following code calls on the functions that allow for hexadecimal, decimal, 
# octal, and binary conversion

            Button(master,text="HEX",width=5,height=3,
                fg="black",bg="orange",
                command=lambda:self.hex()).grid(row=2, column=4, padx=5)

            Button(master,text="DEC",width=5,height=3,
                fg="black",bg="orange",
                command=lambda:self.dec()).grid(row=3, column=4)

            Button(master,text="OCT",width=5,height=3,
                fg="black",bg="orange",
                command=lambda:self.oct()).grid(row=4, column=4)

            Button(master,text="BIN",width=5,height=3,
                fg="black",bg="orange",
                command=lambda:self.bin()).grid(row=5, column=4)            
            

# Driver Code 
root = Tk() 
obj=calc(root) # object instantiated 

root.mainloop() 
