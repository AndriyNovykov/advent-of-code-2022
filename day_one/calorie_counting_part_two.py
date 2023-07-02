input_file = open("input.txt", "r")
lines = input_file.readlines()

list = []

total = 0
for line in lines:
    if line == "\n":
        list.append(total)
        total = 0
    else:
        total += int(line)

list.append(total)

list.sort()
list.reverse()

total = 0
for i in range(3):
    total += list[i]

print(total)
