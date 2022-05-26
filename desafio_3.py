"""
Desafio 3 - Elementar!
"""
T = int(input())

MAIN_COUNT = []

I = 0
while I < T:
    N = int(input())
    SEQ = list(filter(None, input().split(" ")))
    split = [int(x) for x in SEQ]

    COUNT = 0

    II = 0
    while II < len(split):
        NEW = II - 1
        OLD = II

        while split[OLD] < split[NEW] and NEW > -1:
            split.insert(NEW, split.pop(OLD))
            OLD = NEW
            NEW = NEW - 1
            COUNT += 1

        II += 1

    MAIN_COUNT.append(COUNT)

    I += 1

print()
for count in MAIN_COUNT:
    print(count)
