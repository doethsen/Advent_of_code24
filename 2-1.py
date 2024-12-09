with open('list.txt', 'r') as file:
    lines = file.readlines()

count = 0
List = list(line.strip('\n').split(' ') for line in lines)
ints = list(list(int(item) for item in row) for row in List)
for line in ints:
        if ((all([0 < abs(line[I] - line[I+1]) <= 3 for I in range(len(line) - 1)]))) and ((all(line[I] < line[I+1] for I in range(len(line) -1))) or
            (all(line[I] > line[I+1] for I in range(len(line) -1)))):
                count = count +1

print(count)
