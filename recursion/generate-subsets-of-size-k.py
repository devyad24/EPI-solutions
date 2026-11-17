def combinations(n, k):
    res = []
    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            res.append(list(partial_combination))
            return 

        num_remaining = k - len(partial_combination)
        i = offset

        while i <= n : #if n = 5 and i = 1
            directed_combinations(i+1, partial_combination + [i])
            i += 1

    directed_combinations(1, [])

    return res



print(combinations(5, 1))

     
