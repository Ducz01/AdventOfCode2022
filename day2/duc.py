import numpy as np

with open('day2/input_duc.txt') as f:
    data = f.read().splitlines()

rps_map = {
    'X':1,
    'Y':2,
    'Z':3,
    'A':1,
    'B':2,
    'C':3,
}

def part1():
    score = 0
    for line in data:
        p_1, p_2 = line.split(' ')
        player_1 = rps_map[p_1]
        player_2 = rps_map[p_2]

        score += player_2

        if player_1 == player_2:
            score += 3
        elif player_1 == 1 and player_2 == 3:
            pass
        elif player_1 < player_2:
            score += 6
        elif player_1 == 3 and player_2 == 1:
            score += 6
    print(score)
        
part1()

def part2():
    score = 0
    for line in data:
        p_1, p_2 = line.split(' ')
        player_1 = rps_map[p_1]
        outcome = rps_map[p_2]

        score += ((outcome-1)*3)

        if outcome == 1:
            if player_1 == 1:
                score += 3
            else:
                score += player_1-1
        elif outcome == 2:
            score += player_1
        elif outcome == 3:
            if player_1 == 3:
                score += 1
            else:
                score += player_1+1


    print(score)

part2()