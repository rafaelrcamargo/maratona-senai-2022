"""Desafio 1 - Soma de sub-vetor"""
arr = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
MAX = 0
i = 0
while i < len(arr):
    ii = i
    SUM = 0
    while ii < len(arr):
        SUM += arr[ii]
        ii += 1
    if SUM > MAX:
        MAX = SUM
    i += 1
print(MAX)