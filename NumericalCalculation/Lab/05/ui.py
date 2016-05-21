import numpy as np
import matplotlib.pyplot as plt

from  gi.repository import Gtk, GLib

def frequence(lst):
    dic  = {}
    return dic;

def picture():
    pass

class myWindow(Gtk.Window):
    def __init__(self):
        self.lst = []
        Gtk.Window.__init__(self, title = "Frequence Analysis")
        self.set_border_width(10)
        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(5)
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        self.er_checkbox = Gtk.CheckButton("而")
        self.er_checkbox.connect("clicked", self.on_er_checkbox_clicked)

        self.he_checkbox = Gtk.CheckButton("何")
        self.he_checkbox.connect("clicked", self.on_he_checkbox_clicked)

        self.hu_checkbox = Gtk.CheckButton("乎")
        self.hu_checkbox.connect("clicked", self.on_hu_checkbox_clicked)

        self.nai_checkbox = Gtk.CheckButton("乃")
        self.nai_checkbox.connect("clicked", self.on_nai_checkbox_clicked)

        self.grid.add(self.er_checkbox)
        self.grid.attach(self.he_checkbox, 1, 0, 1, 1)
        self.grid.attach(self.hu_checkbox, 2, 0, 1, 1)
        self.grid.attach(self.nai_checkbox, 3, 0, 1, 1)

    def  on_er_checkbox_clicked(self, widget):
        self.lst.append("而")
        print(self.lst)
        print("this is 而")

    def  on_he_checkbox_clicked(self, widget):
        print("this is 何")

    def on_hu_checkbox_clicked(self, widget):
        print("this is 乎")

    def on_nai_checkbox_clicked(self, widget):
        print("this is 乃")

if __name__ == '__main__':
    try:
        myWin = myWindow()
        myWin.connect("delete-event", Gtk.main_quit)
        myWin.show_all()
        Gtk.main()
    except e:
        print(e)
