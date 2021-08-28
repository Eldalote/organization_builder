class UnitObject(object):
    """description of class"""
    def __init__(self, name, unittype):
        self.UnitType = unittype
        self.Name = name
        self.SubUnits = []
        self.Tags = []
        self.Rank = None
        
    
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

