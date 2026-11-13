def permutations(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            res.append(A.copy())
            return

        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            directed_permutations(i+1)
            A[j], A[i] = A[i], A[j]

    res = []
    directed_permutations(0)
    return res

A = [2,3,5,7]
x = permutations(A)
print(x)
