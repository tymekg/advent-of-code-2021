# easy_lengths = [2, 3, 4, 7]
easy_length_mapping = {2: 1, 3: 7, 4: 4, 7: 8}
length_mapping = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [6, 9, 0], 7: [8]}
super_digits = {1: [0, 3, 4, 7, 8, 9], 4: [8, 9], 7: [3, 8, 9, 0]}

digit_encoding = {0: 'ABCEFG', 1: 'CF', 2: 'ACDEG', 3: 'ACDFG', 4: 'BCDF', 5: 'ABDFG',
6: 'ABDEFG', 7: 'ACF', 8: 'ABCDEFG', 9: 'ABCDFG'}
digit_encoding_reverse = {}
for d in digit_encoding.keys():
    signals = digit_encoding[d]
    for s in signals:
        if not s in digit_encoding_reverse:
            digit_encoding_reverse[s] = [d]
        else:
            digit_encoding_reverse[s].append(d)

# signal_possible_mappings = {}
signal_possible_mappings_reverse = {}

signal_mapping = {}

def get_output(line):
    possible_mappings = {}
    impossible_mappings = {}
    impossible_value_if_all = {}
    impossible_value_if_not_all = {}
    impossible_value_if_none = {}

    known_encoding = {}
    decoding_map = {}

    def learn_encoding(value, digit):
        known_encoding[value] = digit
        decoding_map[digit] = value
        if not value in impossible_value_if_none:
            impossible_value_if_none[value] = []
        if len (impossible_value_if_none[value]) < len(digit):
            for c in digit:
                if not c in impossible_value_if_none[value]:
                    impossible_value_if_none[value].append(c)
        if (value == 6 and 9 in known_encoding) or (value == 9 and 6 in known_encoding):
            for c in 'abcdefg':
                if (c in known_encoding[6]) != (c in known_encoding[9]):
                # if c not in known_encoding[9]:
                    if c in impossible_mappings:
                        impossible_mappings[c].add(5)
                    else:
                        impossible_mappings[c] = [5]
                    if 2 in impossible_value_if_not_all:
                        impossible_value_if_not_all[2].append(c)
                    else:
                        impossible_value_if_not_all[2] = [c]
        if value == 5 or value == 4:
            if 9 not in known_encoding:
                if 9 not in impossible_value_if_not_all:
                    impossible_value_if_not_all[9] = []
                for c in digit:
                    impossible_value_if_not_all[9].append(c)
            if 0 not in known_encoding:
                if 0 not in impossible_value_if_all:
                    impossible_value_if_all[0] = []
                for c in digit:
                    impossible_value_if_all[0].append(c)



    def decode_digit(digit):
        if digit in decoding_map:
            return decoding_map[digit]
        def is_possible(v):
            ok = False
            if v not in impossible_value_if_all:
                ok = True
            if not ok:
                for c in impossible_value_if_all[v]:
                    if c not in digit:
                        ok = True
            if not ok:
                return False
            
            passed = False
            if v not in impossible_value_if_none:
                passed = True
            else:
                for c in impossible_value_if_none[v]:
                        if c in digit:
                            passed = True
            if not passed:
                return False
            
            if v not in impossible_value_if_not_all:
                return True
            for c in impossible_value_if_not_all[v]:
                    if c not in digit:
                        return False
            return True
        # print('output: ' + str(output))
        if (len(digit) in easy_length_mapping.keys()):
            value = easy_length_mapping[len(digit)]
            if not value in known_encoding:
                learn_encoding(value, digit)
                # known_encoding[value] = digit
        else:
            possible_values = length_mapping[len(digit)]


            possible_values = list(filter(is_possible, possible_values))
            # print('possible by rejecting impossible if all: ' + str(possible_values))
            value = -1
            for c in digit:
                impossible = impossible_mappings[c]
                possible_values = list(filter(lambda v: v not in impossible, possible_values))
                # print('possible after rejecting impossible for ' + c + ': ' + str(possible_values))
                if (len(possible_values) ==1):
                    value = possible_values[0]
                    break
                candidates = possible_mappings[c]
                # # print(candidates)
                maybe_too_restrictive_values = list(filter(lambda v: v in candidates, possible_values))
                # if len(maybe_too_restrictive_values) == 1:
                #     value = maybe_too_restrictive_values[0]
                #     break
            if value == -1:
                if (len(possible_values) != 1):
                    # print(possible_values)
                    # print("oops")
                    return -1
                value = possible_values[0]
            if value not in known_encoding:
                learn_encoding(value, digit)
        return value

    for c in 'abcdefg':
        possible_mappings[c] = set()
        impossible_mappings[c] = set()
    (patterns, output) = list(map(lambda s: s.strip(), line.split('|')))
    pdigits = patterns.split(' ')
    odigits = output.split(' ')
    easy_digits = list(filter(lambda d: len(d) in easy_length_mapping.keys(), pdigits + odigits))
    for pattern in easy_digits:
        target = easy_length_mapping[len(pattern)]
        targets = [target]
        if target in super_digits:
            targets += super_digits[target]
        for letter in pattern:
            # possible_mappings[letter].add(target)
            for t in targets:
                possible_mappings[letter].add(t)
    for r in 'abcdefg':
        if 7 in possible_mappings[r] and not 1 in possible_mappings[r]:
            signal_mapping[r] = 'A'
            for d in digit_encoding_reverse['A']:
                possible_mappings[r].add(d)
            for d in range(10):
                if 'A' not in digit_encoding[d]:
                    impossible_mappings[r].add(d)
        if 1 in possible_mappings[r]:
            # impossible_mappings[r].add(3)
            for d in [2, 5, 6]:
                if d in impossible_value_if_all:
                    impossible_value_if_all[d].append(r)
                else:
                    impossible_value_if_all[d] = [r]
            for d in [0, 1, 3, 4, 7, 8, 9]:
                if d in impossible_value_if_not_all:
                    impossible_value_if_not_all[d].append(r)
                else:
                    impossible_value_if_not_all[d] = [r]
        
    output_sum = 0
    base = 1000
    for current_output_digit in odigits:
        value = decode_digit(current_output_digit)
        retrain_attempts = 3
        while value < 0 and retrain_attempts > 0:
            for digit in pdigits + odigits:
                decode_digit(digit)
            value = decode_digit(current_output_digit)
            retrain_attempts -= 1

        if value < 0:
            raise Exception("no idea")

        output_sum += int(value * base)
        # print(output_sum)
        base /= 10
    print(output_sum)
    return output_sum

with open('day8/input.txt') as f:
    count = 0
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        count += get_output(line)
    print (count)


