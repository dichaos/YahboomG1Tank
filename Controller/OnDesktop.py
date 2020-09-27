from sys import platform
from tkinter import Tk
import UI.MainWindow as mainWindow
import Comms.NetworkReader as NetworkReader
import sys

root = Tk()

#create window
root.geometry("1024x600")
#root.geometry("800x480")
root.resizable(False, False)

if platform != "win32":
    root.overrideredirect(1)

app = mainWindow.MainWindow(root)

def on_closing():
    app.close()
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()


