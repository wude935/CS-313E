#  File: ConvexHull.py

#  Description: Returns the points of a convex hull and its area

#  Student Name: Derek Wu

#  Student UT EID: dw29924

#  Partner Name: Victor Li

#  Partner UT EID: vql83

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/27/19

#  Date Last Modified: 9/27/19

import math


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

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects


def det(p, q, r):
    # print('p', p)
    # print('q', q)
    # print('r', r)
    return (p.x * q.y) + (q.x * r.y) + (r.x * p.y) - (p.y * q.x) - (q.y * r.x) - (r.y * p.x)

# computes and returns the convex hull of a sorted list of Points
# # convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order


def convex_hull(sorted_points):
    # Create an empty list upper_hull that will store the vertices in the upper hull.
    upper_hull = []
    # Append the first two points p1 and p2 in order into the upper_hull.
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    # For i going from 3 to n
    sorted_points_length = len(sorted_points)
    for i in range(2, sorted_points_length):
        # Append pi to upper_hull.
        upper_hull.append(sorted_points[i])
        # While upper_hull contains three or more points and the last three points in upper_hull do not make a right (negative) turn do
        while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) >= 0:
            # Delete the middle of the last three points from upper_hull
            del upper_hull[-2]
    # Create an empty list lower_hull that will store the vertices in the lower hull.
    lower_hull = []
    # Append the last two points pn and pn-1 in order into lower_hull with pn as the first point.
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])
    # For i going from n - 2 down to 1
    for j in range(sorted_points_length - 3, -1, -1):
        # Append pi to lower_hull
        lower_hull.append(sorted_points[j])
        # While lower_hull contains three or more points and the last three points in the lower_hull do not make a right turn do
        while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0:
            # Delete the middle of the last three points from lower_hull
            del lower_hull[-2]
    # Remove the first and last points for lower_hull to avoid duplication with points in the upper hull.
    del lower_hull[0]
    del lower_hull[-1]
    # Append lower_hull to upper_hull and call it the convex_hull
    convex_hull = upper_hull + lower_hull
    # Return the convex_hull.`
    return convex_hull
# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order


def area_poly(convex_poly):
    convex_poly.append(convex_poly[0])
    add = 0
    sub = 0
    # finds half of the determinate
    for i in range(len(convex_poly) - 1):
        add = add + (convex_poly[i].x * convex_poly[i + 1].y)
        sub = sub + (convex_poly[i].y * convex_poly[i + 1].x)
    area = .5 * abs(add - sub)
    return area


def main():
    file_name = 'Assignment 7/points.txt'
    #file_name = 'points.txt'
    # create an empty list of Point objects
    point_list = []
    # open file points.txt for reading
    with open(file_name, 'r') as file:
        # read file line by line, create Point objects and store in a list
        file_list = file.read().splitlines()
    for i in range(1, int(file_list[0]) + 1):
        item = [int(point) for point in file_list[i].split()]
        point = Point(item[0], item[1])
        point_list.append(point)
    # sort the list according to x-coordinates
    point_list.sort()
    # get the convex hull
    _convex_hull = convex_hull(point_list)
    # print the convex hull
    print('Convex Hull')
    for item in _convex_hull:
        print(item)
    # get the area of the convex hull
    area = area_poly(_convex_hull)
    # print the area of the convex hull
    print('Area of Convex Hull =', area)


# YOU MUST WRITE THIS LINE AS IS
if __name__ == "__main__":
    main()
