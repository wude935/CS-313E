def sortPancakes(stack):
    stackLowRange = 0
    largestNum = 0
    largestNumIndex = -1
    while stackLowRange != len(stack):
        # finds the largest number not yet placed
        for numIndex in range(stackLowRange, len(stack)):
            if stack[numIndex] > largestNum:
                largestNum = stack[numIndex]
                largestNumIndex = numIndex
        # flips pancakes so that the largest is on the bottom
        flippedStack = stack[stackLowRange:largestNumIndex + 1]
        flippedStack.reverse()
        sortedStack = stack[:stackLowRange]
        print('sortedStack', sortedStack)
        print('flippedStack', flippedStack)
        sortedStack.extend(flippedStack)
        stack = sortedStack
        print('flipped to:', stack)
        # update stackLowRange
        stackLowRange += 1   
    print(stack)
    return stack

sortPancakes([1,2,3])
