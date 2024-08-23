#!/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

def is_active():
    import subprocess
    #out = subprocess.run("cat /proc/net/dev | grep wg0")
    out = subprocess.getoutput("cat /proc/net/dev | grep wg0")
    return len(out) != 0

def trayicon_activate(event):
    if is_active():
        to_run = "/home/akawolf/sources/wg-down"
    else:
        to_run = "/home/akawolf/sources/wg-up"

    import subprocess
    out = subprocess.getoutput(to_run)
    print(out)

    set_image()

def current_path():
    import os
    return os.path.dirname(os.path.realpath(__file__))

def get_statistics():
    import subprocess
    rx = subprocess.getoutput(r"cat /proc/net/dev | grep -oP 'wg0'':\s*\K\d+'")
    tx = subprocess.getoutput(r"cat /proc/net/dev | grep -oP 'wg0'':\s*(\d+\s+){8}\K\d+'")
    return (int(rx), int(tx))

active_flag = None
def set_image():
    def set_icon(flag):
        global active_flag
        if flag:
            icon.set_from_pixbuf(pb)
            active_flag = True
        else:
            icon.set_from_pixbuf(pb_grey)
            active_flag = False
    current_flag = is_active()
    if active_flag is None:
        if current_flag:
            set_icon(True)
        else:
            set_icon(False)
    else:
        if active_flag is True and not current_flag:
            set_icon(False)
        if active_flag is False and current_flag:
            set_icon(True)

import os
icon_path = os.path.join(current_path(), "wireguard.svg")
pb = GdkPixbuf.Pixbuf.new_from_file(icon_path)
pb_grey = pb.copy()
pb_grey.saturate_and_pixelate(pb_grey, 0.0, False)

icon = Gtk.StatusIcon()
#icon.set_from_stock(Gtk.STOCK_ABOUT)
#icon.set_from_file("/home/akawolf/sources/wireguard.svg")
#icon.set_from_pixbuf(pb)

set_image()

icon.connect("activate", trayicon_activate)
#icon.connect("popup_menu", self.trayicon_popup)

icon.set_tooltip_markup("wireguard")
#icon.set_tooltip_text("wireguard")

icon.set_visible(True)

from timeloop import Timeloop
from datetime import timedelta
from hurry.filesize import size

tl = Timeloop()

@tl.job(interval=timedelta(seconds=1))
def update_statistics():
    if is_active():
        rx, tx = get_statistics()
        rx, tx = size(rx), size(tx)
    else:
        rx, tx = 0, 0
    stat = f"<b>rx</b>: {rx}\n<b>tx</b>: {tx}"
    icon.set_tooltip_markup(stat)

    set_image()

tl.start(block=False)

Gtk.main()
