from tkinter import *

if __name__ == '__main__':
    # Main object
    root = Tk()

    names = ['Emily', 'Diana', 'Barbara', 'Ada']
    surnames = ['Beautiful', 'Prince', 'Gordon', 'Lovelace']

    lb_names = Listbox(root)
    lb_surnames = Listbox(root)

    for i, name in enumerate(names):
        lb_names.insert(i, name)

    for i, surname in enumerate(surnames):
        lb_surnames.insert(i, surname)

    lb_names.pack()
    lb_surnames.pack()

    root.mainloop()
