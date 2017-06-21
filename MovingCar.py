

from tkinter import * # Import tkinter
import time
    
class Car:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Car") # Set title
        
        # Place self.canvas in the window
        self.canvas = Canvas(window, width = 300, height = 300, 
            bg = "white")
        self.canvas.pack()
        
        # Place buttons in frame
        frame = Frame(window)
        frame.pack()
        
        btRectangle = command = self.displayRect
        btOval = command = self.displayOval
        btLine = command = self.displayLine
        x=10
        for i in range (20):
            
            self.canvas.delete("all")
            Car.displayRect(self,x)
            Car.displayOval(self,x)
            Car.displayLine(self,x)
            x=x+20
            self.canvas.update()
            time.sleep(1)
       
       
        
        window.mainloop() # Create an event loop

    # Display a rectangle
    def displayRect(self, x):
        self.canvas.create_rectangle(x, 30, x+70, 50, fill = "orange", tags = "rect")
        
    # Display an oval
    def displayOval(self,x):
        
        self.canvas.create_oval(x+10, 70, x+30, 50, fill = "black", 
            tags = "oval")
        self.canvas.create_oval(x+40, 70, x+60, 50, fill = "black", 
            tags = "oval1")

    def displayLine(self,x): 
         
         self.canvas.create_line(x+10, 30, x+70, 30, fill = "red", tags = "line1")
         self.canvas.create_line(x+10, 30, x+30, 10, fill = "red", tags = "line2")   
         self.canvas.create_line(x+30, 10, x+40, 10, fill = "red", tags = "line3")
         self.canvas.create_line(x+40, 10, x+60, 30, fill = "red", tags = "line4") 
   

Car() # Create GUI



