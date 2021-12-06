depth = 0
horizontal = 0;
with open('day2/input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        (command, argument) = line.split(' ')
        value = int(argument)
        if (command == 'up'):
            depth -= value
        elif (command == 'down'):
            depth += value
        elif (command == 'forward'):
            horizontal += value
        elif (command == 'forward'):
            horizontal += value
        else:
            raise ValueError('Unexpected command: ' + command)
print(depth * horizontal)