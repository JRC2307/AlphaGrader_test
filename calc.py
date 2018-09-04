import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)

# do something with the lines array
a = 0 

for line in lines:
	a += int(line)

print(a)
