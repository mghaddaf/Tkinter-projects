import tkinter, random, tkinter.messagebox
screen = tkinter.Tk()
screen.geometry("3000x3000")
screen.title("Man vs Machine")
SelectButton = []
def Player_selected(ButtonSelected):
    if ButtonSelected in options:
        ButtonSelected.config(text = "O")
        SelectButton.append(ButtonSelected)
        options.remove(ButtonSelected)
        winner()
        compselect = random.choice(options)
        compselect.config(text = "X")
        options.remove(compselect)
        winner()

def winner():
    for win in wins:
        if win[0]["text"] == "O" and win[1]["text"] == "O" and win[2]["text"] == "O":
            tkinter.messagebox.showinfo("WINNER", "PLAYER (YOU)!")
        if win[0]["text"] == "X" and win[1]["text"] == "X" and win[2]["text"] == "X":
            tkinter.messagebox.showinfo("WINNER", "COMPUTER!")
Button1 = tkinter.Button(screen, font = ("Arial", 20), bg = "white", width = 20, height = 10, text = "", command = lambda:Player_selected(Button1))
Button2 = tkinter.Button(screen, font = ("Arial", 20), bg = "white", width = 20, height = 10, text = "", command = lambda:Player_selected(Button2))
Button3 = tkinter.Button(screen, font = ("Arial", 20), bg = "white", width = 20, height = 10, text = "", command = lambda:Player_selected(Button3))
Button4 = tkinter.Button(screen, font = ("Arial", 20), bg = "white", width = 20, height = 10, text = "", command = lambda:Player_selected(Button4))
Button5 = tkinter.Button(screen, font = ("Arial", 20), bg = "white", width = 20, height = 10, text = "", command = lambda:Player_selected(Button5))
Button6 = tkinter.Button(screen, font = ("Arial", 20), bg = "white", width = 20, height = 10, text = "", command = lambda:Player_selected(Button6))
Button7 = tkinter.Button(screen, font = ("Arial", 20), bg = "white", width = 20, height = 10, text = "", command = lambda:Player_selected(Button7))
Button8 = tkinter.Button(screen, font = ("Arial", 20), bg = "white", width = 20, height = 10, text = "", command = lambda:Player_selected(Button8))
Button9 = tkinter.Button(screen, font = ("Arial", 20), bg = "white", width = 20, height = 10, text = "", command = lambda:Player_selected(Button9))
Button1.grid(row = 1, column = 1)
Button2.grid(row = 1, column = 2)
Button3.grid(row = 1, column = 3)
Button4.grid(row = 2, column = 1)
Button5.grid(row = 2, column = 2)
Button6.grid(row = 2, column = 3)
Button7.grid(row = 3, column = 1)
Button8.grid(row = 3, column = 2)
Button9.grid(row = 3, column = 3)
options = [Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9]
wins = [(Button1, Button2, Button3), (Button4, Button5, Button6), (Button7, Button8, Button9), (Button1, Button4, Button7), (Button2, Button5, Button8), (Button3, Button6, Button9), (Button1, Button5, Button9), (Button7, Button5, Button3)]
screen.mainloop()