import os
from tkinter import *
from PIL import ImageTk, Image

def forward(img_no):
    global label, button_forward, button_back

    label.grid_forget()
    label = Label(image=image_list[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)

    button_forward.config(command=lambda: forward(img_no + 1))
    button_back.config(command=lambda: back(img_no - 1))

    if img_no == len(image_list):
        button_forward.config(state=DISABLED)

    if img_no == 1:
        button_back.config(state=DISABLED)

def back(img_no):
    global label, button_forward, button_back

    label.grid_forget()
    label = Label(image=image_list[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)

    button_forward.config(command=lambda: forward(img_no + 1))
    button_back.config(command=lambda: back(img_no - 1))

    if img_no == 1:
        button_back.config(state=DISABLED)

    if img_no == len(image_list):
        button_forward.config(state=DISABLED)

root = Tk()
root.title("Image Viewer")

image_folder = "images"
image_files = [file for file in os.listdir(image_folder) if file.endswith((".jpg", ".png", ".jpeg"))]


image_list = []
for file in image_files:
    image_path = os.path.join(image_folder, file)
    image = ImageTk.PhotoImage(Image.open(image_path))
    image_list.append(image)

label = Label(image=image_list[0])
label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="Back", command=lambda: back(1), state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text="Forward", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
