def memo_f(n, memo):
    memoLength = len(memo)
    # if n == 0 or n == 1:
    #     return memo[n]
    if n >= memoLength and n > 1:
        newValue = 2 * memo_f(n - 1, memo) - memo_f(n - 2, memo)
        memo.append(newValue)
        print('memo', memo)
        return newValue
    else:
        return memo[n]


def main():
    memo = [0, 1]
    for i in range(100):
        print(i, ' ', memo_f(i, memo))
    print()


main()
