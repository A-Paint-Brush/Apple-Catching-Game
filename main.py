import tkinter
import Game


def start():
    window.destroy()
    Game.Main()


window = tkinter.Tk()
window.title("Instructions")
window.geometry("400x400")
window.maxsize(400, 400)
window.minsize(400, 400)
label = tkinter.Label(window, text="Instructions:\nOnce the game starts, you will see apples falling from the "
                                   "sky\nand a basket at the bottom of the screen. Use the left and right\narrow keys "
                                   "to control the basket and catch the apples! There is\na time limit of one minute. "
                                   "Catch as many apples as you can\nbefore you run out of time!")
label.pack()
btn = tkinter.Button(window, text="Start Game", command=start)
btn.pack()
window.mainloop()
