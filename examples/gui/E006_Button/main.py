from tkinter import *


class Application:
    def __init__(self, _root):
        frame = Frame(_root)
        frame.pack()

        self.button = Button(frame, text="Close", fg="green", command=frame.quit)
        self.button.pack(side=LEFT)

        self.salute = Button(frame, text="Hi", bg="yellow", command=self.print_msg)
        self.salute.pack(side=LEFT)

    @staticmethod
    def print_msg():
        print("Hello")


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
