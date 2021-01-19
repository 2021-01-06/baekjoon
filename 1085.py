import sys
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

o = Location(0, 0)
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
a = Location(x1, y1)
b = Location(x2, y2)

print(min(abs(x2-x1), abs(x1-0), abs(y2-y1), abs(y1-0)))
