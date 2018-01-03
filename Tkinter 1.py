from tkinter import *

class Window(Frame):

    def __int__(self,master = None):
        Frame.__int__(self,master)

        self.master = master

        self.int_window()

    def int_window(self):

        self.master.tile("GUI")

        self.pack(fill=BOTH, expand = 1)

        quitButton = Button(self,text="quit")

        quitButton.place(x=0, y=0)

root = Tk()
root.geometry("700x300")
app = Window(root)

root.mainloop()

