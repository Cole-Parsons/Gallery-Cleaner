from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

def get_File_Path():
    file_path = filedialog.askdirectory()
    print(file_path)


window = Tk()
button = Button(text='Open', command=get_File_Path)
button.pack()

image = Image.open('C:/Users/cgpar/Desktop/pictures/download.jpg')
image = ImageTk.PhotoImage(image)

my_label = Label(window, image=image)
my_label.pack(pady=20)



window.mainloop()