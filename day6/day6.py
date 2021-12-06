
with open('day6/input.txt') as f:
    line = f.readline().rstrip('\n')
    phases = list(map(int, line.split(',')))
    phases_count = {}
    for p in range(9):
        phases_count[p] = 0
    for p in phases:
        phases_count[p] = phases_count[p] + 1
    for day in range(256):
        new_fishes = phases_count[0]
        for p in range(1, 9):
            phases_count[p - 1] = phases_count[p]
        phases_count[6] += new_fishes
        phases_count[8] = new_fishes
    print(sum(list(phases_count.values())))

