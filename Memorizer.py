import tkinter, tkinter.filedialog
screen = tkinter.Tk()
screen.geometry("300x500")
screen.title("Memorizer")

def OpenButton():
    File1 = tkinter.filedialog.askopenfile()
    if File1 != None:
        Items = File1.readlines()
        for item in Items:
            Listbox1.insert(tkinter.END, item)
def AddButton():
    data = Entry1.get()
    Listbox1.insert(tkinter.END, data)
    Entry1.delete(0, tkinter.END)
def DeleteButton():
    item = Listbox1.curselection()
    Listbox1.delete(item)
def SaveButton():
    File1 = tkinter.filedialog.asksaveasfile()
    if File1 != None:
        for item in Listbox1.get(0, tkinter.END):
            print(item, file = File1)
Listbox1 = tkinter.Listbox(screen)
Button1 = tkinter.Button(screen, text = "Save", command = SaveButton)
Button2 = tkinter.Button(screen, text= "Delete", command = DeleteButton)
Button3 = tkinter.Button(screen, text = "Add", command = AddButton)
Button4 = tkinter.Button(screen, text = "Open", command = OpenButton)
Entry1 = tkinter.Entry(screen)
Button1.grid(row = 1, column = 1)
Button2.grid(row = 1, column = 2)
Button3.grid(row = 1, column = 3)
Button4.grid(row = 2, column = 3)
Entry1.grid(row = 2, column = 1, columnspan = 2)
Listbox1.grid(row = 3, column = 1, columnspan = 3)
screen.mainloop()