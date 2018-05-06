data_file = open('./data/insertionsort2_data.txt', 'r')


def insertion_sort2(n, arr):

    for running_num in range(len(arr)):
        if running_num == 0:
            continue
        last_element = arr[running_num]

        for idx in range(running_num-1, -1, -1):
            if last_element < arr[idx]:
                arr[idx+1] = arr[idx]
            elif last_element > arr[idx]:
                arr[idx+1] = last_element
                break
            if idx == 0: # and last_element > arr[idx]:
                arr[idx] = last_element
        print(" ".join(map(str, arr)))

with data_file:
    n = data_file.readline().split()
    arr = list(map(int, data_file.readline().split()))
    insertion_sort2(n, arr)