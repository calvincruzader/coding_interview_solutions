data_file = open('./../data/fib_modified_data.txt', 'r')


def fib_modified(t1, t2, n):
    memo = [0] * (n + 1)

    memo[0] = t1
    memo[1] = t2

    for i in range(2, n):
        print(memo)
        memo[i] = memo[i - 1] ** 2 + memo[i - 2]

    print(memo)
    return memo[n-1]


if __name__ == '__main__':
    t1, t2, n = data_file.readline().split()
    t1, t2, n = [int(t1), int(t2), int(n)]

    result = fib_modified(t1, t2, n)
    print(result)
