def permute(a, lo):
    hi = len(a)
    if (lo == hi):
        print(a)
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute(a, lo + 1)
            a[lo], a[i] = a[i], a[lo]


def q1(letters, envelope, lo):
    hi = len(letters)
    if (lo == hi):
        print(envelope)
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute(a, lo + 1)
            a[lo], a[i] = a[i], a[lo]


def q2(a, lo):
    hi = len(a)
    if (lo == hi):
        for i in range(len(a)):
            if (a[i] == 'A' and a[i + 1] == 'B') or (a[i] == 'B' and a[i + 1 == 'A']):
                if (not (a[i] == 'C' and a[i + 1] == 'D') or not (a[i] == 'D' and a[i + 1 == 'C'])):
                    print(a)
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute(a, lo + 1)
            a[lo], a[i] = a[i], a[lo]


def main():
    q2(['a', 'b', 'c', 'd', 'e'], 0)


main()
