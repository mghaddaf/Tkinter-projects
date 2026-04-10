import tkinter
screen = tkinter.Tk()
screen.geometry("300x300")
screen.title("Mass Converter")
def calculator():
    kg = float(Entry1.get())
    g = kg * 1000
    pounds = kg * 2.20462
    ounces = kg * 35.274
    Label5.config(text = g)
    Label6.config(text = pounds)
    Label7.config(text = ounces)
Label1 = tkinter.Label(screen, text = "Enter the weight in KG")
Label2 = tkinter.Label(screen, text = "Grams")
Label3 = tkinter.Label(screen, text = "Pounds")
Label4 = tkinter.Label(screen, text = "Ounces")
Label5 = tkinter.Label(screen, text = "")
Label6 = tkinter.Label(screen, text = "")
Label7 = tkinter.Label(screen, text = "")
Entry1 = tkinter.Entry(screen)
Button1 = tkinter.Button(screen, text = "Convert", command = calculator)
Label1.grid(row = 1, column = 1)
Label2.grid(row = 2, column = 1)
Label3.grid(row = 2, column = 2)
Label4.grid(row = 2, column = 3)
Label5.grid(row = 3, column = 1)
Label6.grid(row = 3, column = 2)
Label7.grid(row = 3, column = 3)
Entry1.grid(row = 1, column = 2)
Button1.grid(row = 1, column = 3)

screen.mainloop()