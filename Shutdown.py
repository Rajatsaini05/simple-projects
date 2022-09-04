from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l ")
#def exit():
 #   os._exit()
    

st = Tk()
st.title("*Shut Down")
st.geometry("500x500")
st.config(bg="black")

r_button=Button(st,text="RESTART",font=("Time New Roman", 10,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=190,y=150,height=40,width=100)

re_button=Button(st,text="REBOOT",font=("Time New Roman", 10,"bold"),relief=RAISED,cursor="plus",command=restart_time)
re_button.place(x=190,y=210,height=40,width=100)

lg_button=Button(st,text="LOG-OFF",font=("Time New Roman", 10,"bold"),relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=190,y=270,height=40,width=100)

ex_button=Button(st,text="EXIT",font=("Time New Roman", 10,"bold"),relief=RAISED,cursor="plus",command=exit)
ex_button.place(x=190,y=350,height=40,width=100)















st.mainloop()
