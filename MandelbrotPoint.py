from PIL import Image
import numpy as np

class MandelbrotPoint:
    INFINITY = 2
    MAX_ITER = 500

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "x={0} y={1}".format(self.x, self.y)

    def colorOrbite1(self, n, a, b):
        if n < self.MAX_ITER:
            i = n % 16
            mapping = {}
            mapping[0]=[66, 30, 15]
            mapping[1]=[25, 7, 26]
            mapping[2]=[9, 1, 47]
            mapping[3]=[4, 4, 73]
            mapping[4]=[0, 7, 100]
            mapping[5]=[12, 44, 138]
            mapping[6]=[24, 82, 177]
            mapping[7]=[57, 125, 209]
            mapping[8]=[134, 181, 229]
            mapping[9]=[211, 236, 248]
            mapping[10]=[241, 233, 191]
            mapping[11]=[248, 201, 95]
            mapping[12]=[255, 170, 0]
            mapping[13]=[204, 128, 0]
            mapping[14]=[153, 87, 0]
            mapping[15]=[106, 52, 3]
            return mapping[i]
        else:
            return [0, 0, 0]

    def colorOrbite2(self, n, a, b):
        if n < self.MAX_ITER:

            return mapping[i]
        else:
            return [0, 0, 0]

    def getColor(self):
        a = 0
        b = 0
        i = 0
        N = 0
        inf = self.INFINITY * self.INFINITY
        while N < inf and i < self.MAX_ITER:
            aa = a
            a = a*a-b*b + self.x
            b = 2*aa*b + self.y
            i+=1
            N = a*a+b*b
        return self.colorOrbite1(i,a,b)


class MandelbrotSet:

    #x,y coordinate of center of image, width and height the number of pixels to compute
    def __init__(self,xmin,xmax,ymin,ymax,width=640, height=480):
        self._xmin = xmin
        self._xmax = xmax
        self._ymin = ymin
        self._ymax = ymax
        self._width = width
        self._height = height
        self._data = None

    def compute(self):
        self._data = np.zeros((self._width, self._height, 3), dtype=np.uint8)
        xstep = (self._xmax - self._xmin) / self._width
        ystep = (self._ymax - self._ymin) / self._height
        i=0
        while i<self._width:
            j=0
            while j<self._height:
                m = MandelbrotPoint(self._xmin+i*xstep, self._ymin+j*ystep)
                self._data[i, j] = m.getColor()
                j+=1
            i+=1

    def exportToImage(self):
        return Image.fromarray(self._data)

if __name__ == "__main__":
    mSet = MandelbrotSet(-2,1,-1.5,1.5,500,500)
    mSet.compute()
    mSet.exportToImage().show()

