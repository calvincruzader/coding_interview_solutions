data_file = open('./data/icecream_parlor_data.txt', 'r')


def icecreamParlor(m, arr):
    # Complete this function
    result = []
    for i in range(len(arr)):
        kid1 = arr[i]
        for j in range(i+1,len(arr),1):
            kid2 = arr[j]
            if kid1 + kid2 == m:
                result.append(i+1)
                result.append(j+1)

    return result


if __name__ == "__main__":
    t = int(data_file.readline().strip())

    for a0 in range(t):
        m = int(data_file.readline().strip())
        n = int(data_file.readline().strip())
        arr = list(map(int, data_file.readline().strip().split(' ')))

        result = icecreamParlor(m, arr)
        print(" ".join(map(str, result)))


