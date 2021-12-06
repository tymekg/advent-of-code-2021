counter = 0;
with open('day1/input.txt') as f:
    first = int(f.readline())
    second = int(f.readline())
    third = int(f.readline())
    last_window = [first, second, third]
    while True:
        line = f.readline()
        if not line:
            break
        current_depth = int(line)
        new_window = last_window[1:]
        new_window.append(current_depth)
        # print(new_window)
        if (sum(new_window) > sum(last_window)):
            counter += 1
        last_window = new_window
print("Done:")
print(counter)