# Gallery Cleaner App
Have you ever had the annoying pop up on your phone "Storage Full, Free Space", but the only thing taking up storage on your phone is thousands of pictures?  
Personally I think it takes way too long to press the trash can and press delete for each photo. Not to mention how long it takes for the UI to load between each step.  
Of course there's batch delete but then you have no idea what the pictures are you're actually deleting.   
I've seen apps online for photo cleaning but but who knows what they are doing with your photos and where they're going!  

The goal of this app is to be quick, transparent, and easy to use.

## How to Run:
1. clone the repository `git clone https://github.com/Cole-Parsons/Gallery-Cleaner.git`
2. cd into the folder `cd Gallery-Cleaner`
3. Run the program `python main.py`
4. Choose `Select Folder`, and open the folder where your images are stored.
5. Use key binds or buttons to parse and delete your images.

## Binds and Buttons
Select Folder - No Bind = Allows you to choose the folder with you images in it
Delete Trash Images - No Bind = *permanently deletes* all of the images that have been selected to delete
Previous Image - Left Arrow = Go to previous image
Next Image - Right Arrow = Go to next image
Delete Image - Delete/Backspace = Move current Image to the Apps trash folder
Undo Last Delete - Enter/Return = Undo last image deletion

## Tips of Usage:
* If you clicked delete on an image and for some reason can not get it back using the undo function, close the app and access the apps `trash_folder`
