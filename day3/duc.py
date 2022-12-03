with open('day3/input_duc.txt') as f:
    data = f.read().splitlines()

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def part1():
    false_items = ''
    for line in data:
        part1 = line[:int(len(line)/2)]
        part2 = line[int(len(line)/2):]
        for char in part1:
            if char in part2:
                false_items+=char
                break
                
    sum =0 
    print(false_items)
    for char in false_items:
        sum += alphabet.find(char)+1
    print(sum)

# part1()

def part2():
    sum = 0
    for i in range(0, len(data), 3):
        print(i)
        elve1 = data[i]
        elve2 = data[i+1]
        elve3 = data[i+2]

        for char in elve1:
            if char in elve2 and char in elve3:
                sum += alphabet.find(char)+1
                break
    print(sum)
part2()