from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.geometry("512x512")

    v = [IntVar() for _ in range(3)]
    languages = ("English", "Russian", "Turkish")
    buttons = []

    for i, lang in enumerate(languages):
        btn = Checkbutton(root, text=lang, variable=v[i],
                          onvalue=1, offvalue=0, height=2, width=10)
        buttons.append(btn)

    for btn in buttons:
        btn.pack()

    root.mainloop()
