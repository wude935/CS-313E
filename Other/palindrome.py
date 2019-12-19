longestLength = 0
def longest_palindrome(s):
    #changed
    global longestLength
    test = []
    lo = 0
    #changed
    a = list(s)
    is_palindrome(a, test, lo)
    return longestLength

def is_palindrome(a, test, lo):
    hi = len(a)
    #added
    global longestLength
    if (lo == hi):
        teststring = ''
        for i in range (len(test)):
            teststring = teststring + test[i]
        #changed
        testreverse = teststring[::-1]
        print(testreverse)
        if teststring == testreverse:
            if len(test) > longestLength:
                longestLength = len(test)
    else:
        c = test[:]
        test.append(a[lo])
        is_palindrome(a, test, lo + 1)
        is_palindrome(a, c, lo + 1)

def main():
    print(longest_palindrome('abadfadaadfs'))

main()
