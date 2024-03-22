from tkinter import*
from PIL import ImageTk,Image

#Functions
def Back():
    #declation
    global index
    global my_Label
    B_Forward.config(state = ACTIVE)
    if index > 0:
        index -= 1
        a = index + 1
        S_Bar = Label(W,text = '{0} of {1}'.format(a,len(Image_List)), border = 1,relief = 'sunken')
        S_Bar.grid(row = 3, column = 0, columnspan = 3,sticky = 'WE',pady = 5)
    else:
        B_Back.config(state = DISABLED)
    my_Label.grid_forget()
    my_Label = Label(image = Image_List[index])
    my_Label.grid(row = 0, column = 0,columnspan = 3)
    #print(index)



   
    

def Forward ():
    #declation
    global index
    global my_Label
    B_Back.config(state = ACTIVE)
    if index < 3:
        index += 1
        a = index + 1
        print(a)
        S_Bar = Label(W,text = '{0} of {1}'.format(a,len(Image_List)), border = 1,relief = 'sunken')
        S_Bar.grid(row = 3, column = 0, columnspan = 3, sticky = 'WE',pady = 5)
    else:
        B_Forward.config(state = DISABLED)
    my_Label.grid_forget()
    my_Label = Label(image = Image_List[index])
    my_Label.grid(row = 0, column = 0,columnspan = 3)
    #print(index)


W = Tk()
W.title('Image Viewer!')
W.iconbitmap('Images/ICON.ico')

#Assigning Images:
img_1 = ImageTk.PhotoImage(Image.open('Images/a.jpg'))
img_2 = ImageTk.PhotoImage(Image.open('Images/b.jpg'))
img_3 = ImageTk.PhotoImage(Image.open('Images/c.jpg'))
img_4 = ImageTk.PhotoImage(Image.open('Images/d.jpg'))

#Image_List

index = 0
Image_List = [img_1, img_2, img_3, img_4]
my_Label = Label(image = Image_List[index])
my_Label.grid(row = 0, column = 0,columnspan = 3)


#Buttons
B_Back = Button(W,text = '<<', command = Back, padx = 10, pady = 10)
B_Back.grid(row = 1, column = 0,padx = 5, pady = 5)
B_Forward = Button(W,text = '>>', command = Forward, padx = 10, pady = 10)
B_Forward.grid(row = 1, column = 2,padx = 5, pady = 5)
B_Exit = Button(W,text = 'Exit', padx = 10, pady = 10, command = W.quit)
B_Exit.grid(row = 1, column = 1,padx = 5, pady = 5)

#Status bar
S_Bar = Label(W,text = '{0} of 4'.format(1),relief = 'sunken')
S_Bar.grid(row = 3, column = 0, columnspan = 3, sticky = 'WE',pady = 5)





















W.mainloop()
