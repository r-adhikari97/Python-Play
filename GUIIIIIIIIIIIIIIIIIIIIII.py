from tkinter import*



#Functions

def Button_Click(n):
    current = E1.get()
    E1.delete(0,END)
    E1.insert(0,str(current)+str(n))

def Button_Add():
    global op
    op = 1
    global val
    val = int(E1.get())
    E1.delete(0,END)

def Button_Sub():
    global op
    op = 2
    global val
    val = int(E1.get())
    E1.delete(0,END)

def Button_Multiply():
    global op
    op = 3
    global val
    val = int(E1.get())
    E1.delete(0,END)

def Button_Div():
    global op
    op = 4
    global val
    val = int(E1.get())
    E1.delete(0,END)
    
    
def Equal_To():
    val1 = int(E1.get())
    E1.delete(0,END)
    if op == 1:
        X = val + val1
        E1.insert(0,int(X))
    elif op == 2:
        X = val - val1
        E1.insert(0,int(X))
    elif op == 3:
        X = val * val1
        E1.insert(0,int(X))
    elif op == 4:
        X = val / val1
        E1.insert(0,float(X))
    else:
        a = 'Enter valid Operator'
        E1.insert(0,a)

    
def Button_CLR():
    E1.delete(0,END)
    
    
    

W = Tk()
W.title('Calculator')

#Entry
E1= Entry(W,width = 30,borderwidth = 2,relief = 'solid', font = ('Arial',14))
E1.grid(columnspan = 4,row = 0, column=0,padx= 10, pady =10)


#Button
B9 = Button(W,text= '9',padx = 35, pady =15,borderwidth = 1,relief = 'solid', command = lambda: Button_Click(9)).grid(row = 2, column = 0)
B8 = Button(W,text= '8',padx = 35, pady =15,borderwidth = 1,relief = 'solid', command = lambda: Button_Click(8)).grid(row = 2, column = 1)
B7 = Button(W,text= '7',padx = 35, pady =15,borderwidth = 1,relief = 'solid', command = lambda: Button_Click(7)).grid(row = 2, column = 2)
B_Add = Button(W,text= '+',padx = 32, pady =15,borderwidth = 1,relief = 'solid', command = Button_Add).grid(row = 2, column = 3)


B6 = Button(W,text= '6',padx = 35, pady =15,borderwidth = 1,relief = 'solid', command = lambda: Button_Click(6)).grid(row = 3, column = 0)
B5 = Button(W,text= '5',padx = 35, pady =15,borderwidth = 1,relief = 'solid', command = lambda: Button_Click(5)).grid(row = 3, column = 1)
B4 = Button(W,text= '4',padx = 35, pady =15,borderwidth = 1,relief = 'solid', command = lambda: Button_Click(4)).grid(row = 3, column = 2)
B_Sub = Button(W,text= '-',padx = 33, pady =15,borderwidth = 1,relief = 'solid', command = Button_Sub).grid(row = 3, column = 3)


B3 = Button(W,text= '3',padx = 35, pady =15,borderwidth = 1,relief = 'solid', command = lambda: Button_Click(3)).grid(row = 4, column = 0)
B2 = Button(W,text= '2',padx = 35, pady =15,borderwidth = 1,relief = 'solid', command = lambda: Button_Click(2)).grid(row = 4, column = 1)
B1 = Button(W,text= '1',padx = 35, pady =15,borderwidth = 1,relief = 'solid', command = lambda: Button_Click(1)).grid(row = 4, column = 2)
B_Multiply = Button(W,text= 'x',padx = 32, pady =15,borderwidth = 1,relief = 'solid', command = Button_Multiply).grid(row = 4, column = 3)


B0 = Button(W,text= '0',padx = 35, pady =15,borderwidth = 1,relief = 'solid',command = lambda: Button_Click(0)).grid(row = 5, column = 0)
B_EQ = Button(W,text= '=',padx = 35, pady =15,borderwidth = 1,relief = 'solid', command = Equal_To).grid(row = 5, column = 1)
B_CLR = Button(W,text= 'CLR',padx = 27, pady =15,borderwidth = 1,relief = 'solid', command = Button_CLR).grid(row = 5, column = 2)
B_Div = Button(W,text = '/',padx = 33, pady =15,borderwidth = 1,relief = 'solid', command = Button_Div).grid(row = 5, column = 3) 

W.mainloop()

