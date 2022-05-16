from tkinter import *
from memory import play
from time import sleep
import json
from levels import generate_level

highscore = 0

def play_button():
    global highscore
    prev_level = 1
    while True:
        level = generate_level(prev_level)
        level_string.set("Starting level " + str(level["level"]) + "!\n")
        root.update()
        sleep(2)
        res = play(level)
        if(res == "you lose"):
            level_string.set("You got the sequence wrong!\nClick play to try again!\n")
            return
        if(res == "too slow"):
            level_string.set("You were too slow!\nClick play to try again!\n")
            return
        if(highscore < int(level["level"])):
            highscore_string.set("Highscore: " + str(level["level"]))
            highscore = int(level["level"])
        prev_level = level
    return
    
root = Tk()
root.title('Memory game!')
root.geometry('320x480')
root.attributes("-fullscreen", True)

button_play = Button(root, text ="Play", command=play_button).pack()
label = Label(root, text = "Memorize the sequence of the lights and press\nthe buttons in the correct\norder to win!\n").pack()
quit_button = Button(root, text = "Quit", command= root.destroy).place(x=140, y= 210)

level_string = StringVar()
level_label = Label(root, textvariable = level_string).pack()

highscore_string = StringVar()
highscore_label = Label(root, textvariable = highscore_string).pack()
highscore_string.set("Highscore: 0")

root.mainloop()
