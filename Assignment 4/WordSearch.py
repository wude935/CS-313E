#  File: WordSearch.py

#  Description: This program reads in a k by k square of characters and finds pre-set words inside that square

#  Student Name: Derek Wu

#  Student UT EID: dw29924

#  Partner Name: Victor Li

#  Partner UT EID: vql83

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: September 15, 2019

#  Date Last Modified: September 16, 2019

wordSquare = []
wordsToFind = []
numRows = 0
numCols = 0
wordsFound = []

# Reads in a file of a set format and saves it to global variables


def readFile():
    global numRows
    global numCols
    try:
        # opens the file
        file = open("hidden.txt")
        with file as f:
            # adds each line of the file to list characterList
            # each element of characterList is then converted into a list of letters
            characterList = f.read().splitlines()
            characterList = [line.split() for line in characterList]
        squareSize = characterList.pop(0)
        delRow = characterList.pop(0)
        numRows = int(squareSize[0])
        numCols = int(squareSize[1])
        delRow = characterList.pop(numRows)
        delRow = characterList.pop(numRows)
        numOfWords = int(delRow[0])
        count = 0
        while(count < numOfWords):
            wordsToFind.append(characterList.pop(numRows))
            count += 1
        for lines in characterList:
            wordSquare.append(lines)
        wordSquare.pop(len(wordSquare)-1)
    except:
        print("There was an error reading the file.")

# finds the coordinates of the first letter in a given word


def findWord(word):
    realWord = word[0]
    # default values are 0,0 in case word is not found
    rowIndexOfLetter = 0
    colIndexOfLetter = 0
    row = 0
    col = 0
    notComplete = True
    found = False
    while(row < numRows and notComplete):
        while(col < numCols and notComplete):
            if(wordSquare[row][col] == realWord[0:1]):
                # if the first letter of square matches the first letter of a word in the word bank
                # finds if the word exists in the four cardinal directions
                if(checkNorth(realWord, row, col) or checkNorthE(realWord, row, col) or checkEast(realWord, row, col) or checkSouthE(realWord, row, col) or checkSouth(realWord, row, col) or checkSouthW(realWord, row, col) or checkWest(realWord, row, col) or checkNorthW(realWord, row, col)):
                    rowIndexOfLetter = row
                    colIndexOfLetter = col
                    notComplete = False
                    found = True
            col += 1
        row += 1
        col = 0
    if(rowIndexOfLetter == 0 and colIndexOfLetter == 0 and found == False):
        foundWord = (word, rowIndexOfLetter, colIndexOfLetter)
    else:
        foundWord = (word, rowIndexOfLetter+1, colIndexOfLetter+1)
    # adds word, row, and column to wordsFound list
    wordsFound.append(foundWord)

# checks if the word exists in the north direction starting from row, col


def checkNorth(word, row, col):
    found = False
    row -= 1
    exit = False
    letter = 1
    temp = 0
    wordSize = len(word)
    # checks if the letters of the row, col match the letters of the word, with all three indexes incrementing if they do match
    while (outOfBounds(row, col) == False and letter < wordSize and exit == False):
        if (wordSquare[row][col] == word[letter:letter + 1]):
            temp = 0
            # if the entire word is found found is set to true
            if (letter == wordSize-1):
                found = True
                exit = True
        else:
            exit = True
        row -= 1
        letter += 1
    return found

# checks if the word exists in the north east direction starting from row, col


def checkNorthE(word, row, col):
    found = False
    row -= 1
    col += 1
    exit = False
    letter = 1
    temp = 0
    wordSize = len(word)
    # checks if the letters of the row, col match the letters of the word, with all three indexes incrementing if they do match
    while (outOfBounds(row, col) == False and letter < wordSize and exit == False):
        if (wordSquare[row][col] == word[letter:letter + 1]):
            temp = 0
            # if the entire word is found found is set to true
            if (letter == wordSize-1):
                found = True
                exit = True
        else:
            exit = True
        row -= 1
        col += 1
        letter += 1
    return found

# checks if the word exists in the east direction starting from row, col


def checkEast(word, row, col):
    found = False
    col += 1
    exit = False
    letter = 1
    temp = 0
    wordSize = len(word)
    # checks if the letters of the row, col match the letters of the word, with all three indexes incrementing if they do match
    while (outOfBounds(row, col) == False and letter < wordSize and exit == False):
        if (wordSquare[row][col] == word[letter:letter + 1]):
            temp = 0
            # if the entire word is found found is set to true
            if (letter == wordSize-1):
                found = True
                exit = True
        else:
            exit = True
        col += 1
        letter += 1
    return found

