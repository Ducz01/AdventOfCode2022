with open('day7\input_duc.txt') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.subdirs = []

root = Dir('/', None)
current_dir = root

for commandline in data:
    commandparts = commandline.split(' ')
    if commandparts[0] == '$':
        if commandparts[1] == 'cd':
            if commandparts[2] == '/':
                
                current_dir=root
            elif commandparts[2] == '..':
                current_dir = current_dir.parent
            else:
                new_dir = commandparts[2]
                subdir = Dir(new_dir, current_dir)
                current_dir.subdirs.append(subdir)
                current_dir = subdir
    elif commandparts[0] == 'dir':
        continue
    else:
        size = int(commandparts[0])
        current_dir.size += size
sizes = []
def calc_size(dir):
    for subdir in dir.subdirs:
        dir.size += calc_size(subdir)
    sizes.append(dir.size)
    return dir.size
calc_size(root)
    
def part1():
    print(sum([item for item in sizes if item <= 100_000]))

def part2():
    print(min([item for item in sizes if 70000000-max(sizes) + item > 30000000]))
part2()