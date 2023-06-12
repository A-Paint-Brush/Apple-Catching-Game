import tkinter
import Game
import Data


class Results:
    def __init__(self, score):
        self.window = tkinter.Tk()
        self.window.title("Results")
        self.window.geometry("400x400")
        self.window.maxsize(400, 400)
        self.window.minsize(400, 400)
        if score == 0:
            self.label = tkinter.Label(self.window, text="You did not catch any apples in one minute.")
        elif score == 1:
            self.label = tkinter.Label(self.window, text="You caught 1 apple in one minute.")
        else:
            self.label = tkinter.Label(self.window, text="You caught " + str(score) + " apples in one minute.")
        self.label.pack()
        self.btn = tkinter.Button(self.window, text="Restart", command=self.restart)
        self.btn.pack()
        self.window.mainloop()

    def restart(self):
        Data.score = 0
        self.window.destroy()
        Game.Main()
