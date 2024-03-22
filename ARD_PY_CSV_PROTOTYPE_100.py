import serial #Connecting Arduino to Python to File
import csv #reading from csv to python
import numpy as np # Math begins
import tkinter as tk #gui
from tkinter import*



#Conencting Arduino to Python
serial_data = serial.Serial('COM5', baudrate = 9600, timeout =2)



#GUI
def Enter():
    global L2
    Entry_val = int(E1.get())
    global Final_val
    L2.grid_forget()
    L2 = Label(W, text = "Please Wait for 10 seconds !")
    L2.grid(row = 2, column =0, padx = 5, pady = 5, columnspan = 2)

    #Connecting Pytthon data to file
    textfile = open('ARD.csv', 'w')



    # Loop for collecting data
    
    for i in range(10):
        and_data = serial_data.readline().decode('ascii')
        print(and_data)
        textfile.write(and_data)

    textfile.close()
    L2.grid_forget()
    L2 = Label(W, text = "Data Collected!!!")
    L2.grid(row = 2, column =0, padx = 5, pady = 5, columnspan = 2)
    

    

    #Reading csv data back to python

    time = []
    distance = []
    with open('ARD.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row:
                continue
            else:
                time.append(int(row[0]))
                distance.append(float(row[1]))


                

    # Linear Regression


    def regression ( x , y, val):
        N = 0  # Number of elements
        Sum_y = 0  # Summation of Y elemennts
        Sum_x = 0  # Summation of X elements
        SQ_x = 0  #  Square of X elemets
        SQ_y = 0  # Square of Y elements
        MUL = 0  # Multiplication and sum of X and Y elements


        # Length
    
        N = len(x)
    

        # Sum of y elements
    
        for i in y:
            SQ_y= SQ_y + i**2
            Sum_y = Sum_y + i
        

        # Sum of x elements
    
        for i in x:
            SQ_x = SQ_x + i**2
            Sum_x = Sum_x + i

        

        #Product of x and y
        
        for i in range(0,N):
            MUL = MUL + x[i]*y[i]
            NUMBER = round(MUL,3)


        # Generating eqn using 
    
        L1 = [[N, Sum_x], [Sum_x, SQ_x]]
        L2 = [Sum_y , NUMBER]

        # Solving Equations

        R = np.linalg.inv(L1).dot(L2)
        Y = R[0] + (R[1]*val)
        #print(round(Y,3))

        return (round(Y,3))
    
    Final_val = regression(time, distance, Entry_val)
    L2.grid_forget()
    L2 = Label(W, text = Final_val)
    L2.grid(row = 2, column = 0, padx = 5, pady = 5, columnspan = 2)
    
    
    
    

W = tk.Tk()
W.title(" Distance Predictor app ")
L1 = Label(W,text = "Enter Time stamp: ")
L1.grid(row = 0, column = 0, padx = 5, pady = 5)
L2 = Label(W, text = "Welcome!!!")
L2.grid(row = 2, column =0, padx = 5, pady = 5, columnspan = 2)
E1 = Entry(W, width = 10)
E1.grid(row = 0, column = 1, padx = 5, pady = 5)
B1 = Button(text = "Submit", width = 5, command = Enter)
B1.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan  = 2)


W.mainloop()
















    
