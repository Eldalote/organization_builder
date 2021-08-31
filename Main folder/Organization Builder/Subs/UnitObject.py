from tkinter import *
from icecream import ic
class UnitObject(object):
    """description of class"""
    def __init__(self, master):
        self.UnitType = None
        self.Name = None
        self.SubUnits = []
        self.Tags = []
        self.Rank = None
        self.Master = master
        
    
    def Add_SubUnit(self, subunit):
        self.SubUnits.append(subunit)
    def Remove_SubUnit(self, subunit):
        pass
    def print(self):
        pass
    def Add_Tag(self, tag):
        self.Tags.append(tag)
    def Remove_Tag(self, tag):
        pass
    def Check_HasTag(self, tag):
        if self.Tags:
            for item in self.Tags:
                if item == tag:
                    return 1
        return 0
    def Count_Tag(self, tag):
        count = self.Check_HasTag(tag)
        if self.SubUnits:
            for unit in self.SubUnits:
                count += unit.Count_Tag(tag)
        return count
    def Set_Rank(self, rank):
        self.Rank = rank
    def Set_Name(self, name):
        self.Name = name
    def Set_UnitType(self, unittype):
        self.UnitType = unittype
    def Save(self):
        pass
    def define(self, name, subunits, tags, rank):
        self.Name = name
        self.SubUnits = subunits
        self.Tags = tags
        self.Rank = rank

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
        geometry = "300x300+100+100"
        self.window.geometry(geometry)