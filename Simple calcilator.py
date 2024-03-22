from tkinter import*

#Base
W = Tk()
W.title('Simple Calculator')

#Functions



def Display(n):
    current = E1.get()
    E1.delete(0,END)
    E1.insert(0,str(current) + str(n))


def CLR():
    E1.delete(0,END)


def ADD():
    global op
    op = 1
    global v1
    v1 = E1.get()
    E1.delete(0,END)

def SUB():
    global op
    op = 2
    global v1
    v1 = E1.get()
    E1.delete(0,END)

def Multiply():
    global op
    op = 3
    global v1
    v1 = E1.get()
    E1.delete(0,END)


def DIV():
    global op
    op = 4
    global v1
    v1 = E1.get()
    E1.delete(0,END)



def Equal():
    global v2
    v2 = E1.get()
    E1.delete(0,END)
    if op == 1:
        E1.insert(0,int(v1)+int(v2))
    elif op == 2:
        E1.insert(0,int(v1)-int(v2))
    elif op == 3:
        E1.insert(0,int(v1)*int(v2))
    elif op == 4:
        E1.insert(0,int(v1)/int(v2))
    




#Entry
E1 = Entry(W, width = 35, font =("Arial", 18), borderwidth= 2, relief = 'solid')
E1.grid(row = 0, column = 0, columnspan= 4,padx = 10, pady = 10)

#Button
B9 = Button(W,text ='9', font =("Arial", 12),padx = 50, pady = 20,borderwidth= 1, relief = 'solid', command = lambda: Display(9)).grid(row = 1, column = 0,pady = 5)
B8 = Button(W,text ='8', font =("Arial", 12),padx = 50, pady = 20,borderwidth= 1, relief = 'solid', command = lambda: Display(8)).grid(row = 1, column = 1,pady = 5)
B7 = Button(W,text ='7', font =("Arial", 12),padx = 50, pady = 20,borderwidth= 1, relief = 'solid', command = lambda: Display(7)).grid(row = 1, column = 2,pady = 5)
B_Add = Button(W,text ='+',font =("Arial", 12),padx = 50, pady = 20,borderwidth= 1, relief = 'solid', command = ADD).grid(row = 1, column = 3,pady = 5)

B6 =  Button(W,text ='6', font =("Arial", 12),padx = 50, pady = 20,borderwidth= 1, relief = 'solid', command = lambda: Display(6)).grid(row = 2, column = 0,pady = 5)
B5 =  Button(W,text ='5', font =("Arial", 12),padx = 50, pady = 20,borderwidth= 1, relief = 'solid', command = lambda: Display(5)).grid(row = 2, column = 1,pady = 5)
B4 =  Button(W,text ='4',padx = 50, pady = 20, font =("Arial", 12),borderwidth= 1, relief = 'solid', command = lambda: Display(4)).grid(row = 2, column = 2,pady = 5)
B_Sub =  Button(W,text ='--', font =("Arial", 12),padx = 50, pady = 20,borderwidth= 1, relief = 'solid', command = SUB).grid(row = 2, column = 3,pady = 5)

B3 =  Button(W,text = '3',padx = 50, pady = 20, font =("Arial", 12),borderwidth= 1, relief = 'solid', command = lambda: Display(3)).grid(row = 3, column = 0,pady = 5)
B2 =  Button(W,text ='2',padx = 50, pady = 20, font =("Arial", 12),borderwidth= 1, relief = 'solid', command = lambda: Display(2)).grid(row = 3, column = 1,pady = 5)
B1 =  Button(W,text ='1',padx = 50, pady = 20, font =("Arial", 12),borderwidth= 1, relief = 'solid', command = lambda: Display(1)).grid(row = 3, column = 2,pady = 5)
B_Multiply = Button(W,text ='x',padx = 50, pady = 20, font =("Arial", 12),borderwidth= 1, relief = 'solid',command = Multiply).grid(row = 3, column = 3,pady = 5)

B0 =  Button(W,text ='0',padx = 50, pady = 20,borderwidth= 1, relief = 'solid', font =("Arial", 12), command = lambda: Display(0)).grid(row = 4, column = 0,pady = 5)
B_Equal =  Button(W,text ='=',padx = 50, pady = 20, font =("Arial", 12),borderwidth= 1, relief = 'solid', command = Equal).grid(row = 4, column = 1,pady = 5)
B_CLR =  Button(W,text ='C',padx = 50, pady = 20, font =("Arial", 12),borderwidth= 1, relief = 'solid', command = CLR).grid(row = 4, column = 2,pady = 5)
B_Div =  Button(W,text ='/',padx = 50, pady = 20, font =("Arial", 12),borderwidth= 1, relief = 'solid', command = DIV).grid(row = 4, column = 3,pady = 5)

