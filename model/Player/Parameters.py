class Value():
    def __init__(self,value=0,bonus=0):
        self.value=value
        self.bonus=bonus
    def getValue(self):
        return self.value
class Atribut():
    def __init__(self):
        self.values=[Value(),
                     Value(),
                     Value()]
        self.stronger=1

class Parameters():
    def __init__(self):
        self.body        = Atribut()
        self.intilegent  = Atribut()
        self.mental      = Atribut()
        self.Wildness    = Atribut()
