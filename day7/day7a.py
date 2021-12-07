
def align_cost(dest, positions):
    moves = list(map(lambda h: max(h, dest) - min(h, dest), positions))
    total_cost =  sum(moves)
    # print("cost for " + str(dest) + ": " + str(total_cost))
    return total_cost

with open('day7/input.txt') as f:
    line = f.readline().rstrip('\n')
    crab_positions = list(map(int, line.split(',')))
    sum_of_crabs = sum(crab_positions)
    avg = round(sum_of_crabs / len(crab_positions))
    best_cost = align_cost(avg, crab_positions)
    step = 0
    best_pos = avg
    improved = True
    while (improved):
        improved =  False
        step += 1
        new_best_cost = align_cost(avg + step, crab_positions)
        if (new_best_cost < best_cost):
            improved = True
            best_cost = new_best_cost
            best_pos = avg + step
        new_best_cost = align_cost(avg - step, crab_positions)
        if (new_best_cost < best_cost):
            improved = True
            best_cost = new_best_cost
            best_pos = avg - step
    print(best_cost)
    # print(best_pos)


