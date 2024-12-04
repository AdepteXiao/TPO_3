class A:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return self.x

class B:
    def __init__(self, y: A):
        self.y = y

    def upd(self):
        self.y.x = "updated"

    def __str__(self):
        return str(self.y)

class Main:
    def __init__(self):
        self.a = A("a")
        self.b = B(self.a)
        self.b.upd()
        print(self.a)
        print(self.b)

Main()