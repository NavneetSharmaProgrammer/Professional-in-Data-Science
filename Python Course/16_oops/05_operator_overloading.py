class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def print_point(self):
        print(f"X is {self.x}, Y is {self.y}")

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
p1 = Point(10, 20)
p2 = Point(30, 40)

# p = p1.sum(p2) # This will return a new Point object with x=40 and y=60
p = p1 + p2  # Using the overloaded + operator
p.print_point()  # Output: X is 40, Y is 60