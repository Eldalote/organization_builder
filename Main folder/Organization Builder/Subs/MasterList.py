from tkinter import *
from tkinter import simpledialog
from icecream import ic
from Subs.UnitObject import UnitObject
class MasterList(object):
    """description of class"""
    def __init__(self, file):
        self.UnitList = []
        self.RankList = []
        self.TypeList = []
        self.FilePath = file
        self.Name = None        

        self.LoadList()


    def Save(self):
        pass
    def LoadList(self):
        pass
    def ConstructUnits(self):
        pass
    def AddNewUnit(self):
        pass
    def AddNewRank(self):
        rank = simpledialog.askstring("Rank?", "What is the new Rank?")
        self.RankList.append(rank)
        self._Populate_list()
    def AddNewType(self):
        type = simpledialog.askstring("Type?", "What is the new Type?")
        self.TypeList.append(type)
        self._Populate_list()
    def display(self):
        """Displays the window. Unhides it if it already exits, creates it if not."""
        try:
            self.window.deiconify()
        except:
            self._create_window()
        self.window.focus_set()

    def _hide(self):
        """Hides the window"""
        try: 
            self.window.withdraw()
        except:
            pass

    def _close(self):
        """Closes the window (destroy Toplevel object)"""
        try:
            self.window.close()
        except:
            pass

    def _create_window(self):
        """Creates the window"""        
        #create the window
        self.window = Toplevel()
        geometry = "580x600+100+100"
        self.window.geometry(geometry)

        #change 'x' button behavour from close to hide
        self.window.protocol("WM_DELETE_WINDOW", self._hide)
        
        self.window.title(self.Name)
        self.WindowItemList = []
        Button(self.window, text = "Add New Unit", width = 25, height = 5, command = self.AddNewUnit).grid(row= 0, column = 0)
        Button(self.window, text = "Add New Type", width = 25, height = 5, command = self.AddNewType).grid(row= 0, column = 1)
        Button(self.window, text = "Add New Rank", width = 25, height = 5, command = self.AddNewRank).grid(row= 0, column = 2)
        self.TypeListFrame = Frame(self.window, bd = 3, relief = GROOVE, width = 75)
        self.TypeListFrame.grid(row = 1, column = 0, columnspan = 3, sticky = W)
        self.RankListFrame = Frame(self.window, bd = 3, relief = GROOVE)
        self.RankListFrame.grid(row = 2, column = 0, columnspan = 3, sticky = W)
        self.UnitListFrame = Frame(self.window, bd = 3, relief = GROOVE)
        self.UnitListFrame.grid(row = 3, column = 0, columnspan = 3, sticky = W)

        self._Populate_list()

    def _Populate_list(self):
        for item in self.WindowItemList:
            item.destroy()
        self.WindowItemList.clear()
        
        gridrow = 0
        self.WindowItemList.append(Label(self.TypeListFrame, text = "Types:", font=("Futura", 18)))
        self.WindowItemList[-1].grid(row = gridrow, column = 0, rowspan = 3)
        self.WindowItemList.append(Label(self.TypeListFrame, width =50, height = 0))
        self.WindowItemList[-1].grid(row = gridrow, column = 1, columnspan = 4)
        for type in self.TypeList:
            self.WindowItemList.append(Label(self.TypeListFrame, text = type))
            self.WindowItemList[-1].grid(row = gridrow, column = 1, sticky = W)
            gridrow += 1

        gridrow = 0
        self.WindowItemList.append(Label(self.RankListFrame, text = "Ranks:", font=("Futura", 18)))
        self.WindowItemList[-1].grid(row = gridrow, column = 0, rowspan = 3)
        for rank in self.RankList:
            self.WindowItemList.append(Label(self.RankListFrame, text = rank))
            self.WindowItemList[-1].grid(row = gridrow, column = 1)
            gridrow += 1



