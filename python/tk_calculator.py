from tkinter import *


"""

    docs: http://effbot.org/tkinterbook/tkinter-index.htm#class-reference
    keysym manual page: http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm

    App Layout
    ----------
     __________________
    |                  |        Grid Geometry Manager
     __________________         
    | C | +/- | % | /  |        Bugs:
    |------------------|            can add > 1 operator [SOLVED]xxxxxxx
    | 7  | 8  | 9  | X |            long numbers stretch the window
    | 4  | 5  |  6 | - |            
    | 1  | 2  |  3 | + |        Todo:
    | 0  | << |  . | = |            implement operate function XXXXXXXXXXXXX
    --------------------            implemente operation with negative numbers
                                    let the user insert numbers with keyboard
"""

class App:

    def __init__(self, master):
        self.queue_str = ""
        self.operating = False
        self.negative_result = False
        self.operations =  ("+", "-", "/", "%", "*")
        queue_display = []
        str_display = StringVar()
        master.columnconfigure(1, weight=1)
        display = Label(master, textvariable=str_display, bg="grey").grid(row=0, column=1, sticky=W+E)


        def updateDisplay(data):
            str_display.set(data)


        def cancel():
            self.queue_str = ""
            self.operating = False
            queue_display.clear()
            updateDisplay(self.queue_str)


        def backspace():

            if self.queue_str[-1] in self.operations:
                self.operating = False

            #delete last character and update display
            self.queue_str = self.queue_str[:-1]
            updateDisplay(self.queue_str)


        def onclick(char):
        
            if len(self.queue_str) > 0:
                if self.queue_str[-1] in self.operations:
                    self.operating = True
                    #self.queue_str += char
                    #updateDisplay(self.queue_str)

            if self.operating == True:
                if char not in self.operations:
                    self.queue_str += char
                    updateDisplay(self.queue_str)

            if self.operating == False or self.queue_str == "":
                self.queue_str += char
                updateDisplay(self.queue_str)  

        #TODO
        def negative_operate(a, b, operation_todo):
            pass

        def operate():
            operation_str = self.queue_str
            got_first_var = False
            a = b = ""
            operation_todo = ""
            #working on: Operation with Negative numbers

            if self.negative_result == True:
                negative_operate(a, b, operation_todo)
            
            else: #int operations
                for i in operation_str:
                    if got_first_var == False:
                        if i not in self.operations:
                            #store first number in b variable
                            a += i
                        else:
                            #time to store values in the a variable
                            got_first_var = True
                            
                            for x in self.operations:
                                if i == x:
                                    operation_todo = x
                                    break
                    else:
                        #store number after operation in a variable
                        b += i

            
            #time to process operation
            operation_result = 0
            a = float(a)        # ValueError problem
            b = float(b)
            if operation_todo == "*":
                operation_result = a * b
            elif operation_todo == "/":
                operation_result = a / b
            elif operation_todo == "%":
                operation_result = a % b
            elif operation_todo == "+":
                operation_result = a + b
            elif operation_todo == "-":
                operation_result = a - b
            
            cancel()
            if operation_result < 0:
                self.negative_result = True
            else:
                self.negative_result = False

            self.queue_str = str(operation_result)
            updateDisplay(self.queue_str)

        #1st row
        Button(text="C", width=6, fg="red", command=cancel).grid(row=1)
        Button(text="+/-", width=6).grid(row=1, column=1)
        Button(text="%", width=6, command=lambda: onclick("%")).grid(row=1, column=2)
        Button(text="/", width=6, command=lambda: onclick("/")).grid(row=1, column=3)

        #2nd row
        Button(text="7", width=6, command=lambda: onclick("7")).grid(row=2)
        Button(text="8", width=6, command=lambda: onclick("8")).grid(row=2, column=1)
        Button(text="9", width=6, command=lambda: onclick("9")).grid(row=2, column=2)
        Button(text="X", width=6, command=lambda: onclick("*")).grid(row=2, column=3)

        #3rd row
        Button(text="4", width=6, command=lambda: onclick("4")).grid(row=3)
        Button(text="5", width=6, command=lambda: onclick("5")).grid(row=3, column=1)
        Button(text="6", width=6, command=lambda: onclick("6")).grid(row=3, column=2)
        Button(text="-", width=6, command=lambda: onclick("-")).grid(row=3, column=3)

        #4th row
        Button(text="1", width=6, command=lambda: onclick("1")).grid(row=4)
        Button(text="2", width=6, command=lambda: onclick("2")).grid(row=4, column=1)
        Button(text="3", width=6, command=lambda: onclick("3")).grid(row=4, column=2)
        Button(text="+", width=6, command=lambda: onclick("+")).grid(row=4, column=3)

        #5th row
        Button(text="0", width=6, command=lambda: onclick("0")).grid(row=5)
        Button(text="<<", width=6, fg="red", command=backspace).grid(row=5, column=1)
        Button(text=".", width=6).grid(row=5, column=2)
        Button(text="=", width=6, command=operate).grid(row=5, column=3)

        #capturing keyboard input
        def keypressed(event):
            #event.keysym returns <key> as a str.
            
            print(f"keysym = {event.keysym}")
            #onclick(event.keysym)

        #callback receives event as parameter by default
        master.bind("<0>", keypressed) 
        master.bind("<9>", keypressed)
        master.bind("<8>", keypressed)
        master.bind("<7>", keypressed)
        master.bind("<6>", keypressed)  # from 6 to 9 it works. and 0
        master.bind("<5>", keypressed)
        master.bind("<4>", keypressed)
        master.bind("<3>", keypressed)
        master.bind("<2>", keypressed)
        master.bind("<1>", keypressed)
        
        #master.bin() implement backspace


root = Tk()
app = App(root)
root.mainloop()