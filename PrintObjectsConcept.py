# String representation of class Object
# Obj printing concept

class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "x:%s y:%s" % (self.x, self.y)

    def __str__(self):
        return "value of x is %s and y is %s" % (self.x, self.y)


# Test Code
t = Test(10, 25)
print(t)
