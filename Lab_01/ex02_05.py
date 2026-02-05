hours = float(input("Nhap so gio lam viec: "))
rate = float(input("Nhap luong moi gio: "))

if hours <= 44:
    salary = hours * rate
else:
    salary = 44 * rate + (hours - 44) * rate * 1.5

print("Luong thuc linh:", salary)
