from sys import platform
from tkinter import Tk
import UI.MainWindow as mainWindow
import Comms.NetworkReader as NetworkReader

root = Tk()

#create window
root.geometry("1024x600")
#root.geometry("800x480")
root.resizable(False, False)

if platform != "win32":
    root.overrideredirect(1)

app = mainWindow.MainWindow(root)

root.mainloop()


