#  File: Intervals.py

#  Description: Sorts a list of tuples and related functions

#  Student Name: Derek Wu

#  Student UT EID: dw29924

#  Partner Name: Yash Pathak

#  Partner UT EID: YKP224

#  Course Name: CS 313E

#  Unique Number: 502010

#  Date Created: 09/09/2019

#  Date Last Modified: 09/09/2019


# opens file and converts its contents into a sorted list of tuples
def read_file():
    with open('intervals.txt', 'r') as file:  # retrieves file from folder
        file_list = file.read().splitlines()
    tuple_list = []
    for i in file_list:
        line = i.split()
        line = tuple(int(j) for j in line)
        tuple_list.append(line)
    # tuples are sorted ascending from the first value of the interval
    tuple_list = sorted(tuple_list, key=getKey)
    return tuple_list

# returns true if two tuples overlap, if not it returns false


def does_overlap(tuple_1, tuple_2):
    lower_1 = int(tuple_1[0])
    upper_1 = int(tuple_1[1])
    lower_2 = int(tuple_2[0])
    upper_2 = int(tuple_2[1])
    if (lower_1 > upper_2 or upper_1 < lower_2):
        return False
    else:
        return True

# takes two tuples and collapses them


def collapse(tuple_1, tuple_2):
    lower_1 = int(tuple_1[0])
    upper_1 = int(tuple_1[1])
    lower_2 = int(tuple_2[0])
    upper_2 = int(tuple_2[1])
    collapsed_tuple = []
    if (lower_1 > lower_2):
        collapsed_tuple.append(lower_2)
    else:
        collapsed_tuple.append(lower_1)
    if (upper_1 > upper_2):
        collapsed_tuple.append(upper_1)
    else:
        collapsed_tuple.append(upper_2)
    return tuple(collapsed_tuple)

# function used to sort tuple_list


def getKey(item):
    return item[0]

# collapses all tuples in a list into a single tuples
# returns all the tuples that are not collapsable


def collapse_list(tuple_list):
    reference_tuple = tuple_list[0]
    non_intersecting_tuples = []
    # print(len(tuple_list))
    for i in range(len(tuple_list)):
        current_tuple = tuple_list[i]
        if does_overlap(reference_tuple, current_tuple) and i != len(tuple_list) - 1:
            # print(i)
            reference_tuple = collapse(reference_tuple, current_tuple)
        elif i == len(tuple_list) - 1:
            #print(i, 'will append last')
            reference_tuple = collapse(reference_tuple, current_tuple)
            #print('ref', reference_tuple)
            non_intersecting_tuples.append(reference_tuple)
            reference_tuple = tuple_list[i]
        else:
            #print(i, 'will append')
            non_intersecting_tuples.append(reference_tuple)
            reference_tuple = tuple_list[i]
    return (non_intersecting_tuples)

# prints out items in a list line by line


def print_output(tuple_list):
    for row in tuple_list:
        print(row)

# bonus question: returns the non-intersecting intervals in increasing order of the size of the intervals


def sort_output(tuple_list):
    import sys
    sorted_output = []
    while len(tuple_list) > 0:
        smallest_size_row = tuple_list[0]
        smallest_size = 0
        # finds smallest value in the tuple array and adds it to the output list while removing it from the tuple_list
        for row in tuple_list:
            new_size = abs(row[1] - row[0])
            #print(smallest_size)
            if new_size > smallest_size:
                #print(new_size)
                smallest_size = new_size
                smallest_size_row = row
        sorted_output.append(smallest_size_row)
        tuple_list.remove(smallest_size_row)
    sorted_output.reverse()
    return (sorted_output)


def main():
    print('Non-intersecting Intervals:')
    print_output(collapse_list(read_file()))
    print('Non-intersecting Intervals by order of size:')
    print_output(sort_output(collapse_list(read_file())))


main()
