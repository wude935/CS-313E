#  File: Geom.py

#  Description: Functions related to basic Geometry

#  Student Name: Derek Wu

#  Student UT EID: dw29924

#  Partner Name: Victor Li

#  Partner UT EID: vql83

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/20/19

#  Date Last Modified: 9/20/19


import math


class Point (object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle (object):
    # constructor
    # x, y, and radius are floats
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c overlaps this circle (non-zero area of overlap)
    # but neither is completely inside the other
    # the only argument c is a Circle object
    # returns a boolean
    def circle_overlap(self, c):
        distance = self.center.dist(c.center)
        inside = self.circle_inside(c)
        return not inside and distance < (self.radius + c.radius)

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribe(self, r):
        x = (r.ul.x + r.lr.x)/2
        y = (r.ul.y + r.lr.y)/2
        radius = r.lr.dist(r.ul)/2
        output = Circle(radius, x, y)
        return output

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__(self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return abs(self.radius - other.radius) <= tol


class Rectangle (object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        return float(abs(self.ul.x-self.lr.x))

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width(self):
        return float(abs(self.ul.y-self.lr.y))

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        return 2*self.length() + 2*self.width()

    # determine the area
    # takes no arguments, returns a float
    def area(self):
        return self.length() * self.width()

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside(self, p):
        return (self.ul.x < p.x < self.lr.x) and (self.lr.y < p.y < self.ul.y)

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside(self, r):
        return r.ul.x < self.ul.x and r.lr.x > self.lr.x and r.ul.y > self.ul.y and r.lr.y < self.lr.y

    # determine if the Rectangles has the exact same cooridinates and dimensions
    # takes a rectangle object r as an argument, returns a boolean
    def rectangle_exact_same(self, r):
        return r.ul.x == self.ul.x and r.lr.x == self.lr.x and r.ul.y == self.ul.y and r.lr.y == self.lr.y

    # determine if the Rectangles has the exact same cooridinates and dimensions
    # takes a rectangle object r as an argument, returns a boolean
    def rectangle_share_side(self, r):
        return r.ul.x == self.ul.x or r.lr.x == self.lr.x or r.ul.y == self.ul.y or r.lr.y == self.lr.y

    # determine if the Rectangles do not overlap
    def rectangle_no_overlap(self, r):
        return r.lr.x > self.ul.x or r.ul.x < self.lr.x or r.lr.y > self.ul.y or r.lr.y > self.ul.y

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def rectangle_overlap(self, r):
        x_range = [self.ul.x, self.lr.x]
        y_range = [self.lr.y, self.ul.y]
        return x_range[0] < r.ul.x < x_range[1] or x_range[0] < r.lr.x < x_range[1] or y_range[0] < r.ul.y < y_range[1] or y_range[0] < r.lr.y < y_range[1]

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rectangle_circumscribe(self, c):
        ul_x = c.center.x - c.radius
        lr_x = c.center.x + c.radius
        ul_y = c.center.y + c.radius
        lr_y = c.center.y - c.radius
        return Rectangle(ul_x, ul_y, lr_x, lr_y)

    # give string representation of a rectangle
    # takes no arguments, returns a string

    def __str__(self):
        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        return self.width() == other.width() and self.length() == other.length()


def main():
    # open the file geom.txt
    with open('Assignment 5/geom.txt', 'r') as file:
        file_list = file.read().splitlines()
    input = [line.split('#')[0].strip().split() for line in file_list]
    # create Point objects P and Q
    P = Point(float(input[0][0]), float(input[0][1]))
    Q = Point(float(input[1][0]), float(input[1][1]))
    # print the coordinates of the points P and Q
    print('Coordinates of P:', P)
    print('Coordinates of Q:', Q)
    # find the distance between the points P and Q
    print('Distance between P and Q:', P.dist(Q))
    # create two Circle objects C and D
    C = Circle(float(input[2][0]), float(input[2][1]), float(input[2][2]))
    D = Circle(float(input[3][0]), float(input[3][1]), float(input[3][2]))
    # print C and D
    print('Circle C:', C)
    print('Circle D:', D)
    # compute the circumference of C
    print('Circumference of C:', C.circumference())
    # compute the area of D
    print('Area of D:', D.area())
    # determine if P is strictly inside C
    if (C.point_inside(P)):
        print('P is inside C')
    else:
        print('P is not inside C')
    # determine if C is strictly inside D
    if (D.circle_inside(C)):
        print('C is inside D')
    else:
        print('C is not inside D')
    # determine if C and D intersect (non zero area of intersection)
    if (D.circle_overlap(C)):
        print('C does intersect D')
    else:
        print('C does not intersect D')
    # determine if C and D are equal (have the same radius)
    if C == D:
        print('C is equal to D')
    else:
        print('C is not equal to D')
    # create two rectangle objects G and H
    G = Rectangle(float(input[4][0]), float(input[4][1]),
                  float(input[4][2]), float(input[4][3]))
    H = Rectangle(float(input[5][0]), float(input[5][1]),
                  float(input[5][2]), float(input[5][3]))
    # print the two rectangles G and H
    print('Rectangle G:', G)
    print('Rectangle H:', H)
    # determine the length of G (distance along x axis)
    print('Length of G:', G.length())
    # determine the width of H (distance along y axis)
    print('Width of H:', H.width())
    # determine the perimeter of G
    print('Perimeter of G:', G.perimeter())
    # determine the area of H
    print('Area of H:', H.area())
    # determine if point P is strictly inside rectangle G
    if (G.point_inside(P)):
        print('P is inside G')
    else:
        print('P is not inside G')
    # determine if rectangle G is strictly inside rectangle H
    if G.rectangle_inside(H):
        print('G is inside H')
    else:
        print('G is not inside H')
    # determine if rectangles G and H overlap (non-zero area of overlap)
    if G.rectangle_overlap(H):
        print('G does overlap H')
    else:
        print('G does not overlap H')
    # find the smallest circle that circumscribes rectangle G
    # goes through the four vertices of the rectangle
    circle = Circle()
    print('Circle that circumscribes G:', circle.circle_circumscribe(G))
    # find the smallest rectangle that circumscribes circle D
    # all four sides of the rectangle are tangents to the circle
    rectangle = Rectangle()
    print('Rectangle that circumscribes D:',
          rectangle.rectangle_circumscribe(D))
    # determine if the two rectangles have the same length and width
    if G == H:
        print('Rectangle G is equal to H')
    else:
        print('Rectangle G is not equal to H')
    # close the file geom.txt
    file.close()


# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
