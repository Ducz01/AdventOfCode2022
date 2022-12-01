import numpy as np

with open('day1/input_duc.txt') as f:
    data = f.read().splitlines()

def part1():
    calories = {}
    elve_index = 0
    for item in data:
        if item == '':
            elve_index +=1
            continue
        if elve_index in calories:
            calories[elve_index] += int(item)
        else:
            calories[elve_index] = int(item)

    highest_calorie_elve = max(calories, key=lambda k: calories[k])
    print(calories[highest_calorie_elve])

# part 2
def part2():
    calories = {}
    total_calories = 0
    
    elve_index = 0
    for item in data:
            if item == '':
                elve_index +=1
                continue
            if elve_index in calories:
                calories[elve_index] += int(item)
            else:
                calories[elve_index] = int(item)

    for i in range(3):
        

        highest_calorie_elve = max(calories, key=lambda k: calories[k])
        total_calories += calories[highest_calorie_elve]
        print(calories[highest_calorie_elve])
        del calories[highest_calorie_elve]

    print(total_calories)
part2()