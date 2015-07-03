__author__ = '28164'


class Coordinate(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Coordinates are ' + str(self.__dict__)

def wrapper(some_function):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)

        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)

        ret = some_function(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker

@wrapper
def add(a, b):
    return Coordinate(a.x+b.x, a.y+b.y)

one = Coordinate(100,200)
two = Coordinate(-100,200)

print add(one, two)