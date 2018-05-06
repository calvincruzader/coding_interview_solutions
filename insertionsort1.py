data_file = open('./data/insertionsort1_data.txt', 'r')


def insertion_sort1(n, arr):
    last_element = arr[len(arr)-1]
    for idx in range(len(arr)-1, -1, -1):
        if last_element < arr[idx]:
            arr[idx+1] = arr[idx]
            print(" ".join(map(str,arr)))
        if last_element > arr[idx]:
            arr[idx+1] = last_element
            print(" ".join(map(str,arr)))
            break
        if idx == 0:
            arr[idx] = last_element
            print(" ".join(map(str, arr)))


with data_file:
    n = data_file.readline().split()
    arr = list(map(int, data_file.readline().split()))
    insertion_sort1(n, arr)