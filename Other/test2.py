# generate all subsets of a set
output = False


def sub_sets(a, b, lo, target):
    global output
    hi = len(a)
    if (lo == hi):
        if (len(b) == 2 and (b[0] + b[1] == target)):
            output = True
    else:
        c = b[:]
        b.append(a[lo])
        sub_sets(a, b, lo + 1, target)
        sub_sets(a, c, lo + 1, target)


def does_sum(nums, target):
    sub_sets(nums, [], 0, target)
    return output


def main():
    print(does_sum([2, 12, 1, 5, 24, 16], 35))


main()
