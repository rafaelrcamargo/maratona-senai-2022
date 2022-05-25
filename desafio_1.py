"""
Desafio 1 - Soma de sub-vetor
"""

arr = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

MAX = 0

i = 0
while i < len(arr):
    try:
        SUB = arr[i] + arr[i + 1]
        if SUB > MAX:
            MAX = SUB
    except:
        if arr[i] > MAX:
            MAX = SUB
    i += 1

print(MAX)
