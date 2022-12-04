from tkinter import *
from tkinter import messagebox
import datetime
import random
import time
global low_r
global hi_r
global cnvs
global id_text
global id_needle

def update_gauge():
    global hi_r
    global low_r
    global cnvs
    global id_text
    global id_needle
    newvalue = random.randint(low_r,hi_r)
    cnvs.itemconfig(id_text,text = str(newvalue) + "°C")
    # Rescale value to angle range (0%=120deg, 100%=30 deg)
    angle = 120 * (hi_r - newvalue)/(hi_r - low_r) + 30
    cnvs.itemconfig(id_needle,start = angle)
    root.after(300, update_gauge)  
def humidity_indcator():
	global hi_r
	global low_r
	global cnvs
	global id_text
	global id_needle
	canvas_width = 400
	canvas_height =300
 
	hum_root = Tk()
 
	cnvs = Canvas(hum_root, width=canvas_width, height=canvas_height)
	cnvs.grid(row=2, column=1)
 
	coord = 10, 50, 350, 350 #define the size of the gauge
	low_r = 0 # chart low range
	hi_r = 100 # chart hi range
 
	# Create a background arc with a number of range lines
	numpies = 8
	for i in range(numpies):
		cnvs.create_arc(coord, start=(i*(120/numpies) +30), extent=(120/numpies), fill="white",  width=1)    
 
	# add hi/low bands
	cnvs.create_arc(coord, start=30, extent=120, outline="green", style= "arc", width=40)
	cnvs.create_arc(coord, start=30, extent=20, outline="red", style= "arc", width=40)
	cnvs.create_arc(coord, start=50, extent=20, outline="yellow", style= "arc", width=40)
	# add needle/value pointer
	id_needle = cnvs.create_arc(coord, start= 119, extent=1, width=7)
 
	# Add some labels
	cnvs.create_text(180,15,font="Times 20 italic bold", text="Humidity")
	cnvs.create_text(25,140,font="Times 12 bold", text=low_r)
	cnvs.create_text(330,140,font="Times 12 bold", text=hi_r)
	id_text = cnvs.create_text(170,210,font="Times 15 bold")
 
	hum_root.after(300, update_gauge)
 
	hum_root.mainloop()

def temp_indcator():
    global hi_r
    global low_r
    global cnvs
    global id_text
    global id_needle
    canvas_width = 400
    canvas_height =300
   

    temp_root = Toplevel()
 
    cnvs = Canvas(temp_root, width=canvas_width, height=canvas_height)
    cnvs.grid(row=2, column=1)
 
    coord = 10, 50, 350, 350 #define the size of the gauge
    low_r =500 # chart low range
    hi_r = 950 # chart hi range
 
    # Create a background arc with a number of range lines
    numpies = 8
    for i in range(numpies):
        cnvs.create_arc(coord, start=(i*(120/numpies) +30), extent=(120/numpies), fill="white",  width=1)    
 
    # add hi/low bands
    cnvs.create_arc(coord, start=30, extent=120, outline="green", style= "arc", width=40)
    cnvs.create_arc(coord, start=30, extent=20, outline="red", style= "arc", width=40)
    cnvs.create_arc(coord, start=50, extent=20, outline="yellow", style= "arc", width=40)
    # add needle/value pointer
    id_needle = cnvs.create_arc(coord, start= 119, extent=1, width=7)
 
    # Add some labels
    cnvs.create_text(180,15,font="Times 20 italic bold", text="Temerature")
    cnvs.create_text(25,140,font="Times 12 bold", text=low_r)
    cnvs.create_text(330,140,font="Times 12 bold", text=hi_r)
    id_text = cnvs.create_text(170,210,font="Times 15 bold")
 
    temp_root.after(300, update_gauge)
 
    temp_root.mainloop()
def time_indicator():
  time_root=Toplevel()
  time_root.title("Time")
  time_root.geometry("300x300")
  photo_3=PhotoImage(file="daynnight.png")
  photo_3=photo_3.subsample(1,1)
  label_4=Label(time_root,image=photo_3)
  label_4.place(x=0,y=0)
  day_label=Label(time_root,background="white",fg="orange",bd=1,font=('Helvetica bold', 20))
  day_label.place(x=150,y=250)
  now = datetime.datetime.now()
  hour_var=now.hour
  if hour_var>=12:
    day_label.config(text="  Night  ")
  elif hour_var<12:
    day_label.config(text="   Day   ")

  time_root.mainloop()

def Ok():
    uname = e1.get()
    password = e2.get()

    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")


    elif(uname == "admin" and password == "123"):
        messagebox.showinfo("","Login Success")
        screen = Toplevel(root)
        screen.title("Main Nuclear Page")
        screen.geometry("500x500")
        photo_1=PhotoImage(file="nuclear.png")
        photo_1=photo_1.subsample(3,2)
        label_1=Label(screen,image=photo_1,bg="black",height=500,width=700)
        label_1.place(x=0,y=0)
        b1= Button(screen, text="Day",height = 3, width = 13 ,fg="red",bd='5',command=time_indicator).place(x=30, y=20)
        b2= Button(screen, text="Tempurature",height = 3, width = 13,fg="red",bd='5',command=temp_indcator).place(x=30, y=130)
        b3= Button(screen, text="Humidity",height = 3, width = 13,fg="red",bd='5',command=humidity_indcator).place(x=30, y=240)
        screen.mainloop()

    else :
        messagebox.showinfo("","Incorrent Username and Password\nTry again")


root = Tk()
root.title("Login")
root.geometry("350x350")
bg = PhotoImage( file = "nuclear-power.png")
global e1
global e2

label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)
Label(root, text="UserName" , fg="red" ).place(x=50, y=10)
Label(root, text="Password", fg="red").place(x=50, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")


Button(root, text="Login", fg="red", command=Ok , bd = '5', height = 3, width = 10).place(x=10, y=100)

root.mainloop()
