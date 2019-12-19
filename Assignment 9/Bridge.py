
#  File: Bridge.py

#  Description:  This program will calculate the quickest time it takes n number of people to cross a bridge by utilizing two different strategies

#  Student Name:  Victor Li

#  Student UT EID:  vql83

#  Partner Name: Derek Wu

#  Partner UT EID: dw29924

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: October 3, 2019

#  Date Last Modified: October 4, 2019


def read_file():
    file_name = 'bridge.txt'
    # open file bridge.txt for reading
    with open(file_name, 'r') as file:
        file_list = file.read().splitlines()
    test_case_list = []
    line = 2
    while line < len(file_list):
        test_case_list.append(
            [int(number) for number in file_list[line: line + int(file_list[line]) + 1]])
        line = line + int(file_list[line]) + 2
    return test_case_list


# takes the the fastest person (a) and another person (b) and calculates the time it takes for them to cross the bridge
# a < b
def strategy_one(a, b):
    # 1. add the time it takes a and b to cross the bridge together (to safety)
    # 2. add the time it takes a to cross the bridge (to danger)
    return b + a


# takes two fastest people (a and b) and two other people (c and d) and calculates the time it takes for them to cross the bridge
# a < b < c < d
def strategy_two(a, b, c, d):
    # 1. add the time it takes a and b to cross the bridge together (to safety)
    # 2. add the time it takes a to cross the bridge (to danger)
    # 3. add the time it takes c and d to cross the bridge together (to safety)
    # 4. add the time it takes b to cross the bridge (to danger)
    return b + a + d + b


def use_strategy_one(test_case, sorted_test_case):
    time = 0
    if (test_case[0] > 1):
        # loops backwards from the end of sorted_test case until there are only two elements left
        # plugs in the largest elements of sorted_test_case as b
        index = len(sorted_test_case) - 1
        while index > 1:
            # adds the result of strategy one to the total time
            time = time + \
                strategy_one(sorted_test_case[0], sorted_test_case[index])
            index -= 1
        # adds the time it takes for the last two people to cross the bridge (to safety)
        time = time + sorted_test_case[1]
    else:
        time += sorted_test_case[0]
    return time

# uses strategy two to calculate the total time


def use_strategy_two(test_case, sorted_test_case):
    time = 0
    # if sorted_test_case has an even number of people, run strategy_two for all the people until there are two people left
    if (test_case[0] % 2 == 0 and test_case[0] > 1):
        # loops backwards from the end of sorted_test case until there are only two elements left
        # plugs in the largest two elements of sorted_test_case strategy_two as c and d
        index = len(sorted_test_case) - 1
        while index > 1:
            # adds the result of strategy two to the total time
            time = time + strategy_two(sorted_test_case[0], sorted_test_case[1],
                                       sorted_test_case[index - 1], sorted_test_case[index])
            index -= 2
        # adds the time it takes the two fastest people to cross the bridge (to safety)
        time = time + sorted_test_case[1]
    # if sorted_test_case has an odd number of people, run strategy_two for all people until there are three people left
    elif test_case[0] > 1:
        # loops backwards from the end of sorted_test case until there are only two elements left
        # plugs in the largest two elements of sorted_test_case strategy_two as c and d
        index = len(sorted_test_case) - 1
        while index > 2:
            # adds the result of strategy two to the total time
            time = time + strategy_two(sorted_test_case[0], sorted_test_case[1],
                                       sorted_test_case[index - 1], sorted_test_case[index])
            index -= 2
        # adds the time it takes the last three people to cross the bridge (to safety)
        time = time + sorted_test_case[2] + \
            sorted_test_case[0] + sorted_test_case[1]
    else:
        time += sorted_test_case[0]
    return time


# calculates the shortest time for a group of people to cross the bridge
def calculate(test_case):
    # sorts the test_case
    sorted_test_case = sorted(test_case[1:])
    strategy_one_result = use_strategy_one(test_case, sorted_test_case)
    strategy_two_result = use_strategy_two(test_case, sorted_test_case)
    # chooses between the results strategy_one and strategy_two
    if strategy_one_result > strategy_two_result:
        print(strategy_two_result)
    else:
        print(strategy_one_result)
    print("")


def main():
    test_case_list = read_file()
    for test_case in test_case_list:
        calculate(test_case)


if __name__ == "__main__":
    main()
