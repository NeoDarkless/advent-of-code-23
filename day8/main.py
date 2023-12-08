puzzle_input = open("day8/input.txt", "r")
lines = puzzle_input.readlines()

directions = lines[0]

for line in lines:
    if line != lines[0:2]:
        node = line[0:3]
        left = line[7:10]
        right = line[12:15]
        print(node, left, right, lines.index(line))