from tkinter import *

if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, height=512, width=512)
    img = PhotoImage(file="dog_small.png")
    canvas.create_image(256, 256, image=img)
    canvas.pack()

    root.mainloop()
