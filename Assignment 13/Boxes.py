#  File: Boxes.py

#  Description: Finds the largest subsets of boxes that can stack given a list of boxes

#  Student Name: Derek Wu

#  Student UT EID: dw29924

#  Partner Name: Victor Li

#  Partner UT EID: vql83

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/18/19

#  Date Last Modified: 10/18/19


def read_file():
    file_name = 'boxes.txt'
    # open file box.txt for reading
    with open(file_name, 'r') as file:
        file_list = file.read().splitlines()
    box_list = []
    for i in range(1, int(file_list[0]) + 1):
        box_list.append(sorted(list(map(int, file_list[i].split()))))
    return sorted(box_list)

# determines whether or not a box fits within another box


def does_fit(box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


max_boxes = 1
sub_set_list = []
largest_subsets_list = []
# generate all subsets of a set


def find_largest_sub_sets(a, b=[], lo=0):
    hi = len(a)
    if (lo == hi):
        global max_boxes
        global sub_set_list
        global largest_subsets_list
        # filters out all subsets that have a smaller length than the length of the largest subset found so far
        if len(b) >= max_boxes:
            # loops through the subset to check if the boxes fit within each other
            i = 1
            while does_fit(b[i - 1], b[i]):
                if i < len(b) - 1:
                    i += 1
                else:
                    # if the length of the new subset is larger than the length of the largest subset found so far, update the max_boxes
                    if len(b) > max_boxes:
                        # clear largest_subsets
                        largest_subsets_list = []
                        # append subset to largest_subsets_list
                        largest_subsets_list.append(b)
                        # update max_boxes
                        max_boxes = len(b)
                        #print('NEW VALUE: ', max_boxes)
                        break
                    # if not, then append the subset to the existing largest_subsets_list
                    else:
                        largest_subsets_list.append(b)
                        # print(largest_subsets)
                        break
    else:
        c = b[:]
        b.append(a[lo])
        find_largest_sub_sets(a, b, lo + 1)
        find_largest_sub_sets(a, c, lo + 1)


def main():
    box_list = read_file()
    find_largest_sub_sets(box_list)
    print('Largest Subset of Nesting Boxes')
    for largest_subset in largest_subsets_list:
        for i in range(len(largest_subset)):
            if i == len(largest_subset) - 1:
                print(largest_subset[i])
                print()
            else:
                print(largest_subset[i])


main()
