nums = input("Nhap cac so, cach nhau boi dau phay: ").split(",")

nums = [int(x) for x in nums]
tong = sum(nums)

print("Danh sach:", nums)
print("Tong:", tong)
