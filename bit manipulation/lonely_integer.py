from functools import reduce

data_file = open('./../data/lonely_integer_data.txt', 'r')


def lonely_integer(a):
    return reduce((lambda x, y: x ^ y), a)


if __name__ == '__main__':
    n = int(data_file.readline().strip())
    a = list(map(int, data_file.readline().strip().split()))
    result = lonely_integer(a)
    print(result)
