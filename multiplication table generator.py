import tkinter, tkinter.ttk

screen = tkinter.Tk()
screen.geometry("350x700")
screen.title("Multiplication table")
def GenerateTable():
    number = int(Combobox1.get())
    equation = ""
    for i in range(x_rate.get() + 1):
        equation += str(number) + "X" + str(i) + "=" + str(number * i) + "\n"
        i = i + 1
    Label3.config(text = equation)
Label1 = tkinter.Label(screen, text = "Mathematical Table")
Label2 = tkinter.Label(screen, text = "Number and Range: ")
Label3 = tkinter.Label(screen, text = "")
Button1 = tkinter.Button(screen, text = "Generate", command = GenerateTable)
Combobox1 = tkinter.ttk.Combobox(screen)
Numbers = []
for i in range(101):
    Numbers.append(i)
Combobox1["values"] = Numbers

x_rate = tkinter.IntVar()
Radiobutton1 = tkinter.ttk.Radiobutton(screen, text = "10", variable=x_rate, value=10)
Radiobutton2 = tkinter.ttk.Radiobutton(screen, text = "20", variable=x_rate, value=20)
Radiobutton3 = tkinter.ttk.Radiobutton(screen, text = "30", variable=x_rate, value=30)
Label1.grid(row = 1, column = 2)
Label2.grid(row = 2, column = 1)
Label3.grid(row = 3, column = 2)
Button1.grid(row = 5, column = 2)
Combobox1.grid(row = 2, column = 2)
Radiobutton1.grid(row = 2, column = 3)
Radiobutton2.grid(row = 3,column = 3)
Radiobutton3.grid(row = 4, column = 3)












screen.mainloop()