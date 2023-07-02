input_file = open("input.txt", "r")
lines = input_file.readlines()

total = 0
max = 0
for line in lines:
    if line == "\n":
        if max < total:
            max = total
        total = 0
    else:
        total += int(line)

if max < total:
    max = total

print(max)
    