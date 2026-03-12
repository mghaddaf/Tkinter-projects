import tkinter
screen = tkinter.Tk()
screen.geometry("500x500")
screen.title("System Login")
def login_button():
    loginn = entry1.get()
    passwordd = entry2.get()
    if loginn == "Ryan" and passwordd == "Ryan":
        print("Login Successful! Redirecting...")
    else:
        print("Incorrect. Please check your username or password")
def cancel_button():
    screen.destroy()
label1 = tkinter.Label(screen, text = "Username:")
label2 = tkinter.Label(screen, text = "Password:")
label1.grid(row = 1, column = 1)
label2.grid(row = 2, column = 1)
entry1 = tkinter.Entry(screen)
entry1.grid(row = 1, column = 2)
entry2 = tkinter.Entry(screen, show = "*")
entry2.grid(row = 2, column = 2)
login = tkinter.Button(screen, bg = "Green", text = "Login", command = login_button)
login.grid(row = 3, column = 1)
cancel = tkinter.Button(screen, bg = "Red", text = "Cancel", command = cancel_button)
cancel.grid(row = 3, column = 2)
screen.mainloop()