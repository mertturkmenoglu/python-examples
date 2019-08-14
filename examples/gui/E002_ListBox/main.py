from tkinter import *

if __name__ == '__main__':
    root = Tk()

    names = ['Emily', 'Diana', 'Barbara', 'Selina', 'Ada']
    lb = Listbox(root)

    for i, name in enumerate(names):
        lb.insert(i, name)

    lb.pack()

    root.mainloop()
