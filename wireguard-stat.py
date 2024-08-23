#!/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from wg_interface import is_active
from icon_interface import set_image, set_tooltip, set_callback_activate
from jobs import tl

def trayicon_activate(event):
    if is_active():
        to_run = "/home/akawolf/sources/wg-down"
    else:
        to_run = "/home/akawolf/sources/wg-up"

    import subprocess
    out = subprocess.getoutput(to_run)
    print(out)

    set_image()


set_tooltip("wireguard")

set_callback_activate(trayicon_activate)

set_image()

tl.start(block=False)

Gtk.main()
