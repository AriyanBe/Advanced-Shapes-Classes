COL_TITLE = '--------'
LINE = '--------'
COLOR_PREFIX = "Color: "
FILL_PREFIX = "Filled: "
SHORT_PREFIX = "Shortest Triangle Side: "
AREA_PREFIX = "Area of the rectangle: "


class Shape:
    def __init__(self, color, fill):
        self.setColor(color)
        self.setFill(fill)

    def setColor(self, color):
        self.__color = color

    def setFill(self, fill):
        self.__fill = fill

    def getColor(self):
        return self.__color

    def getFill(self):
        return self.__fill

    def __str__(self):
        if self.getFill == 1:
            fillStr = "Yes"
        else:
            fillStr = "No"
        return COLOR_PREFIX + self.getColor() + "\t" + FILL_PREFIX + fillStr


class Triangle(Shape):
    def __init__(self, color, fill, a1, a2, a3):
        super().__init__(color, fill)
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3

    def findShort(self):
        if self.__a1 < self.__a2 and self.__a1 < self.__a3:
            return self.__a1
        elif self.__a2 < self.__a1 and self.__a2 < self.__a3:
            return self.__a2
        else:
            return self.__a3

    def __str__(self):
        lineStr = super().__str__() + "\t" + SHORT_PREFIX + str(self.findShort())
        return lineStr

class Rectangle(Shape):
    def __init__(self, color, fill, b1, b2):
        super().__init__(color, fill)
        self.__b1 = b1
        self.__b2 = b2

    def findArea(self):
        area = self.__b1 * self.__b2
        return area

    def __str__(self):
        lineStrarea = super().__str__() + "\t" + AREA_PREFIX + str(self.findArea())
        return lineStrarea

    def printReport(objLst):
        print(LINE)
        for i in range(len(objLst)):
            print(objLst[i])
        print(LINE)

def main():
    tr1 = Triangle("Red", 1, 2.5, 3.1, 2.8)
    rect1 = Rectangle("Green", 0, 5, 10)
    objLst = [tr1, rect1]
    printReport(objLst)

main()
