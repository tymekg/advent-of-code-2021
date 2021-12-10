opening = {')': '(', ']': '[', '}': '{', '>' : '<'}
closings = opening.keys()
points = {')': 3, ']': 57, '}': 1197, '>' : 25137}

def find_illegal(line):
    stack = []
    for c in line:
        if c in closings:
            expected_opening = opening[c]
            if len(stack) == 0:
                return c
            actual = stack.pop()
            if (actual != expected_opening):
                return c
        else:
            stack.append(c)
    return None

with open('day10/input.txt') as f:
    score = 0
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        illegal = find_illegal(line)
        if illegal != None:
            score += points[illegal]
    print(score)





