from tkinter import *
import speedtest

sp =Tk()
sp.title("***Internet speed***")
sp.geometry("800x800")
sp.config(bg="black")

def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6)),3)+"Mbps"
    up=str(round(sp.upload()/(10**6)),3)+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)
    
    
lab=Label(sp,text="Internet speed Test",font=("TIme New Roman",10,"bold"))
lab.place(x=175,y=130,height=50,width=380)

lab=Label(sp,text="Download speed",font=("TIme New Roman",10,"bold"))
lab.place(x=175,y=230,height=50,width=380)

lab_down=Label(sp,text="00",font=("TIme New Roman",10,"bold"))
lab_down.place(x=175,y=290,height=50,width=380)

lab=Label(sp,text="Upload Speed",font=("TIme New Roman",10,"bold"))
lab.place(x=175,y=350,height=50,width=380)

lab_up=Label(sp,text="00",font=("TIme New Roman",10,"bold"))
lab_up.place(x=175,y=410,height=50,width=380)

button=Button(sp,text="Check Speed",font=("Time New Roman",10,"bold"),relief=RAISED,bg="blue",command=speedcheck)
button.place(x=175,y=520,height=50,width=380)


























sp.mainloop()
