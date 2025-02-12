class GPS:
    def __init__(self,g,p,s):
        self._g = g
        self._p = p
        self._s = s
    def getG(self):
        return self._g
    def getP(self):
        return self._p
    def getS(self):
        return self._s
    def setG(self, new_g):
        self._g = new_g
    def setP(self, new_p):
        self._p = new_p
    def setS(self, new_s):
        self._s = new_s
n = GPS(1,0,0)
n.setG(int(input()))
n.setP(int(input()))
n.setS(int(input()))
print (n.getG(),n.getP(),n.getS())

