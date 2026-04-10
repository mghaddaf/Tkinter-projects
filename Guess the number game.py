import tkinter, tkinter.messagebox, random
screen = tkinter.Tk()
screen.geometry("500x500")
screen.title("Guess the number game")
number = random.randint(1, 20)
def submit():
    tkinter.messagebox.showinfo("" ,"Well, " + entry1.get() + ", I am thinking of a number between 1 and 20")
def result():
    guess = entry2.get()
    guess = int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("" ,"Lower")
    elif guess < number:
        tkinter.messagebox.showinfo("" ,"Higher")
    elif guess == number:
        tkinter.messagebox.showinfo("" ,"You got it!")

label1 = tkinter.Label(screen, text = "Welcome to our game!")
label2 = tkinter.Label(screen, text = "What's your name?")
label3 = tkinter.Label(screen, text = "Take a guess:")
entry1 = tkinter.Entry(screen)
entry2 = tkinter.Entry(screen)
button1 = tkinter.Button(screen, text = "Ok", command = submit)
button2 = tkinter.Button(screen, text = "Guess", command = result)
label1.grid(row = 1, column = 2)
label2.grid(row = 2, column = 1)
label3.grid(row = 4, column = 1)
entry1.grid(row = 2, column = 2)
entry2.grid(row = 4, column = 2)
button1.grid(row = 2, column = 3)
button2.grid(row = 3, column = 3)

screen.mainloop()