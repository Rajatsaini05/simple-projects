from pytube import YouTube
from tkinter import *

down=Tk()
down.geometry("500x500")
link=input("Enter the link of youtube : ")
youtube=YouTube(link)

print(youtube.title)
print(youtube.thumbnail_url)
vid=youtube.streams.all()
vid_list=list(enumerate(vid))
for i in vid_list:
    print(i)
print()
strn=int(input("enter: "))
vid[strn].download()
print("sucessfully")
