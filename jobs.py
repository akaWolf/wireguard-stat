from timeloop import Timeloop
from datetime import timedelta
from hurry.filesize import size

from wg_interface import is_active, get_statistics
from icon_interface import set_image, set_tooltip

tl = Timeloop()

@tl.job(interval=timedelta(seconds=1))
def update_statistics():
    if is_active():
        rx, tx = get_statistics()
        rx, tx = size(rx), size(tx)
    else:
        rx, tx = 0, 0

    stat = f"<b>rx</b>: {rx}\n<b>tx</b>: {tx}"
    set_tooltip(stat)

    set_image()
