import math


def read_file():
    #file_name = 'Assignment 8/work.txt'
    file_name = 'work.txt'
    # open file work.txt for reading
    with open(file_name, 'r') as file:
        file_list = file.read().splitlines()
    test_case_list = []
    for i in range(1, 1 + int(file_list[0])):
        test_case_list.append(list(map(int, file_list[i].split())))
    return test_case_list

# returns the number of lines of code that will be created given k and a potential_v value
def equation(k, potential_v):
    p = 0
    while potential_v//(k**p) > 0:
        p += 1
    sum = 0
    for i in range(p + 1):
        sum = sum + potential_v//(k**i)
    result = sum
    return result


# returns v
def find_v(test_case):
    n = test_case[0]
    k = test_case[1]
    # creates a list of values from 1 to n
    search_list = list(range(1, n + 1))
    low_index = 0
    high_index = len(search_list) - 1
    # loops through the search_list, plugging each value in the list in the equation
    while (low_index <= high_index):
        mid_index = (low_index + high_index) // 2
        result = equation(k, search_list[mid_index])
        # print('potential_v', search_list[mid_index])
        # print('result', result)
        # if the result from the equation is equal to n, return the v value
        if n == result:
            #print('ANSWER', search_list[mid_index])
            return search_list[mid_index]
        # if the result from the equation is less than n, make the upper half of the search_list the new search_list
        elif n > result:
            low_index = mid_index + 1
        # if the result from the equation is larger than n, make the lower half of the search_list the new search_list
        elif n < result:
            high_index = mid_index - 1
            less_mid_index_result = equation(k, search_list[mid_index -1])
            if less_mid_index_result < n:
                #print('ANSWER IS', search_list[mid_index])
                return search_list[mid_index]
                
def main():
    test_case_list = read_file()
    for test_case in test_case_list:
        print(find_v(test_case))

main()
