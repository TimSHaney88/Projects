#exercise 9.7

from tkinter import * # Import tkinter

#draw a graph


class Line:
    
    def __init__(self):
        window = Tk() # Create a window
        window.title("Grid") # Set title
        frame = Frame(window)
        frame.pack()
        
        # Place self.canvas in the window
        self.canvas = Canvas(window, width = 100, height = 100, 
            bg = "white")
        self.canvas.pack()
        #btLine = Button(frame, text = "Grid",
        btLine = command = self.displayLine
        #btLine = self.displayLine
        #btLine.grid(row = 1, column = 5)
        Line.displayLine(self)


 # Display a line
    def displayLine(self):
        x1 = 20
        y1 = 10
        y2 = 90
        
        x3 = 10
        y3 = 20
        x4 = 90
       
        for i in range (0, 7):
            self.canvas.create_line(x1, y1, x1, y2, fill = "red", tags = "line")
            x1 = x1 + 10
            
        for k in range (0, 7):
            self.canvas.create_line(x3, y3, x4, y3, fill = "blue",
            tags = "line")
            y3 = y3 + 10
                
                 
                
                

  
Line()
