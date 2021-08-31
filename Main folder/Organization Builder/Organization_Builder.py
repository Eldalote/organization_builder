from tkinter import *
from icecream import ic
from Subs.MasterList import MasterList
from Subs.UnitObject import UnitObject


def get_screen_size():
    """
    Hack to get the resolution of the active monitor
    :return: x, y, resolution in pixels.
    """
    test = Tk()
    test.update_idletasks()
    test.attributes('-fullscreen', True)
    test.state('iconic')
    x = test.winfo_width()
    y = test.winfo_height()    
    test.destroy()
    return x, y

def main():
    #Get screen resolution of the active monitor
    screensize = get_screen_size()

    #build the main window
    mainWindow = Tk()
    mainWindow.geometry(f'{300}x{300}+{int(screensize[0]*0.4)}+{int(screensize[1]*0.4)}')
    mainWindow.title("Main Window")

    ML = MasterList("todo")
    ML.display()


       
    #main windown main loop
    mainWindow.mainloop()
    

if __name__ == "__main__":
    main()