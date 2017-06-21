

#creat an investment calculator

from tkinter import * #import all definitions from tkinter

class FutureValueCalculator:
    def __init__(self):
        window = Tk() # create a window
        window.title("Future Value Calculator") #set a title

        Label(window, text = "Investment Amount").grid(row = 1,
            column =1, sticky = W)
        Label(window, text = "years").grid(row = 2,
            column =1, sticky = W)
        Label(window, text = "annual Interest Rate").grid(row = 3,
            column =1, sticky = W)                                            
        Label(window, text = "future Value").grid(row = 4,
            column =1, sticky = W)

        self.investmentAmountVar = StringVar()
        Entry(window, textvariable = self.investmentAmountVar,
            justify = RIGHT).grid( row = 1, column = 2)

        self.yearsVar = StringVar()
        Entry(window, textvariable = self.yearsVar,
            justify = RIGHT).grid( row = 2, column = 2)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar,
            justify = RIGHT).grid( row = 3, column = 2)

        self.futureValueVar = StringVar()
        lblFutureValue = Label(window,
            textvariable = self.futureValueVar).grid(row = 4,column = 2,
            sticky = E)

        btComputeValue = Button(window, text = "Compute Value",
            command = self.computeValue).grid(row = 5, column = 2, sticky = E)

        window.mainloop() #create an event loop

    def computeValue(self):
        futureValue = self.getValue(float(self.investmentAmountVar.get()),
            float(self.annualInterestRateVar.get())/1200,
            int(self.yearsVar.get()))
        self.futureValueVar.set(format(futureValue, '10.2f'))

    def getValue(self, investmentAmount, annualInterestRate, years):
        futureValue = investmentAmount * (1 + annualInterestRate)**(years *
            12)
        return futureValue;
        
FutureValueCalculator() #create GUI
        
        
        

