from tkinter import *


def button_clicked():
    print('Button clicked')


if __name__ == '__main__':
    root = Tk()
    button = Button(root, text='Click Me', command=button_clicked)
    button.pack(pady=50, padx=50)
    root.mainloop()
