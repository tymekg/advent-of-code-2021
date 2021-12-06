lines = 0;
ones = {};
bits = 0;

with open('day3/input.txt') as f:
    while True:
        line = f.readline()
        if bits == 0:
            bits = len(line)
            for i in range(bits - 1):
                ones[i] = 0
        if not line:
            break
        for i in range(bits - 1):
            cbit = line[i]
            if cbit == '1':
                ones[i] += 1
        lines += 1
    gamma = '0'
    epsilon = '0'
    for i in range(bits - 1):
        if (ones[i] * 2 > lines):
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
    
    print(gamma)
    gammaVal = int(gamma, 2)
    print(gammaVal)
    epsilonVal = int(epsilon, 2)
    print (gammaVal * epsilonVal)
