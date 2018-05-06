data_file = open('./data/equal_stacks_data.txt', 'r')


def equal_stacks(h1, h2, h3):

    stack1, stack2, stack3 = [], [], []
    height1, height2, height3 = 0, 0, 0

    for i in range(len(h1)-1, -1, -1):
        height1 += h1[i]
        stack1.append(h1[i])

    for i in range(len(h2)-1, -1, -1):
        height2 += h2[i]
        stack2.append(h2[i])

    for i in range(len(h3)-1, -1, -1):
        height3 += h3[i]
        stack3.append(h3[i])

    while height1 != height2 or height2 != height3 or height1 != height3:
        # check the tallest height and pop it
        tallest = max([height1, height2, height3])
        if tallest == height1: height1 -= stack1.pop()
        elif tallest == height2: height2 -= stack2.pop()
        else: height3 -= stack3.pop()

    print("{} {} {}".format(height1, height2, height3))
    return height1


if __name__ == '__main__':
    n1, n2, n3 = data_file.readline().split()

    h1 = list(map(int, data_file.readline().split()))
    h2 = list(map(int, data_file.readline().split()))
    h3 = list(map(int, data_file.readline().split()))

    result = equal_stacks(h1, h2, h3)
    print(result)

