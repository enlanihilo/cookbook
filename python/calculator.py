from tkinter import *


"""

    docs: http://effbot.org/tkinterbook/tkinter-index.htm#class-reference
    keysym manual page: http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm

    App Layout
    ----------
     __________________
    |                  |        Grid Geometry Manager
     __________________         
    | << | +/- | % | / |        Bugs:
    |------------------|            can add > 1 operator [SOLVED]xxxxxxx
    | 7  | 8  | 9  | X |            long numbers stretch the window
    | 4  | 5  |  6 | - |            
    | 1  | 2  |  3 | + |        Todo:
    | 0  |  Clear  | = |            +/- functionality
    --------------------            
"""

class App:

    def __init__(self, master):
        self.queue_str = ""
        self.operating = False
        self.operations =  ("+", "-", "/", "%", "*")
        self.queue_display = []
        self.operation_todo = ""
        self.operator_idx = 0
        str_display = StringVar()
        master.columnconfigure(1, weight=1)
        display = Label(master, textvariable=str_display, bg="grey").grid(row=0, column=1, sticky=W+E)


        def updateDisplay(data):
            str_display.set(data)


        def cancel():
            self.queue_str = ""
            self.operating = False
            self.queue_display.clear()
            updateDisplay(self.queue_str)


        def backspace():

            try:
                if len(self.queue_str) == 0:
                    cancel()

                if self.queue_str[-1] in self.operations:
                    self.operating = False

                #delete last character and update display    
                self.queue_str = self.queue_str[:-1]
                updateDisplay(self.queue_str)

            except:
                print("There is nothing to cancel.")


        def onclick(char):

            if len(self.queue_str) > 0:
                if self.queue_str[0] == "-":
                    pass

                if self.queue_str[-1] in self.operations and len(self.queue_str) > 1:
                    self.operating = True
                    self.operation_todo = self.queue_str[-1]
                    self.queue_display.append(self.queue_str[:-1])
                    

            if self.operating == True:
                if char not in self.operations:
                    self.queue_str += char
                    updateDisplay(self.queue_str)

            if self.operating == False or self.queue_str == "":
                self.queue_str += char
                updateDisplay(self.queue_str)  


        def operate():
            #grab the operator index so you can grab the 2nd number 
            for c in self.queue_str:
                if self.queue_str.find(c) > 0 and c == self.operation_todo:
                    self.operator_idx =  self.queue_str.find(c)
            #append to the self.queue_display
            self.queue_display.append(self.queue_str[self.operator_idx+1:])

            #calculation time:
            #print(f"Todo: {self.queue_display[0]} {self.operation_todo} {self.queue_display[1]}")
            
            if self.queue_display[0][0] == "-":
                a = float(self.queue_display[0][1:])
                a *= -1
            else:
                a = float(self.queue_display[0])

            b = float(self.queue_display[1])
            if self.operation_todo == "+":
                result = a + b
            if self.operation_todo == "-":
                result = a - b
            if self.operation_todo == "%":
                result = a % b
            if self.operation_todo == "/":
                result = a / b
            if self.operation_todo == "*":
                result = a * b

            result = str(result)
            cancel()
            updateDisplay(result)


        #1st row
        Button(text="<<", width=6, fg="red", command=backspace).grid(row=1)
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
        Button(text="Clear", width=6, fg="red", command=cancel).grid(row=5, column=1)
        Button(text="=", width=6, command=operate).grid(row=5, column=3)

        #capturing keyboard input
        def keypressed(event):
            #print(f"keysym = {event.keysym}")

            if event.keysym == "c":
                cancel()          
            elif event.keysym == "plus":
                onclick("+")
            elif event.keysym == "slash":
                onclick("/")
            elif event.keysym == "minus":
                onclick("-")
            elif event.keysym == "Return":
                operate()
            elif event.keysym == "percent":
                onclick("%")
            elif event.keysym == "asterisk":
                onclick("*")
            elif event.keysym == "BackSpace":
                backspace()
            else:
                onclick(event.keysym)

        #callback receives event as parameter by default
        master.bind("<Key-0>", keypressed)  
        master.bind("<Key-9>", keypressed)  
        master.bind("<Key-8>", keypressed)  
        master.bind("<Key-7>", keypressed)  
        master.bind("<Key-6>", keypressed)  
        master.bind("<Key-5>", keypressed)  
        master.bind("<Key-4>", keypressed)  
        master.bind("<Key-3>", keypressed)  
        master.bind("<Key-2>", keypressed)   
        master.bind("<Key-1>", keypressed)
        master.bind("<c>", keypressed)
        master.bind("<plus>", keypressed)
        master.bind("<slash>", keypressed)
        master.bind("<minus>", keypressed)
        master.bind("<Return>", keypressed)
        master.bind("<percent>", keypressed)
        master.bind("<asterisk>", keypressed)
        master.bind("<BackSpace>", keypressed)
        

root = Tk()
app = App(root)
root.mainloop()