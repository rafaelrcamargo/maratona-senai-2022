"""
Desafio 1 - Soma de sub-vetor
"""

# Initial array
arr = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

# Max sum of sub-array list
MAX = 0

# Iterator
i = 0
while i < len(arr):
    # Sub array sum
    SUM = 0

    # Subiterator
    ii = i
    while ii < len(arr):
        SUM += arr[ii]
        ii += 1

    # Comparison
    if SUM > MAX:
        MAX = SUM
    i += 1

# Result
print(MAX)
