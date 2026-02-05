nums = input("Nhap cac so: ").split()

nums = [int(x) for x in nums]

print("So lon nhat:", max(nums))
print("So nho nhat:", min(nums))
