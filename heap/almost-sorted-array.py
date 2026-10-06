import itertools
import heapq
'''
Input: 1. An almost sorted array
        2. A key 'k' which tells how far is an element from its position in its sorted version of array
Problem Statement: Given the above inputs output a sorted array
Example: 
    Input: [3,-1,2,6,4,5,8]
    Output: [-1,2,3,4,5,6,8]

'''

def sort_almost_sorted_array(nums, k):
    min_heap = []
    heapq.heapify(min_heap)
    for n in itertools.islice(nums, k):
        heapq.heappush(min_heap, n)

    for i in range(k, len(nums)):
        top = heapq.heappushpop(min_heap, nums[i])
        print(top)

    #print remaining k - 1 elements
    while min_heap:
        print(heapq.heappop(min_heap))


sort_almost_sorted_array([3,-1,2,6,4,5,8], 2)
    

