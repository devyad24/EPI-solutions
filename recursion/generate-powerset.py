def generate_powerset(arr):
    powerset = []

    def directed_powerset(i, curr_subset):
        if i == len(arr):
            powerset.append(list(curr_subset))
            return

        directed_powerset(i+1, curr_subset)
        directed_powerset(i+1, curr_subset + [arr[i]])

    directed_powerset(0, [])
    return powerset

s = [0,1,2]
print(generate_powerset(s))

