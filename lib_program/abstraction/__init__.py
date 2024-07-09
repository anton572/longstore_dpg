from lib_program.abstraction.Error import *

class Abstract():
    def __new__(cls):
        if Abstract in cls.mro()[:2]:
            raise ErrorAbstractObject(cls)
        return super().__new__(cls)
def der(name):
    def abstr(self,*a,**k):
        raise ErrorInterfeseNotInitMethod(self,name)
    return abstr
def _getMethod(cls):
    return [func for func in dir(cls) for i in cls.mro()
                if callable(getattr(cls, func))
                and not (
                    func.startswith("__")
                    or func.startswith('_'+i.__name__+"__")
                        )
                ]
def _relialase(cls):

        method=_getMethod(cls)

        for i in method:

            abstr=der(i)
            abstr.name=i
            setattr(cls,i,abstr)
def _getyorMethod(cls):
    return [attr for attr in dir(cls) if callable(getattr(cls, attr)) and attr in cls.__dict__]
class Interference():
    id=0
    def __new__(cls, *args, **kwargs):
        if Interference in cls.mro()[:2]:
            raise ErrorInterferenceObject(cls)
        elif Interference == cls.mro()[2]:
            if cls.id != id(cls):
                indax=cls.mro().index(Interference)
                beforeInterference=cls.mro()[indax-1]
                cls.id=id(cls)
                _relialase(beforeInterference)
                methodbeforeInterference=_getyorMethod(beforeInterference)
                methodmy=[attr for attr in dir(cls) if callable(getattr(cls, attr)) and attr in cls.__dict__]
                for i in methodbeforeInterference:
                    if not i in methodmy:
                        raise ErrorInterfeseNotInitMethod(cls,i)
        else:
            clas=cls.__mro__[1]

            clas.__new__(clas)
        return super().__new__(cls)




