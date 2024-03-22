import cx_Oracle
from tkinter import *
from tkinter import messagebox



val = 0
def CheckBox():
    val = 1
    if val ==  1:
        Button(text = 'INSERT', width = 30, height = 1, borderwidth=1, relief="solid", state = 'active', command = insert).place( x = 260, y = 465)

   
def insert ():
    con = cx_Oracle.connect('system/12345@DESKTOP-VU0HSP2:1521/XE')
    cur = con.cursor()
    cur.execute("insert into CyberCafe(firstname, lastname, age, phone) values('"+First_name.get()+"','"+Last_name.get()+"','"+Age.get()+"','"+Phone.get()+"')")
    messagebox.showinfo('Record Inserted')
    con.commit()

    
    
screen = Tk()
screen.geometry('500x500')
screen.title('CyberCafe User Entry')

#Heading 
heading = Label(text = 'Welcome to CyberSpace!!!', font = 'Arial 14 bold', bg = 'grey', fg = 'white', width = '500', height ='5',borderwidth=1, relief="solid")
heading.pack()

#Panel
panel = Label(bg = 'white', fg = 'black', width = '500', height ='25', borderwidth=1, relief="solid")
panel.place( x = 1, y = 80)


#Image
photo = PhotoImage( file = 'E:\VSIT\AM\DDD.gif')
image = Label( image = photo, borderwidth=1, relief="solid")
image.place( x = 270, y = 90)

#Insert_Data label
Label(panel, text = 'First name ',bg = 'white').place( x = 15, y = 10)
Label(panel, text = 'Last name ',bg = 'white').place(x = 15, y = 70 )
Label(panel, text = 'Age ',bg = 'white').place(x = 15, y = 130)
Label(panel, text = 'Phone ',bg = 'white').place(x = 15, y = 190)



#Entry_vals
First_name = Entry(panel, width = 30, borderwidth=1, relief="solid")
First_name.place( x = 15, y = 30)
Last_name = Entry(panel, width = 30, borderwidth=1, relief="solid")
Last_name.place( x = 15, y = 90)
Age = Entry(panel, width = 30, borderwidth=1, relief="solid")
Age.place( x = 15, y = 150)
Phone = Entry(panel, width = 30, borderwidth=1, relief="solid")
Phone.place( x = 15, y = 210)


#Button vals
Button(text = 'INSERT', width = 30, height = 1, borderwidth=1, relief="solid", state = 'disabled').place( x = 260, y = 465)
Checkbutton ( text = 'Agree to T&C', onvalue = 1 , offvalue = 0, command = CheckBox).place( x = 50, y = 465)

#Label
#Label(panel, text = 'T & C\n1. Minors Not Allowed \nunless Accompanied\n\n2. Do Not Exceed Time Limit\n\n3. Strict action will be taken agaisnt \npornographic content ',bg = 'white',).place(x = 1, y = 240)
Label(panel, text = 'T & C ',bg = 'white', font = 'Helvetica 12 bold').place(x = 15, y = 260)
Label(panel, text = '1.Minors Not Allowed unless Accompanied  ',bg = 'white').place(x = 15, y = 280)
Label(panel, text = '2. Turn off the PC after use',bg = 'white').place(x = 15, y = 300)
Label(panel, text = '3. Strict action will be taken agaisnt \npornographic content',bg = 'white').place(x = 15, y = 320)

screen.mainloop()

                         









