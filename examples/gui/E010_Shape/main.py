from tkinter import *
from math import sin
from math import cos

if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, height=512, width=512)
    y_pad = 50
    w_height = 512
    w_width = 512
    x = 62
    body_len = 100
    a_len = 60
    l_len = 75

    oval = canvas.create_oval((w_width - x) / 2,
                              y_pad,
                              (w_width - x) / 2 + x,
                              y_pad + x)
    body = canvas.create_line(w_width / 2,
                              y_pad + x,
                              w_width / 2,
                              y_pad + x + body_len)
    l_arm = canvas.create_line(w_width / 2,
                               y_pad + x,
                               w_width / 2 + sin(60) * a_len,
                               y_pad + x - cos(60) * a_len)
    r_arm = canvas.create_line(w_width / 2,
                               y_pad + x,
                               w_width / 2 - sin(60) * a_len,
                               y_pad + x - cos(60) * a_len)
    l_leg = canvas.create_line(w_width / 2,
                               y_pad + x + body_len,
                               w_width / 2 + sin(60) * l_len,
                               y_pad + x + body_len - cos(60) * l_len)
    r_leg = canvas.create_line(w_width / 2,
                               y_pad + x + body_len,
                               w_width / 2 - sin(60) * l_len,
                               y_pad + x + body_len - cos(60) * l_len)
    canvas.pack()

    root.mainloop()
