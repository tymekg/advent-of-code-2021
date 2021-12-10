
map = []
height = 0
width = 0

def get_depth(x, y):
    global map
    if x < 0 or x >= width or y < 0 or y >= height:
        return 10
    return int(map[y][x])

with open('day9/test.txt') as f:
    count = 0
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        map.append(line)
    height = len(map)
    width = len(map[0])
    risk = 0
    for y in range(height):
        for x in range(width):
            current = get_depth(x, y)
            if current < get_depth(x -1, y) and current < get_depth(x +1, y) and current < get_depth(x, y -1) and current < get_depth(x, y+1):
                risk += 1 + current

    print(risk)



