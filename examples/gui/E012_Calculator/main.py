from tkinter import *
from functools import partial


def call_result(label_result, first, second):
    result = int(first.get()) + int(second.get())
    label_result.config(text="Result = %d" % result)
    return


def add(label, n1, n2):
    result = int(n1.get()) + int(n2.get())
    label.config(text="Result = {}".format(result))
    return


def sub(label, n1, n2):
    result = int(n1.get()) - int(n2.get())
    label.config(text="Result = {}".format(result))
    return


def mul(label, n1, n2):
    result = int(n1.get()) * int(n2.get())
    label.config(text="Result = {}".format(result))
    return


def div(label, n1, n2):
    if n2.get() != 0:
        result = int(n1.get()) / int(n2.get())
        label.config(text="Result = {}".format(result))
        return


if __name__ == '__main__':
    root = Tk()
    root.geometry('480x480')
    root.title('PyC')

    fst = StringVar()
    snd = StringVar()

    l_fst = Label(root, text="First: ").grid(row=1, column=0)
    l_snd = Label(root, text="Second").grid(row=2, column=0)
    l_rsl = Label(root)
    l_rsl.grid(row=7, column=2)

    e_fst = Entry(root, textvariable=fst).grid(row=1, column=2)
    e_snd = Entry(root, textvariable=snd).grid(row=2, column=2)

    partial_add = partial(add, l_rsl, snd, fst)
    partial_sub = partial(sub, l_rsl, snd, fst)
    partial_mul = partial(mul, l_rsl, snd, fst)
    partial_div = partial(div, l_rsl, snd, fst)

    btn_add = Button(root, text="Add", command=partial_add).grid(row=3, column=1)
    btn_sub = Button(root, text="Sub", command=partial_sub).grid(row=3, column=2)
    btn_mul = Button(root, text="Mul", command=partial_mul).grid(row=4, column=1)
    btn_div = Button(root, text="Div", command=partial_div).grid(row=4, column=2)

    root.mainloop()
