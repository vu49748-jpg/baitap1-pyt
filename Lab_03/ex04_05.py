def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhap so: "))

if la_so_nguyen_to(n):
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")
