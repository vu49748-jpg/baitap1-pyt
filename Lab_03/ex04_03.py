def la_so_chan(n):
    return n % 2 == 0

n = int(input("Nhap so: "))

if la_so_chan(n):
    print("Day la so chan")
else:
    print("Day la so le")
