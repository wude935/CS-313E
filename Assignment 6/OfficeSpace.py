#  File: OfficeSpace.py

#  Description: This program reads in the input for various different office spaces and assigns office locations for each employee

#  Student Name: Derek Wu

#  Student UT EID:

#  Partner Name: Victor Li

#  Partner UT EID: vql83

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/22/19


# Reads in the file and creates a list for each test case
def readFile():
    current_line = 1
    test_case_list = []
    with open('office.txt', 'r') as file:
        file_list = file.read().splitlines()
    # adds all test cases to test_case_list
    while current_line < len(file_list):
        test_case_length = 0
        test_case = []
        # adds dimensions of office to test_case
        test_case.append([int(line)
                          for line in file_list[current_line - 1].split()])
        test_case_length = int(file_list[current_line]) + 1
        # adds all the employee requests to the test_case
        for i in range(test_case_length):
            test_case.append(
                [line for line in file_list[current_line + i].split()])
        test_case_list.append(test_case)
        current_line += test_case_length + 1
    return test_case_list

# Goes through a test case and creates an exmpty 2d matrix
# Creates an empty 2d matrix of 0s and adds 1 for each employee that wants the space


def eachTestCase(testCase):
    print(testCase)
    dimensions = testCase.pop(0)
    temp = testCase.pop(0)
    length = dimensions[0]
    height = dimensions[1]
    totalArea = length*height
    contestedArea = 0
    employeeList = []
    totalGuaranteedArea = 0
    tempLength = length+1
    tempHeight = height+1
    # creates the officespace matrix based on the length and width of the office coordinates
    officeSpace = [[0] * tempLength for i in range(tempHeight)]
    # if a employee wants a squarefoot, increment the value of element in the officespace matrix by 1
    for names in testCase:
        x1 = int(names[1])
        x2 = int(names[3])
        y1 = int(names[2])
        y2 = int(names[4])
        while x1 < x2:
            while(y1 < y2):
                officeSpace[y2][x1] += 1
                y2 -= 1
            x1 += 1
            y2 = int(names[4])
    # counts the number of elements in the officespace matrix that is larger than 1 to determine the contested area
    for x in range(len(officeSpace)-1):
        for y in range(len(officeSpace[x])-1):
            if officeSpace[x][y] > 1:
                contestedArea += 1
    # loops through the names and then through the officespace matrix to find to the guranteedarea and totalguranteed area for every employee
    for names in testCase:
        name = names[0]
        x1 = int(names[1])
        x2 = int(names[3])
        y1 = int(names[2])
        y2 = int(names[4])
        guaranteedArea = 0
        while x1 < x2:
            while(y1 < y2):
                if(not officeSpace[y2][x1] > 1):
                    guaranteedArea += 1
                    totalGuaranteedArea += 1
                y2 -= 1
            x1 += 1
            y2 = int(names[4])
        employeeList.append((name, guaranteedArea))

    # for lines in officeSpace:
    #     print(lines)

    # calculates unallocated area
    unallocatedArea = totalArea - contestedArea - totalGuaranteedArea
    # prints the results
    print("Total " + str(totalArea))
    print("Unallocated " + str(unallocatedArea))
    print("Contested " + str(contestedArea))
    for names in employeeList:
        print(str(names[0]) + " " + str(names[1]))
    print("")


def main():
    testCases = readFile()
    for cases in testCases:
        eachTestCase(cases)


if __name__ == "__main__":
    main()
