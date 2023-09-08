import sys

from app.i18n import I18N
from app.gui import GUI


I18N.set_language("pl_PL")

gui = GUI(sys.argv)
gui.config()

status = gui.start_gui_cycle()

match status:
    case 0:
        print("Program finished successful")
    case _:
        print("Unexpected program finishing")
