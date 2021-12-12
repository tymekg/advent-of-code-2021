paths = []
exits = {}

def read_line(line):
    global paths, exits
    path = line.split('-')
    paths.append(path)
    if not path[0] in exits:
        exits[path[0]] = set()
    if not path[1] in exits:
        exits[path[1]] = set()
    exits[path[0]].add(path[1])
    exits[path[1]].add(path[0])

def find_pahts_to_end(start, visited, visited_some_twice):
    global paths, exits
    if not start in exits:
        return None
    if start == 'end':
        return {'end'}
    if start[0].islower():
        new_visited = visited | {start}
    else:
        new_visited = visited
    paths_to_end = set()
    for e in exits[start]:
        if (e != 'start') and (not e in visited or not visited_some_twice):
            pte = find_pahts_to_end(e, new_visited, visited_some_twice or e in visited)
            if pte == None:
                continue
            paths_to_end |= pte
    with_start = set()
    for pte in paths_to_end:
        with_start.add(start + '-' + pte)
    # print(with_start)
    return with_start

def find_pahts_through():
    global paths, exits
    paths_through = []
    small_visited = set()


with open('day12/input.txt') as f:
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        read_line(line)

    paths_through = find_pahts_to_end('start', set(), False)
    print(len(paths_through))

