from tkinter import *

if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, bg="#ffa827", height=512, width=512)
    coordinates = 50, 100, 150, 200

    arc = canvas.create_arc(coordinates, start=0, extent=45, fill="#8d1832")
    canvas.pack()

    root.mainloop()
