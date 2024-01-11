# Bài 110: Cần có tổng 200000 đồng từ 3 loại giấy bạc 1000 đồng, 2000 đồng, 5000 đồng. Lập chương trình để tìm ra tất cả các phương án có thể

def find_combinations(total_amount, n1000, n2000, n5000):
    for x in range(n1000 + 1):
        for y in range(n2000 + 1):
            for z in range(n5000 + 1):
                if x * 1000 + y * 2000 + z * 5000 == total_amount:
                    print(f"Phuong an: {x} x 1000 + {y} x 2000 + {z} x 5000 = {total_amount} dong")

def main():
    total_amount = 200000
    n1000 = int(input("Nhap so to 1000 dong: "))
    n2000 = int(input("Nhap so to 2000 dong: "))
    n5000 = int(input("Nhap so to 5000 dong: "))

    find_combinations(total_amount, n1000, n2000, n5000)

# Test rollback (chính thức)

if __name__ == "__main__":
    main()
