from math import copysign

diagram = {}

def parse_line(line):
    pointsText = list(line.split(' -> '))
    points = list(map(lambda t: list(map(int, t.split(','))), pointsText))
    return points

def mark_point(x, y):
    if (x, y) in diagram:
        current_value = diagram[(x, y)]
        diagram[(x, y)] = current_value + 1
    else:
        diagram[(x, y)] = 1

def mark_line(start, end):
    if start[0] != end[0] and start[1] != end[1]:
        # diagonal
        length = abs(end[0] - start[0]) + 1
        step_x = copysign(1, end[0] - start[0])
        step_y = copysign(1, end[1] - start[1])
        for offset in range(length):
            mark_point(start[0] + offset * step_x, start[1] + offset * step_y)
    else:
        # horizontal or vertical
        for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
            for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                mark_point(x, y)

def count_danger():
    count = 0
    for point in diagram.values():
        if point > 1:
            count += 1
    return count


with open('day5/input.txt') as f:
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        points = parse_line(line)
        # print(points)
        mark_line(points[0], points[1])
    print(count_danger())