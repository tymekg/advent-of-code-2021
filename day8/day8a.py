easy_lengths = [2, 3, 4, 7]

def count_easy_digits(line):
    (patterns, output) = list(map(lambda s: s.strip(), line.split('|')))
    odigits = output.split(' ')
    easy_digits = list(filter(lambda d: len(d) in easy_lengths, odigits))
    return len(easy_digits)

with open('day8/input.txt') as f:
    count = 0
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        count += count_easy_digits(line)
    print (count)


