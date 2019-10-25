from tkinter import *

#docs: http://effbot.org/tkinterbook/tkinter-index.htm#class-reference


"""
    App Layout

     __________________
    |                  |        Grid Geometry Manager
     __________________         
    | C | +/- | % | /  |        Bugs:
    |------------------|            can add > 1 operator
    | 7  | 8  | 9  | X |            long numbers stretch the window
    | 4  | 5  |  6 | - |            
    | 1  | 2  |  3 | + |        Todo:
    | 0       |  . | = |            add operations functionality
    --------------------

"""

class App:

    def __init__(self, master):
        self.queue_str = ""
        queue_display = []
        str_display = StringVar()
        display = Label(master, textvariable=str_display, bg="grey").grid(row=0)

        def updateDisplay(data):
            str_display.set(data)

        def cancel():
            self.queue_str = ""
            queue_display.clear()
            updateDisplay(self.queue_str)

        def backspace():
            self.queue_str = self.queue_str[:-1]
            updateDisplay(self.queue_str)

        def onclick(char):
            self.queue_str += char
            updateDisplay(self.queue_str)


        #1st row
        Button(text="C", fg="red", command=cancel).grid(row=1)
        Button(text="+/-").grid(row=1, column=1)
        Button(text="%", command=lambda: onclick("%")).grid(row=1, column=2)
        Button(text="/", command=lambda: onclick("/")).grid(row=1, column=3)

        #2nd row
        Button(text="7", command=lambda: onclick("7")).grid(row=2)
        Button(text="8", command=lambda: onclick("8")).grid(row=2, column=1)
        Button(text="9", command=lambda: onclick("9")).grid(row=2, column=2)
        Button(text="X", command=lambda: onclick("*")).grid(row=2, column=3)

        #3rd row
        Button(text="4", command=lambda: onclick("4")).grid(row=3)
        Button(text="5", command=lambda: onclick("5")).grid(row=3, column=1)
        Button(text="6", command=lambda: onclick("6")).grid(row=3, column=2)
        Button(text="-", command=lambda: onclick("-")).grid(row=3, column=3)

        #4th row
        Button(text="1", command=lambda: onclick("1")).grid(row=4)
        Button(text="2", command=lambda: onclick("2")).grid(row=4, column=1)
        Button(text="3", command=lambda: onclick("3")).grid(row=4, column=2)
        Button(text="+", command=lambda: onclick("+")).grid(row=4, column=3)

        #5th row
        Button(text="0", command=lambda: onclick("0")).grid(row=5)
        Button(text="<<", fg="red", command=backspace).grid(row=5, column=1)
        Button(text=".").grid(row=5, column=2)
        Button(text="=").grid(row=5, column=3)


root = Tk()
app = App(root)
root.mainloop()