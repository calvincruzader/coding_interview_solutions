import heapq

my_heap = []
heapq.heappush(my_heap, 8)
heapq.heappush(my_heap, 5)
heapq.heappush(my_heap, 79)

print(heapq.heappop(my_heap))