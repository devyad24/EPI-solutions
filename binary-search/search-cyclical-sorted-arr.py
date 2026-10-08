'''
given a cyclical sorted array, find the min of the array in O(logn) time
'''
def search_cyclical_sorted_array(n):
    l,h = 0,len(n)-1
    m = 0

    while l<h:
        m = (l + h) // 2

        if n[m] < n[h]:
            h = m #our answer could be at previous h so keep it in bound
        else:
            l = m + 1

    return l

n = [379, 478, 550, 103, 203, 220, 234, 279, 368]
print(search_cyclical_sorted_array(n))
