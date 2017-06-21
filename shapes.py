

#create shapes


from tkinter import * # Import tkinter
    
class Shapes:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Canvas Demo") # Set title
        
        # Place self.canvas in the window
        self.canvas = Canvas(window, width = 200, height = 100, 
            bg = "white")
        self.canvas.pack()
        
        # Place buttons in frame
        frame1 = Frame(window)
        frame1.pack()
        self.v2 = IntVar()
        self.v1 = IntVar()
        rbRectangle = Radiobutton(frame1, text = "Rectangle",
            variable = self.v2, value = 1, command = self.displayRect) 
        rbOval = Radiobutton(frame1, text = "Oval", variable = self.v2,
            value = 2, command = self.displayOval) 
        cbtFill = Checkbutton(frame1, text = "Fill", variable = self.v1) 
        
        
        rbRectangle.grid(row = 1, column = 1)
        rbOval.grid(row = 1, column = 2)
        cbtFill.grid(row = 1, column = 3)
        
        window.mainloop() # Create an event loop

    def processRadiobutton(self):
        print(("Rectangle" if self.v2.get() == 1 else "Oval") 
            + " is selected " )

     # Display a rectangle
    def displayRect(self):
        if self.v1.get() == 1:
            self.canvas.create_rectangle(10, 10, 190, 90, fill = "Red",
            tags = "rect")
        else:
            self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

    # Display an oval
    def displayOval(self):
        if self.v1.get() == 1:
            self.canvas.create_oval(10, 10, 190, 90, fill = "Red",
                tags = "oval")
        else:
            self.canvas.create_oval(10, 10, 190, 90,
            tags = "oval")

Shapes()
