from tkinter import *
import youtube_dl
from tkinter import messagebox

scrap = Tk()
scrap.title("Youtube scrap")
scrap.configure(bg="#333333")
scrap.geometry("750x325")

label = Label(scrap, text='Youtube Video Downloader',bg = "#333333",fg="#B22222", font=("Times New Roman",30))
label.grid(row=0,column=1, padx=10, pady=20, ipady=10)

label1 = Label(scrap,text="Youtube link  :",bg = "#333333",fg = "#B22222",font=("Calibri",25))
label1.grid(row=1,column=0,pady=5,padx=5)

link = StringVar()
inp = Entry(scrap,textvariable=link, width=30,borderwidth=2,font=("Calibri",15))
inp.grid(row=1,column=1,padx=10,pady=20,ipady=10)


def download():
    Videolink = link.get()
    if (Videolink != ""):
        y= {}   
        video=youtube_dl.YoutubeDL(y)
        video.download([Videolink])
        Label(scrap, text = 'DOWNLOADED',bg = "#333333",fg="#B22222",padx=45,pady=15, font = ("Times New Roman",15)).grid(row=5,column=1)
    else:
        Label(scrap, text = 'N0 LINK FOUND',bg = "#333333",fg="#B22222",padx=45,pady=15, font = ("Times New Roman",15)).grid(row=5,column=1)

        
Download = Button(scrap, text = 'Download', font=("Times New Roman",15),padx=45,pady=15,bg='black',fg='#B22222', command= download)
Download.grid(row=4,column=1)



scrap.mainloop()
