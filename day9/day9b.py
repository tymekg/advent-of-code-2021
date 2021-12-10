import string
map = []
height = 0
width = 0

def get_depth(x, y):
    global map
    if x < 0 or x >= width or y < 0 or y >= height:
        return 10
    return int(map[y][x])

def get_basin(x, y, basin):
    global width, height
    include_plateau = True
    current = get_depth(x, y)
    if current >= 9:
        return None
    neighbours = [(x -1, y), (x +1, y), (x, y -1), (x, y+1)]
    neighbours = list(filter(lambda p: p not in basin and p[0] >= 0 and p[0] < width and p[1] >=0 and p[1] < height, neighbours))
    # for nb in neighbours:
    #     if current >= get_depth(nb[0], nb[1]):
    #         return None
    current_basin = [(x, y)] + basin
    for nb in neighbours:
        nb_basin = get_basin(nb[0], nb[1], current_basin)
        if nb_basin != None:
            current_basin = current_basin + nb_basin
    basin = list(set(current_basin))
    for p in basin:
        # map[p[1]][p[0]] = '9' # prevent reuse in further basins
        map[p[1]] = map[p[1]][:p[0]] + '9' + map[p[1]][p[0]+1:]
    return basin
        
def get_basin_size(basin):
    return len(basin)
    # size = 0
    # for b in basin:
    #     size += get_depth(b[0], b[1])
    # print(str(basin) + ' = ' + str(size))
    # return size

def print_basin(basin):
    global width, height
    for y in range(height):
        for x in range(width):
            if (x, y) in basin:
                print('#', end='')
            else:
                print('·', end='')
        print('')


def print_basins(basins, depths=False):
    global width, height
    markers = string.ascii_uppercase + string.ascii_lowercase 
    seamap = ['·' *width ] * height
    for b in range(len(basins)):
        basin = basins[b]
        for p in basin:
            if depths:
                marker = str(get_depth(p[0], p[1]))
            else:
                marker = markers[b % len(markers)]
            seamap[p[1]] = seamap[p[1]][:p[0]] + marker + seamap[p[1]][p[0]+1:]
    for y in range(height):
        for x in range(width):
                print(seamap[y][x], end='')
        print('')

with open('day9/input.txt') as f:
    count = 0
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        map.append(line)
    height = len(map)
    width = len(map[0])
    sizes = []
    basins = []
    for y in range(height):
        for x in range(width):
            basin = get_basin(x, y, [])
            if basin != None:
                size = get_basin_size(basin)
                sizes.append(size)
                basins.append(basin)
                # print_basin(basin)
                # print('size = ' + str(size) + '\n')
    sizes.sort(reverse=True)
    basins.sort(key=len, reverse=True)
    print_basins(basins)
    print(sizes)
    print_basins(basins[:3], depths=True)
    print(sizes[0] * sizes[1] * sizes[2])



