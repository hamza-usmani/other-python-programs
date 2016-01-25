import Tkinter
from Tkinter import *
from Tkinter import Menu
from ScrolledText import *
import tkFileDialog
import tkMessageBox
 
root = Tkinter.Tk(className="SimpleText")

root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())

textPad = ScrolledText(root, width=80, height=100, )

# menu
 
def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Open file')
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()
 
def save_command():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        data = textPad.get
        file.write(data)
        file.close()
         
def exit_command():
    if tkMessageBox.askokcancel("Quit", "Quit?"):
        root.destroy()
 
def about_command():
    label = tkMessageBox.showinfo("About", "SimpleText Editor\nHamza Usmani \n2016")
         
 
def dummy():
    print "delete"

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about_command)

textPad.pack()
root.mainloop()





