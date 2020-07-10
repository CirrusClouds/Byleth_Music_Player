import pygame
import tkinter as tkr
import os


# Create window
player = tkr.Tk()


# Edit window
player.title("Audio Player")
player.geometry("205x340")
color = '#76EEC6'
bgImage = tkr.PhotoImage(file='/home/jamie/Pictures/emotes/bylethflushed.png')


# Playlist register
os.chdir("/home/jamie/Music")
songlist = os.listdir()

# Playlist input
playlist = tkr.Listbox(player, highlightcolor=color, selectmode=tkr.SINGLE)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

# Initialise pygame
pygame.init()
pygame.mixer.init()


# Commands


def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

   
def ExitPlayer():
    pygame.mixer.music.stop()


def Pause():
    pygame.mixer.music.pause()

   
def UnPause():
    pygame.mixer.music.unpause()

   
# Register Buttons
Button1 = tkr.Button(player, width=5, height=3, text="O", command=Play)
Button2 = tkr.Button(player, width=5, height=3, text="X", command=ExitPlayer)
Button3 = tkr.Button(player, width=5, height=3, text="| |", command=Pause)
Button4 = tkr.Button(player, width=5, height=3, text="| >", command=UnPause)


# Song Name
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)

# Label for cute image
palugiggle = tkr.Label(player, image=bgImage, width=100, height=120)


# Place widgets
palugiggle.pack(fill="both", ipady=10)
songtitle.pack()
playlist.pack(fill="both", expand=1)
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")


# Activate
player.mainloop()
