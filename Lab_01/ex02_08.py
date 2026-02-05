values = input("Nhap chuoi nhi phan (phan tach boi dau phay): ").split(",")

result = []

for v in values:
    if int(v, 2) % 5 == 0:
        result.append(v)

print(",".join(result))
