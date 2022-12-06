import numpy as np

with open('day5/input_duc.txt') as f:
    crates_input, commands_input = ''.join(f.readlines()).split("\n\n")
    f.close()

def parse_crates():
    crates_array = crates_input.split('\n')
    number_of_cols = crates_array[-1].split(' ')[-2]
    crates_array = crates_array[:len(crates_array)-1]
    stack = [list() for i in range(int(number_of_cols))]
    for index in reversed(range(len(crates_array))):
        crate_line = crates_array[index]
        column_index = 0
        for i in range(0, len(crate_line)-1,4):
            crate = crate_line[i+1]
            if not crate == ' ':
                stack[column_index].append(crate_line[i+1])
            column_index+=1
    return stack

def part1():
    # parse crates into numpy array
    stack = parse_crates()
    commands = commands_input.split('\n')
    for command in commands:
        commands_collection = command.split(' ')
        amount = int(commands_collection[1])
        prev = int(commands_collection[3])
        next = int(commands_collection[5])

        for i in range(amount):
            stack[next-1].append(stack[prev-1].pop())
    answer = ''
    for i in range(9):
        answer += stack[i].pop()
    print(answer)


def part2():
    stack = parse_crates()
    commands = commands_input.split('\n')
    for command in commands:
        commands_collection = command.split(' ')
        amount = int(commands_collection[1])
        prev = int(commands_collection[3])
        next = int(commands_collection[5])
        crates_holder = []
        for i in range(amount):
            crates_holder.append(stack[prev-1].pop())
        crates_holder.reverse()
        stack[next-1].extend(crates_holder)
    answer = ''
    for i in range(9):
        answer += stack[i].pop()
    print(answer)

part2()
