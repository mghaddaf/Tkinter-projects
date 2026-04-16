import tkinter, random
screen = tkinter.Tk()
screen.geometry("500x150")
screen.title("Rock Paper Scissors")
playerscore = 0
computerscore = 0
options = ["rock", "paper", "scissors"]
def RPS(Player_Selected):
    global playerscore, computerscore
    compselect = random.choice(options)
    Label5.config(text = "You selected: " + Player_Selected)
    Label6.config(text = "Computer Selected: " + compselect)
    if Player_Selected == compselect:
        Label2.config(text = "Draw!")
    if Player_Selected == "paper" and compselect == "rock" or Player_Selected == "scissors" and compselect == "paper" or Player_Selected == "rock" and compselect == "scissors":
        Label2.config(text = "You Win!")
        playerscore = playerscore + 1
        Label7.config(text = "Your Score: " + str(playerscore))
        Label8.config(text = "Computer Score: " + str(computerscore))
    if compselect == "rock" and Player_Selected == "scissors" or compselect == "paper" and Player_Selected == "rock" or compselect == "scissors" and Player_Selected == "paper":
        Label2.config(text = "Computer Wins!")
        computerscore = computerscore + 1
        Label7.config(text = "Your Score: " + str(playerscore))
        Label8.config(text = "Computer Score: " + str(computerscore))
                      
Label1 = tkinter.Label(screen, text = "Rock Paper Scissors")
Label2 = tkinter.Label(screen, text = "")
Label3 = tkinter.Label(screen, text = "Your Options:")
Label4 = tkinter.Label(screen, text = "Score:")
Label5 = tkinter.Label(screen, text = "You selected:  ")
Label6 = tkinter.Label(screen, text = "Computer selected:  ")
Label7 = tkinter.Label(screen, text = "Your Score:  ")
Label8 = tkinter.Label(screen, text = "Computer Score:  ")
Button1 = tkinter.Button(screen, text = "Rock", command = lambda:RPS("rock"))
Button2 = tkinter.Button(screen, text = "Paper", command = lambda:RPS("paper"))
Button3 = tkinter.Button(screen, text = "Scissors", command = lambda:RPS("scissors"))
Label1.grid(row = 1, column = 1, columnspan=4)
Label2.grid(row = 2, column = 1, columnspan=4)
Label3.grid(row = 3, column = 1)
Label4.grid(row = 4, column = 1)
Label5.grid(row = 4, column = 2)
Label6.grid(row = 5, column = 2)
Label7.grid(row = 4, column = 4)
Label8.grid(row = 5, column = 4)
Button1.grid(row = 3, column = 2)
Button2.grid(row = 3, column = 3)
Button3.grid(row = 3, column = 4)
screen.mainloop()