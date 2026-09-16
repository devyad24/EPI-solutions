import itertools
import random
import bisect

'''
Purpose of this code:


    The function `non_uniform_random_number_generation` takes some values and their probablities 
    to occur in some set of sample space. Now give a random number([0,1]) we need to map the rndnum
    to one of the probablities. Mapping a certain probablity isn't possible here instead we map on
    a range of probablities.

    To make that range `generate_probablity_keypairs` is useful. It generates a prefix sum 2d array
    consisting of range tuples.

    Later on `non_uniform_random_number_generation` iterates the probablity range using binary search
    to find a suitable range for randnum.

    Once a suitable range is found we fetch the index of that tuple range. We return the element of `values` 
    for that particular index.
'''

def generate_probablity_keypairs(probablities):
    running_sum = last_prefix_sum = 0.0
    prefix_sum_of_probablities = [] 

    for p in probablities:
        running_sum += p
        prefix_sum_of_probablities.append([last_prefix_sum, running_sum])
        last_prefix_sum = running_sum
    return prefix_sum_of_probablities
        
def non_uniform_random_number_generation(values, probablities):

    prefix_sum_of_probablities = generate_probablity_keypairs(probablities)

    print(f'prefix_sum_of_probablities: {prefix_sum_of_probablities}')
    low, high = 0, len(prefix_sum_of_probablities)-1
    rand_num = random.random()
    print(f'rand_num{rand_num}')
    interval_idx = -1
    while low < high:
        middle = low + high // 2
        if rand_num >= prefix_sum_of_probablities[middle][0] and rand_num < prefix_sum_of_probablities[middle][1]:
            interval_idx = middle
            break
        elif rand_num < prefix_sum_of_probablities[middle][0]:
            high -= 1
        elif rand_num > prefix_sum_of_probablities[middle][1]:
            low += 1
    return values[interval_idx]
    


print(non_uniform_random_number_generation([3,5,7,11], [0.5,0.333,0.111,0.0555]))
