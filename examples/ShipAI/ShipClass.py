


def setParam(Value):
    try:
        tmpVal= Value
        if tmpVal:
           return tmpVal
        else: return 0
    except ValueError:
        print('NullValueException')

class ship (object):
    def __new__(cls, *p, **k):
          inst = object.__new__(cls)
          return inst
    #def __init__(self,name,speed,manoevr,detect,armour,shield,hull,turrets,dorsal,prow,port,starboard,keel):
    def __init__(self, *p, **k):

        self.name=setParam(p[0])
        self.speed=setParam(p[1])
        self.manoevr=setParam(p[2])
        self.detect=setParam(p[3])
        self.armour=setParam(p[4])
        self.shield=setParam(p[5])
        self.hull=setParam(p[6])
        self.turrets=setParam(p[8])
        self.dorsal=setParam(p[8])
        self.prow=setParam(p[9])
        self.port=setParam(p[10])
        self.starboard=setParam(p[11])
        self.keel=setParam(p[12])

    def __getattribute__(self, name):
        return super(ship, self).__getattribute__(name)

    def __setattr__(self, name, value):
        return super(ship, self).__setattr__(name, value)

    def getAll(self, *p, **k):
        print "p={0} k={1}".format(p, k)
def gets(CLS,*p):
    print("p={0}".format(p))

"""
x=ship('aaa',9,2,3,4,3,10,3,2,2,3,0,3)
omg=getattr(x,'dorsal')
print(omg)
gets(x)
"""