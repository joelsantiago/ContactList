__author__ = 'Joel Santiago'

from ttk import Frame, Label, Style
from Tkinter import *


class ContactList(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Contact List")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        contacts = [
            'Joel Santiago',
            'Sandra Rusakiewicz',
            'Jose Santiago',
            'Marlise Santiago'
        ]

        lbl = Label(self, text="Contacts")
        lbl.grid(padx=16, pady=5, sticky=W)

        lb = Listbox(self)
        for i in contacts:
            lb.insert(END, i)

        lb.bind("<<ListboxSelect>>", self.onSelect)

        lb.grid(row=1, column=0, columnspan=2, rowspan=4, padx=20, sticky=(E + W + S + N))

        nameLabel = Label(self, text="Name")
        nameLabel.grid(row=1, column=2)
        entry = Entry(self)
        entry.grid(row=1, column=3)

        addressLabel = Label(self, text="Address")
        addressLabel.grid(row=2, column=2)
        entry = Entry(self)
        entry.grid(row=2, column=3)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.grid(row=5, column=0, padx=16, pady=5, sticky=W)

    def onSelect(self, val):

        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)


def main():

    root = Tk()
    cl = ContactList(root)
    root.geometry("500x250+300+200")
    root.mainloop()

if __name__ == '__main__':
    main()
