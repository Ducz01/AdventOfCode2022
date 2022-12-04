with open('day4/input_duc.txt') as f:
    lines = f.readlines()

def split_sections(sections):
        return list(map(int,sections.split('-')))

def part1():
    counter = 0
    
    for line in lines:
        elve1, elve2 = list(map( split_sections,line.split(',')))
        # check if elve2 is in elve1
        if elve1[0] <= elve2[0] and elve1[1] >= elve2[1]:
            counter += 1
        # check the other way around
        elif elve2[0] <= elve1[0] and elve2[1] >= elve1[1]:
            counter += 1
    print(counter)
part1()

def part2():
    counter = 0
    for line in lines:
        elve1, elve2 = list(map( split_sections,line.split(',')))
        # wenn elve1[0] < elfe2[0] => muss auch das 2. element kleiner sein
        if elve1[0] < elve2[0] and elve1[1] < elve2[0]:
            # keine überlappung
            continue
        
        if elve2[0] < elve1[0] and elve2[1] < elve1[0]:
            # keine überlappung
            continue
        counter +=1
    print(counter)

part2()