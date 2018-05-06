data_file = open('./data/missing_numbers_data.txt', 'r')

def missingNumbers(arr, brr):
    # Complete this function

    a_dict = dict()
    b_dict = dict()

    for b_num in brr:
        if b_dict.get(b_num) is None:
            b_dict[b_num] = 1
        else:
            b_dict[b_num] += 1

    for a_num in arr:
        if a_dict.get(a_num) is None:
            a_dict[a_num] = 1
        else:
            a_dict[a_num] += 1

    a_keys = a_dict.keys()
    b_keys = a_dict.keys()
    unique_keys = list(set(list(a_keys - b_keys) + list(b_keys - a_keys)))

    all_keys = set(list(a_keys) + list(b_keys))

    missing_frequencies = []
    for key in all_keys:
        if a_dict[key] and b_dict[key] and a_dict[key] != b_dict[key]:
            missing_frequencies.append(key)

    result = sorted((unique_keys + missing_frequencies))

    return result


if __name__ == "__main__":
    n = int(data_file.readline().strip())
    arr = list(map(int, data_file.readline().strip().split(' ')))
    m = int(data_file.readline().strip())
    brr = list(map(int, data_file.readline().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print (" ".join(map(str, result)))
