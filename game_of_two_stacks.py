data_file = open('./data/game_of_two_stacks_data.txt', 'r')

g = data_file.readline()


def two_stacks(x, a, b):
    x = int(x)
    stack_a = []
    stack_b = []

    for idx in range(len(a) - 1, -1, -1):
        stack_a.append(a[idx])

    for idx in range(len(b) - 1, -1, -1):
        stack_b.append(b[idx])

    max_deletions = 0
    val2 = 0
    for j in range(len(b)):
        val2 += b[j]
        if val2 > x:
            break
        max_deletions += 1

    value = 0
    running_deletions_a = 0
    for i in range(len(a)):
        # checks against x
        value += a[i]
        if value > x:
            break
        running_deletions_a += 1

        value_from_b = 0
        running_deletions_b = 0
        for j in range(len(b)):
            value_from_b += b[j]
            if value + value_from_b > x:
                break
            running_deletions_b += 1

        running_deletions = running_deletions_b + running_deletions_a
        if running_deletions > max_deletions:
            max_deletions = running_deletions

    return max_deletions


for _ in range(int(g)):
    n, m, x = data_file.readline().split()
    a = list(map(int, data_file.readline().split()))
    b = list(map(int, data_file.readline().split()))

    result = two_stacks(x, a, b)
    print(str(result))
