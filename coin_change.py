data_file = open('./data/coin_change_data.txt', 'r')



def get_ways(n, c):

    # bottoms up approach

    for coin in c:



if __name__ == '__main__':
    n, m = data_file.readline().split(" ")
    n, m = [int(n), int(m)]
    c = list(map(int, data_file.readline().strip().split(' ')))
    ways = get_ways(n, c)
