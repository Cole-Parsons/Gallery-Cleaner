from tkinter import *
from tkinter import filedialog

def openFile():
    file_path = filedialog.askdirectory()
    print(file_path)


window = Tk()
button = Button(text='Open', command=openFile)
button.pack()
window.mainloop()