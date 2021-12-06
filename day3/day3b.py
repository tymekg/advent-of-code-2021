lines = 0;
bits = 0;
reportLines = [];

def filterReport(reportLines, mostCommon = True):
    checkPosition = 0
    while (len(reportLines) > 1):
        # print("lines:")
        # print(reportLines)
        ones = 0;
        for l in reportLines:
            if l[checkPosition] == '1':
                ones += 1
        if (ones * 2 < len(reportLines)) == mostCommon:
            goodBit = '0'
        else:
            goodBit = '1'
        reportLines = list(filter(lambda line: line[checkPosition] == goodBit, reportLines))
        checkPosition += 1
    return int(reportLines[0], 2)

with open('day3/input.txt') as f:
    while True:
        line = f.readline().rstrip('\n')
        if bits == 0:
            bits = len(line)
        if not line:
            break
        reportLines.append(line)
    checkPosition = 0

    # while (len(reportLines) > 1):
    #     print("lines:")
    #     print(reportLines)
    #     ones = 0;
    #     for l in reportLines:
    #         if l[checkPosition] == '1':
    #             ones += 1
    #     if (ones * 2 < len(reportLines)):
    #         goodBit = '0'
    #     else:
    #         goodBit = '1'
    #     reportLines = list(filter(lambda line: line[checkPosition] == goodBit, reportLines))
    #     checkPosition += 1
    # oxygen = int(reportLines[0], 2)
    oxygen = filterReport(reportLines)
    print(oxygen)
    co2 = filterReport(reportLines, False)
    print(co2)
    print(co2 * oxygen)


