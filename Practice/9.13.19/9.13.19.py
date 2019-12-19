import math

# Programming Exercise: Given a set of points find the shortest distance
# between any two points in that set.
# Extension 1: Find the Point objects that have the shortest distance
# and print them.

# Extension 2: Find the maximum distance and the Point objects that
# have the maximum distance.


class Point (object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # test for equality of two Point objects
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


def read_file():
    try:
        point_list = [int(line) for line in point_list]

    # with open('Practice/9.13.19/points.txt', 'r') as file:
    #     point_list = file.read()
    # print(point_list)


def main():
    # create an empty list of Point objects
    read_file()
    # open file points.txt for reading

    # read the file line by line, create Point objects and add to the list

    # initialize a variable to hold the shortest distance

    # Use a pair of nested loops to go through all pairs of Point objects
    # Find the minimum distance between all pairs

    # print the shortest distance


main()
