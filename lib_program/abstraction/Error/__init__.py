class ErrorAbstraction(Exception):
    pass
class ErrorAbstractObject(ErrorAbstraction):
    def __init__(self,cls):
        super().__init__("it is impossible to create Object of Abstract class name:"+cls.__name__)
class ErrorInterferenceObject(ErrorAbstraction):
    def __init__(self,cls):
        super().__init__("it is impossible to create Object of Interference name:"+cls.__name__)
class ErrorInterfeseNotInitMethod(ErrorAbstraction):
    def __init__(self,cls,name):
        super().__init__("not realization Method in class "+cls.__name__+": "+name)
