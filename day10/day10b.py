opening = {')': '(', ']': '[', '}': '{', '>' : '<'}
closings = opening.keys()
closing = {v: k for k, v in opening.items()}
points = {')': 3, ']': 57, '}': 1197, '>' : 25137}
incomplete_points = {')': 1, ']': 2, '}': 3, '>' : 4}

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

def get_incomplete_score(line):
    stack = []
    for c in line:
        if c in closings:
            expected_opening = opening[c]
            if len(stack) == 0:
                return c
            actual = stack.pop()
            if (actual != expected_opening):
                return 0
        else:
            stack.append(c)
    score = 0
    while len(stack) > 0:
        next_missing = closing[stack.pop()]
        score = score * 5 + incomplete_points[next_missing]
    return score

with open('day10/input.txt') as f:
    scores = []
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        score = get_incomplete_score(line)
        if score > 0:
            scores.append(score)
    print(scores)
    scores.sort()
    print(scores)
    print(scores[len(scores)//2])





