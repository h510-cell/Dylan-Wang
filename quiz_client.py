import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import os
import time
from playsound import playsound
import pygame
from pygame import mixer


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
filePathLabel  = None
song_selected = None

global song_counter
song_counter = 0

for file in os.listdir('shared files'):
    filename = os.fsdecode(file)
    listbox.insert(song_counter,filename)
    song_counter = song_counter + 1

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text = "Now Playing:" +song_selected)
    else:
        infoLabel.configure(text = "")

def stop():
    global song_selected

    pygame
    mixer.init()
    mixer.music.load('shared files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text = "")


def musicWindow():

    print("\n\t\t\t\tMucis Sharing")

   
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg="LightSkyBlue")

    global listbox
    

    selectLabel = Label(window, text= "Select Song",bg="LightSkyBlue", font = ("Calibri",10))
    selectLabel.place(x=10, y=8)


    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    PlayButton=Button(window,text="Play",width =10,bd=1,bg = "skyBlue" ,font = ("Calibri",10))
    PlayButton.place(x=30,y=200)

    Stop=Button(window,text="Stop",width =10,bd=1,bg = "skyBlue" ,font = ("Calibri",10))
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Upload",width =10,bd=1,bg = "skyBlue" ,font = ("Calibri",10))
    Upload.place(x=30,y=250)

    Download=Button(window,text="Download",width =10,bd=1,bg = "skyBlue" ,font = ("Calibri",10))
    Download.place(x=200,y=250)

    infoLabel = Label(window, text= "",fg= "blue", font = ("Calibri",8))
    infoLabel.place(x=4, y=200)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()