data_file = open('./data/strong_password_data.txt', 'r')


def get_total(a, b):
    smallest_num_in_b = min(b)

    # get all the factors of the smallest num in B
    factor_list = []
    for num in range(1, smallest_num_in_b + 1):
        if smallest_num_in_b % num == 0:
            factor_list.append(num)

    print(factor_list)

    # remove all the factors that aren't factors of ALL the items in B
    factor_to_remove = set()
    for num in b:
        for factor in factor_list:
            # print("{} {} ".format(num, factor))
            if num % factor != 0:
                factor_to_remove.add(factor)

    for num_to_remove in factor_to_remove:
        factor_list.remove(num_to_remove)

    print(factor_list)

    # remove all the factors that don't have an item in A as a factor
    factor_to_remove = set()
    for num in a:
        for factor in factor_list:
            if factor % num != 0:
                factor_to_remove.add(factor)

    for num_to_remove in factor_to_remove:
        factor_list.remove(num_to_remove)

    print(factor_list)

    result = len(factor_list)
    return result


with data_file:
    nm = data_file.readline().split()
    n, m = nm[0], nm[1]
    a = list(map(int, data_file.readline().rstrip().split()))
    b = list(map(int, data_file.readline().rstrip().split()))

    total = get_total(a, b)
    print(total)