
from tkinter import *
import tkinter 

window_1 = Tk() 
# adding title to the window 

window_1.title("Hello Martina ")
window_1.geometry('700x500')

num = 0
num2=0
Label(window_1, font =('Helvetica bold',22), text = 'Score Board',bg ='yellow').place(x=260,y=20)
#callback : function for changing label
label1 = Label(window_1, justify=CENTER)
label1.pack()
def increment():

	global num
	if(num<9):
		num += 1
		lbl.configure(text=num) 
	else:
		num=9
def increment2():

	global num2
	if(num2<9):
		num2 += 1
		lb2.configure(text=num2) 
	else:
		num=9
def zero():
		global num2 
		global num
		num2=0
		num=0
		lb2.configure(text=num2)
		lbl.configure(text=num) 		

photo_1 = PhotoImage(file='MOR.png')
photo_2 = PhotoImage(file='CRO.png')

# editing of the image resizing of it 
# resizing decreased by increasing the number 
photo_1 = photo_1.subsample(2,2)
photo_2 = photo_2.subsample(2,2)
re  =Button(window_1 , text = "Restart Match " , bd = '5',background="green" , command = zero)
re.place(x=300,y=400)
B_1  =Button(window_1 , text = "Increment The button " , bd = '5',background="red" ,image=photo_1, command = increment)

B_1.place(x=170,y=190)
lbl=Label(window_1, text=num,font = ('Verdana', 15),bd = '5',background="black",fg="red")
lbl.place(x=195+20,y=290+40+20)

B_2  =Button(window_1 , text = "Increment The button " , bd = '5',background="blue" ,image=photo_2, command = increment2)

B_2.place(x=400,y=190)
lb2=Label(window_1, text=num2,font = ('Verdana', 15),bd = '5',background="black",fg="red")
lb2.place(x=195+20+150+70+20,y=290+40+20)
b2 =Button(window_1 , text = "Close the window" ,background="red", bd = '10' , command = window_1.destroy)
b2.pack(side = BOTTOM)
window_1.mainloop()