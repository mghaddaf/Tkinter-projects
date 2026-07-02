import tkinter, time, tkinter.messagebox
screen = tkinter.Tk()
screen.geometry("500x500")
screen.title("Countdown stopwatch")

hours = tkinter.StringVar()
minutes = tkinter.StringVar()
seconds = tkinter.StringVar()
hours.set("00")
minutes.set("00")
seconds.set("00")
def timer():
    userhours = int(Entry1.get())
    userminutes = int(Entry2.get())
    userseconds = int(Entry3.get())
    while userseconds > 0:
        userseconds = userseconds - 1
        if userseconds == 0 and userminutes > 0:
            userminutes = userminutes - 1
            userseconds = 60
        if userminutes == 0 and userhours > 0:
            userhours = userhours - 1
            userminutes = 59
            userseconds = 60
        hours.set(userhours)
        minutes.set(userminutes)
        seconds.set(userseconds)
        time.sleep(1)
        screen.update()
        if userhours == 0 and userminutes == 0 and userseconds == 0:
            tkinter.messagebox.showinfo("TIME IS UP", "TIME IS UP")

Entry1 = tkinter.Entry(screen, textvariable = hours)
Entry2 = tkinter.Entry(screen, textvariable = minutes)
Entry3 = tkinter.Entry(screen, textvariable = seconds)
Button1 = tkinter.Button(screen, text = "Set time countdown", command = timer)
Entry1.grid(row = 1, column = 1)
Entry2.grid(row = 1, column = 2)
Entry3.grid(row = 1, column = 3)
Button1.grid(row = 3, column = 2)

screen.mainloop()