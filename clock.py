from tkinter import *
import datetime

 
def time_date():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    mi=time.strftime('%M')
    se=time.strftime('%S')
    am=time.strftime('%p')
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=se)
    
    lab_day.config(text=am)
    lab_hr.after(200,time_date)
    #lab.mi.after(200,

clock=Tk()
clock.title('   *****DIGITAL CLOCK*****')
clock.geometry('800x500')
clock.config(bg='black')

lab_hr=Label(clock,text="00",font=('Time New Romen',60,"bold"),
             bg='green',fg='black')
lab_hr.place(x=40,y=45,height=110,width=100)
lab_hr_txt=Label(clock,text="HOUR",font=('Time New Romen',20,"bold"),
             bg='green',fg='black')
lab_hr_txt.place(x=40,y=185,height=30,width=100)

lab_min=Label(clock,text="00",font=('Time New Romen',60,"bold"),
             bg='green',fg='black')
lab_min.place(x=180,y=45,height=110,width=100)
lab_min_txt=Label(clock,text="MIN",font=('Time New Romen',20,"bold"),
             bg='green',fg='black')
lab_min_txt.place(x=180,y=185,height=30,width=100)
lab_sec=Label(clock,text="00",font=('Time New Romen',60,"bold"),
             bg='green',fg='black')
lab_sec.place(x=340,y=45,height=110,width=100)

lab_sec_txt=Label(clock,text="SEC",font=('Time New Romen',20,"bold"),
             bg='green',fg='black')
lab_sec_txt.place(x=340,y=185,height=30,width=100)
lab_day=Label(clock,text="00",font=('Time New Romen',40,"bold"),
             bg='green',fg='black')
lab_day.place(x=560,y=45,height=110,width=100)

lab_day_txt=Label(clock,text="AM/PM",font=('Time New Romen',15,"bold"),
             bg='green',fg='black')
lab_day_txt.place(x=560,y=185,height=20,width=100)

time_date()
clock.mainloop()








