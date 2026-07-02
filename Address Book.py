import tkinter, tkinter.filedialog
screen = tkinter.Tk()
screen.geometry("500x500")
screen.title("Adress book")
data = {}
def OpenButton():
    global data
    File1 = tkinter.filedialog.askopenfile()
    if File1 != None:
        data = eval(File1.readline())
        UpdateListBox()
def AddButton():
    Name = Entry1.get()
    Address = Entry2.get()
    Mobile = Entry3.get()
    Email = Entry4.get()
    Birthday = Entry5.get()
    data[Name] = [Address, Mobile, Email, Birthday]
    UpdateListBox()
    Entry1.delete(0, tkinter.END)
    Entry2.delete(0, tkinter.END)
    Entry3.delete(0, tkinter.END)
    Entry4.delete(0, tkinter.END)
    Entry5.delete(0, tkinter.END)

def UpdateListBox():
        Listbox1.delete(0, tkinter.END)
        for name in data.keys():
            Listbox1.insert(tkinter.END, name)

def DeleteButton():
    item = Listbox1.curselection()
    Listbox1.delete(item)
def SaveButton():
    File1 = tkinter.filedialog.asksaveasfile()
    if File1 != None:
        print(data, file = File1)

Label1 = tkinter.Label(screen, text = "My address book")
Label2 = tkinter.Label(screen, text = "Name:")
Label3 = tkinter.Label(screen, text = "Address:")
Label4 = tkinter.Label(screen, text = "Mobile:")
Label5 = tkinter.Label(screen, text = "Email:")
Label6 = tkinter.Label(screen, text = "Birthday:")
Button1 = tkinter.Button(screen, text = "Open", command = OpenButton)
Button2 = tkinter.Button(screen, text ="Edit")
Button3 = tkinter.Button(screen, text = "Delete", command = DeleteButton)
Button4 = tkinter.Button(screen, text = "Save", command = SaveButton)
Button5 = tkinter.Button(screen, text = "Update / Add", command = AddButton)
Entry1 = tkinter.Entry(screen)
Entry2 = tkinter.Entry(screen)
Entry3 = tkinter.Entry(screen)
Entry4 = tkinter.Entry(screen)
Entry5 = tkinter.Entry(screen)
Listbox1 = tkinter.Listbox(screen)
Label1.grid(row = 2, column = 2)
Label2.grid(row = 2, column = 3)
Label3.grid(row = 3, column = 3)
Label4.grid(row = 4, column = 3)
Label5.grid(row = 5, column = 3)
Label6.grid(row = 6, column = 3)
Button1.grid(row = 1, column = 3)
Button2.grid(row = 7, column = 1)
Button3.grid(row = 7, column = 2)
Button4.grid(row = 8, column = 2)
Button5.grid(row = 7, column = 4)
Entry1.grid(row = 2, column = 4)
Entry2.grid(row = 3, column = 4)
Entry3.grid(row = 4, column = 4)
Entry4.grid(row = 5, column = 4)
Entry5.grid(row = 6, column = 4)
Listbox1.grid(row = 2, column = 1, columnspan = 2, rowspan = 5)

screen.mainloop()