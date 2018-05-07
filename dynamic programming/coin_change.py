data_file = open('./../data/coin_change_data.txt', 'r')


def get_ways(n, c):
    # bottoms-up approach

    combinations = [0] * (n + 1)
    combinations[0] = 1
    c.sort()
    for coin in c:
        print("coin: {}".format(coin))
        for i in range(1, len(combinations), 1):
            if i - coin >= 0:
                combinations[i] += combinations[i - coin] # be careful! with python wrapping
            print(combinations)
        print()

    return combinations[n]


if __name__ == '__main__':
    n, m = data_file.readline().split(" ")
    n, m = [int(n), int(m)]
    c = list(map(int, data_file.readline().strip().split(' ')))
    ways = get_ways(n, c)
    print(str(ways))