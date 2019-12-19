# This function computes all permutations
def permute(a, lo):
    hi = len(a)
    if (lo == hi and formed(a)):
        print(''.join(i for i in a))
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute(a, lo + 1)
            a[lo], a[i] = a[i], a[lo]


def formed(a):
    checksum = 0
    for parentheses in a:
        if parentheses == '(':
            checksum += 1
        elif parentheses == ')':
            checksum -= 1
        if (checksum < 0):
            return False
    return True


def generate_parentheses(n):
    shell = []
    for i in range(n):
        shell.append('(')
        shell.append(')')
    permute(shell, 0)


def main():
    generate_parentheses(3)


main()
