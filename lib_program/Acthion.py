class Acthion():
    def __init__(self):
        self.__functhions=[]
    def __iadd__(self, other):
        if not callable(other):
            raise ValueError("not invoke:"+str(other))
        self.__functhions.append(other)
        return self
    def __imul__(self, other):
        if not callable(other):
            raise ValueError("not invoke:"+str(other))
        self.__functhions.remove(other)
        return self
    def __call__(self, *args, **kwargs):
        self.invoke(*args, **kwargs)
    def invoke(self,*args,**kwargs):
        for i in self.__functhions:
            i(*args,**kwargs)

