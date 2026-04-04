from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from pathlib import Path

selected_folder = None

def get_file_path():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    print('Selected folder: ', selected_folder)
    if selected_folder:
        parse_images_folder()

def parse_images_folder():
    image_files = [f for f in selected_folder.iterdir() if f.suffix.lower() in [".png", ".jpg", ".jpeg", "heic", "heif"]]
    print(f"Found {len(image_files)} images")

#add displaying image to window


# GUI
window = Tk()
button = Button(text='Open', command=get_file_path)
button.pack()

image = Image.open('C:/Users/cgpar/Desktop/pictures/download.jpg')
image = ImageTk.PhotoImage(image)

my_label = Label(window, image=image)
my_label.pack(pady=20)

window.mainloop()