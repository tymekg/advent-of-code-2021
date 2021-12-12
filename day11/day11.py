energy_map = {}
height = 0
width = 0

def get_energy(x, y):
    global energy_map
    if x < 0 or x >= width or y < 0 or y >= height:
        return 0
    return int(energy_map[y][x])


def next_step():
    flashed = set()
    def increase_level(x, y):
        if x < 0 or x >= width or y < 0 or y >= height:
            return
        new_level = energy_map[(x, y)] + 1
        energy_map[(x, y)] = new_level
        if new_level == 10 and not (x, y) in flashed:
            flashed.add((x,y))
            for nx in [-1, 0, 1]:
                for ny in [-1, 0, 1]:
                    if (nx != 0 or ny != 0):
                        increase_level(x + nx, y + ny)
    for x in range(width):
        for y in range(height):
            increase_level(x, y)
    for f in flashed:
        energy_map[f] = 0
    return len(flashed)

with open('day11/input.txt') as f:
    flashes = 0
    x = 0
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        x = 0
        for c in line:
            energy_map[(x, height)] = int(c)
            x += 1
        height += 1
    width = x
    flashes = 0
    for s in range(100):
        step_flashes = next_step()
        flashes += step_flashes
    print(flashes)





