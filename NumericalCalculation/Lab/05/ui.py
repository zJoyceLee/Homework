import numpy as np
import matplotlib
matplotlib.use('Gtk3Agg')
import matplotlib.pyplot as plt

import gi
gi.require_version('Gtk', '3.0')
from  gi.repository import Gtk, GLib

def frequency(lst):
    """
    Recive a list and the file path: Foo(lst, path)
    Return a dict: list value is key, frequency in file is value
    """
    dic  = {}
    """ function here """
    return dic;

def picture(dic):
    """
    Draw the dict with histogram
    """
    n = len(dic)
    frequency = tuple(dic.values())
    ind = np.arange(n)
    width =  0.35
    fig, ax = plt.subplots()
    rects = ax.barh(ind, frequency, width, color = 'y')
    ax.set_xlabel('frequency')
    ax.set_ylabel('word')
    ax.set_title('Distribution')
    ax.set_yticks(ind + width)

    word = tuple(dic.keys())
    ax.set_yticklabels(word)

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            width  = rect.get_width()
            text_y = rect.get_y() + rect.get_height() / 2.
            text_x = 1.05 * width
            ax.text(text_x, text_y,
                    '%d' % int(width), ha = 'center', va = 'bottom')

    autolabel(rects)
    plt.show()


class myWindow(Gtk.Window):
    def __init__(self):
        self.particle_lst = ['而', '何', '乎', '乃', '其', '且', '若', '所', '为', '焉', '也', '以', '因', '于', '与', '则', '者', '之']
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

        self.label = Gtk.Label("请输入虚词")
        self.entry = Gtk.Entry()

        self.submit_button = Gtk.Button("Submit")
        self.submit_button.connect("clicked", self.on_submit_button_clicked)


        self.grid.add(self.er_checkbox)
        self.grid.attach(self.he_checkbox, 1, 0, 1, 1)
        self.grid.attach(self.hu_checkbox, 2, 0, 1, 1)
        self.grid.attach(self.nai_checkbox, 3, 0, 1, 1)
        self.grid.attach(self.label, 0, 1, 2, 1)
        self.grid.attach(self.entry, 2, 1, 2, 1)
        self.grid.attach(self.submit_button, 0, 2, 1, 1)

    def  on_er_checkbox_clicked(self, widget):
        if "而" in self.lst:
            self.lst.remove("而")
        else:
            self.lst.append("而")
        print(self.lst)

    def  on_he_checkbox_clicked(self, widget):
        if "何" in self.lst:
            self.lst.remove("何")
        else:
            self.lst.append("何")
        print(self.lst)

    def on_hu_checkbox_clicked(self, widget):
        if "乎" in self.lst:
            self.lst.remove("乎")
        else:
            self.lst.append("乎")
        print(self.lst)

    def on_nai_checkbox_clicked(self, widget):
        if "乃" in self.lst:
            self.lst.remove("乃")
        else:
            self.lst.append("乃")
        print(self.lst)

    def on_submit_button_clicked(self, widget):
        """
        draw result
        """
        ss = self.entry.get_text()
        if ss != '' and  ss in self.particle_lst and ss not in self.lst:
            self.lst.append(ss)

        n = len(self.lst)
        dic = frequency(self.lst)
        d = {'1':1, '2':2, '3':3.3}
        """ Here you shuld use dic After finished the func frequency"""
        picture(d)


if __name__ == '__main__':
    try:
        myWin = myWindow()
        myWin.connect("delete-event", Gtk.main_quit)
        myWin.show_all()
        Gtk.main()
    except:
        print('Error')
