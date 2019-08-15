from tkinter import *
import tkinter.messagebox

if __name__ == '__main__':
    root = Tk()

    def callback():
        tkinter.messagebox.showinfo("Title", "Message")

    btn = Button(root, padx=20, pady=20, text="Click", command=callback)
    btn.pack()

    root.mainloop()
