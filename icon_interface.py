from gi.repository import Gtk, GdkPixbuf
import os

from wg_interface import is_active
from utils import current_path

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

def set_callback_activate(callback):
    icon.connect("activate", callback)

def set_tooltip(text):
    icon.set_tooltip_markup(text)

icon_path = os.path.join(current_path(), "wireguard.svg")
pb = GdkPixbuf.Pixbuf.new_from_file(icon_path)
pb_grey = pb.copy()
pb_grey.saturate_and_pixelate(pb_grey, 0.0, False)

icon = Gtk.StatusIcon()
icon.set_visible(True)