# checks if the word exists in the southeast direction starting from row, col


def checkSouthE(word, row, col):
    found = False
    row += 1
    col += 1
    exit = False
    letter = 1
    temp = 0
    wordSize = len(word)
    # checks if the letters of the row, col match the letters of the word, with all three indexes incrementing if they do match
    while (outOfBounds(row, col) == False and letter < wordSize and exit == False):
        if (wordSquare[row][col] == word[letter:letter + 1]):
            temp = 0
            # if the entire word is found found is set to true
            if (letter == wordSize-1):
                found = True
                exit = True
        else:
            exit = True
        row += 1
        col += 1
        letter += 1
    return found

# checks if the word exists in the south direction starting from row, col


def checkSouth(word, row, col):
    found = False
    row += 1
    exit = False
    letter = 1
    temp = 0
    wordSize = len(word)
    # checks if the letters of the row, col match the letters of the word, with all three indexes incrementing if they do match
    while (outOfBounds(row, col) == False and letter < wordSize and exit == False):
        if (wordSquare[row][col] == word[letter:letter + 1]):
            temp = 0
            # if the entire word is found found is set to true
            if (letter == wordSize-1):
                found = True
                exit = True
        else:
            exit = True
        row += 1
        letter += 1
    return found

# checks if the word exists in the southwest direction starting from row, col


def checkSouthW(word, row, col):
    found = False
    row += 1
    col -= 1
    exit = False
    letter = 1
    temp = 0
    wordSize = len(word)
    # checks if the letters of the row, col match the letters of the word, with all three indexes incrementing if they do match
    while (outOfBounds(row, col) == False and letter < wordSize and exit == False):
        if (wordSquare[row][col] == word[letter:letter + 1]):
            temp = 0
            # if the entire word is found found is set to true
            if (letter == wordSize-1):
                found = True
                exit = True
        else:
            exit = True
        row += 1
        col -= 1
        letter += 1
    return found

# checks if the word exists in the west direction starting from row, col


def checkWest(word, row, col):
    found = False
    col -= 1
    exit = False
    letter = 1
    temp = 0
    wordSize = len(word)
    # checks if the letters of the row, col match the letters of the word, with all three indexes incrementing if they do match
    while (outOfBounds(row, col) == False and letter < wordSize and exit == False):
        if (wordSquare[row][col] == word[letter:letter + 1]):
            temp = 0
            # if the entire word is found found is set to true
            if (letter == wordSize-1):
                found = True
                exit = True
        else:
            exit = True
        col -= 1
        letter += 1
    return found

# checks if the word exists in the northwest direction starting from row, col


def checkNorthW(word, row, col):
    found = False
    row -= 1
    col -= 1
    exit = False
    letter = 1
    temp = 0
    wordSize = len(word)
    # checks if the letters of the row, col match the letters of the word, with all three indexes incrementing if they do match
    while (outOfBounds(row, col) == False and letter < wordSize and exit == False):
        if (wordSquare[row][col] == word[letter:letter + 1]):
            temp = 0
            # if the entire word is found found is set to true
            if (letter == wordSize-1):
                found = True
                exit = True
        else:
            exit = True
        row -= 1
        col -= 1
        letter += 1
    return found

# checks if the row and column are outside of the word square


def outOfBounds(row, col):
    if(row >= numRows or col >= numCols):
        return True
    else:
        return False


def writeOutput(wordsFound):
    # writes and creates found.txt file
    output_file = open('found.txt', 'w+')
    longest_length = 0
    for element in wordsFound:
        if len(element[0][0]) > longest_length:
            longest_length = len(element[0][0])
    for element in wordsFound:
        # first right justifies the word, then right justifies the entire output
        output_string = '%s %s %s\n' % (element[0][0].ljust(longest_length), str(
            element[1]).rjust(numCols//10 + 1), str(element[2]).rjust(numRows//10 + 1))
        output_file.write(output_string)
    output_file.close()


def main():
    readFile()
    for words in wordsToFind:
        findWord(words)
    writeOutput(wordsFound)


if __name__ == "__main__":
    main()
