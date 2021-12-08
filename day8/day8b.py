# easy_lengths = [2, 3, 4, 7]
easy_length_mapping = {2: 1, 3: 7, 4: 4, 7: 8}
length_mapping = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [6, 9], 7: [8]}
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
    output_sum = 0;
    possible_mappings = {}
    impossible_mappings = {}
    impossible_value_if_all = {}
    impossible_value_if_not_all = {}
    # impossible_value_if_none = {}
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
    

    # for input_singal in 'ABCDEEFG':
    #     possible_rewired_signals = set('abcdeefg')
    #     for d in range(10):
    #         if input_singal in digit_encoding[d]:
    #             for r in 'abcdfg':
    #                 if not d in possible_mappings[r]:
    #                     if (r in possible_rewired_signals):
    #                         possible_rewired_signals.remove(r)
    #     if len(possible_rewired_signals) == 1:
    #         rewired = possible_rewired_signals.pop()
    #         # signal_possible_mappings[rewired] = input_singal
    #         signal_possible_mappings_reverse[input_singal] = rewired
    #     else:
    #         print("lipa")

    # for s in signal_possible_mappings_reverse.keys():
    #     rewired = signal_possible_mappings_reverse[s]
    #     for d in digit_encoding_reverse[s]:
    #         # for c in digit_encoding
    #         possible_mappings[rewired].add(d)
    # for d in range(10):
        
    base = 1000
    for output in odigits:
        # print('output: ' + str(output))
        if (len(output) in easy_length_mapping.keys()):
            value = easy_length_mapping[len(output)]
        else:
            # possible_values = range(10)
            possible_values = length_mapping[len(output)]
            # print('possible by length: ' + str(possible_values))
            def is_not_impossible(v):
                ok = False
                if v not in impossible_value_if_all:
                    ok = True
                if not ok:
                    for c in impossible_value_if_all[v]:
                        if c not in output:
                            ok = True
                if not ok:
                    return False
                
                # passed = False
                # if v not in impossible_value_if_none:
                #     passed = True
                # else:
                #     for c in impossible_value_if_none[v]:
                #             if c in output:
                #                 passed = True
                # if not passed:
                #     return False
                
                if v not in impossible_value_if_not_all:
                    return True
                for c in impossible_value_if_not_all[v]:
                        if c not in output:
                            return False
                return True


            possible_values = list(filter(is_not_impossible, possible_values))
            # print('possible by rejecting impossible if all: ' + str(possible_values))
            value = -1
            for c in output:
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
                if (len(possible_values) > 1):
                    print(possible_values)
                    print("oops")
                value = possible_values[0]
        output_sum += int(value * base)
        # print(output_sum)
        base /= 10
    print(output_sum)
    return output_sum

with open('day8/test.txt') as f:
    count = 1
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        count += get_output(line)
    print (count)


