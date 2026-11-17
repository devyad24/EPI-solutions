import itertools

def maximum_sum(arr):
   min_sum = max_sum = 0 

   running_sum = 0
   for running_sum in itertools.accumulate(arr):
       min_sum = min(min_sum, running_sum)
       max_sum = max(max_sum, running_sum - min_sum)
   
   return max_sum


arr = [-1]

print(maximum_sum(arr))




