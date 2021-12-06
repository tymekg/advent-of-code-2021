last_depth = -1
counter = -1;
with open('day1/input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        current_depth = int(line)
        # print (current_depth)
        if (current_depth < 0):
            print("err")
        if (current_depth > last_depth):
            counter += 1
        last_depth = current_depth
print("Done:")
print(counter)