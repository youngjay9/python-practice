class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f'Shape __init__ local namespace:{locals()}')

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y
        # print(f'Shape move local namespace:{locals()}')

    print(f'Shape class namespace:{locals()}')



class Circle(Shape):
    PI = 3.14

    def __init__(self, r=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = r
        print(f'Circle __init__ local namespace:{locals()}')

    def area(self):
        # print(f'Circle area local namespace:{locals()}')
        # print(f'Circle area global namespace:{list(globals())}')
        return self.__class__.PI * self.radius * self.radius

    print(f'Circle class namespace:{locals()}')
    print(f'Circle class namespace:{globals()}')



print(f'shape module global namespace:{list(globals())}')
