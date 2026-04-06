from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from pathlib import Path
import shutil

selected_folder = None
images_files = []
current_image_index = 0

def get_file_path():
    selected_folder_string = filedialog.askdirectory()
    print('Selected folder: ', selected_folder)
    if selected_folder_string:
        global selected_folder_path 
        selected_folder_path = Path(selected_folder_string)
        create_trash_folder()
        parse_images_folder()

def parse_images_folder():
    image_files = [f for f in selected_folder_path.iterdir() if f.suffix.lower() in [".png", ".jpg", ".jpeg", "heic", "heif"]]
    print(f"Found {len(image_files)} images")
    return images_files

def view_images(images):
    for i in range(len(images)):
        image_path = images[i]
        image = Image.open(image_path)
        image.show()

        input = ('Enter y to continue:')
        if input.lower() == 'y':
            continue

def show_next_image(images):
    global current_index
    if current_image_index < len(images):
        image_path = images[current_image_index]
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img
        current_image_index += 1

def show_previous_image(images):
    global current_index
    if current_image_index != 0:
        image_path = images[current_image_index]
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img
        current_image_index -= 1


def create_trash_folder():
    global trash_folder_name
    global trash_folder_path
    trash_folder_name = 'trash_folder'
    trash_folder_path = Path(trash_folder_name)
    
    try:
        Path(trash_folder_name).mkdir(exist_ok=True)
    except FileExistsError:
        print(f'{trash_folder_name} already exists')
    except PermissionError:
        print('You do not have permission to create folder')
    except OSError as e:
        print(f'Error has occured {e}')
    

def delete_trash_images_folder():
    if not any(trash_folder_path.iterdir()):
        print('Folder is empty')
        return
    try:
        choice = input('Are you sure you want to delete ? y/n:')
        if choice.lower == 'y':
            shutil.rmtree(trash_folder_name)
        else:
            print('TODO: go back to the main window')
    except FileExistsError:
        print('gallery_cleaner_trash_images folder does not exist')
    except PermissionError:
        print('You do not have permission to remove folder')
    except OSError as e:
        print(f'Error has occured {e}')

#add displaying image to window


# GUI
window = Tk()
get_user_images_folder_button = Button(text='Select Folder', command=get_file_path)
get_user_images_folder_button.pack()

delete_trash_images_button = Button(text='Delete Trash Images', command=delete_trash_images_folder)
delete_trash_images_button.pack()

img_label = Label(window)
img_label.pack()

next_button = Button(window, text='Next Image', command=show_next_image(images_files))
next_button.pack()

previous_button = Button(window, text='Previous Image', command=show_previous_image(images_files))
previous_button.pack()

window.mainloop()