with open('day6\input_duc.txt') as f:
    data = f.readline()
def get_marker_pos(dis):
    temp = []
    for i in range(len(data)):
        temp.append(data[i])
        if len(temp) > dis:
            temp.pop(0)
            if len(set(temp)) >= dis:
                print(i+1)
                break
get_marker_pos(4)
get_marker_pos(14)