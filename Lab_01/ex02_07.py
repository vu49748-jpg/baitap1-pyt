lines = []

while True:
    s = input()
    if s == "":
        break
    lines.append(s.upper())

for line in lines:
    print(line)
