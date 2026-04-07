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
    print('Selected folder: ', selected_folder_string)
    if selected_folder_string:
        global selected_folder_path 
        selected_folder_path = Path(selected_folder_string)
        create_trash_folder()
        parse_images_folder()

def parse_images_folder():
    global images_files
    images_files = [f for f in selected_folder_path.iterdir() if f.suffix.lower() in [".png", ".jpg", ".jpeg", "heic", "heif"]]
    print(f"Found {len(images_files)} images")

    if images_files:
        display_image(current_image_index)

def display_image(index):
    image_path = images_files[index]
    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

def show_next_image(images):
    global current_image_index
    if current_image_index < len(images) - 1:
        current_image_index += 1
        display_image(current_image_index)

def show_previous_image(images):
    global current_image_index
    if current_image_index > 0:
        current_image_index -= 1
        display_image(current_image_index)

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
    

def empty_trash_images_folder():
    if not any(trash_folder_path.iterdir()):
        text_box.insert(END, 'Trash folder has nothing in it')
        window.after(2000, lambda: clear_text_box())
        return
    try:
        for item in trash_folder_path.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
        text_box.insert(END, 'Trash folder has been emptied')
        window.after(2000, lambda: clear_text_box())
    except  Exception as e:
        print (f"could not delete {item}: {e}")
        text_box.insert(END, 'Error')
        window.after(2000, lambda: clear_text_box())

def move_image_to_trash(images, index):
    global current_image_index
    destination = trash_folder_path / images[index].name
    shutil.move(images[index], destination)

    images.pop(index)

    if current_image_index >= len(images):
        current_image_index = len(images) - 1
    
    if images:
        display_image(current_image_index)
    else:
        img_label.config(image=' ')
        img_label.image = None
        text_box.insert(END, 'No More Images')
        window.after(2000, lambda: clear_text_box())

def clear_text_box():
    text_box.delete('1.0', END)

#add displaying image to window

# GUI
window = Tk()
window.title('Gallery Cleaner')

get_user_images_folder_button = Button(text='Select Folder', command=get_file_path)
get_user_images_folder_button.grid(row=0, column=1, padx=5, pady=5)

empty_trash_images_button = Button(text='Delete Trash Images', command=empty_trash_images_folder)
empty_trash_images_button.grid(row=5, column=1, padx=5, pady=5)

img_label = Label(window)
img_label.grid(row=1, column=1, padx=5, pady=5)

next_button = Button(window, text='Next Image', command=lambda: show_next_image(images_files))
next_button.grid(row=3, column=1, padx=5, pady=5)

previous_button = Button(window, text='Previous Image', command=lambda: show_previous_image(images_files))
previous_button.grid(row=3, column=0, padx=5, pady=5)

delete_image_button = Button(window, text='Delete Image', command=lambda: move_image_to_trash(images_files, current_image_index))
delete_image_button.grid(row=3, column=2, padx=5, pady=5)

text_box = Text(window, height=2, width=50)
text_box.grid(row=2, column=1, padx=5, pady=5)

window.mainloop()