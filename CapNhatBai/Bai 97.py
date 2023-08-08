# Bài 97: Viết chương trình nhập 3 cạnh của 1 tam giác, cho biết đó là tam giác gì

a, b, c = map(float, input('Nhập độ dài 3 cạnh tam giác: ').split())
eps = 1e-10

if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b:
    flag = 0
    if a == b or b == c or c == a:
        flag += 1
    if a == b and b == c:
        flag += 1
    if abs(pow(a, 2) + pow(b, 2) - pow(c, 2)) < eps or abs(pow(a, 2) + pow(c, 2) - pow(b, 2)) < eps or abs(pow(c, 2) + pow(b, 2) - pow(a, 2)) < eps:
        flag += 3
    tamgiac = {
        0: 'Tam giac thuong',
        1: 'Tam giac can',
        2: 'Tam giac deu',
        3: 'Tam giac vuong',
        4: 'Tam giac vuong can'
    }
    print(tamgiac[flag])
else:
    print('Nhập số đo không hợp lệ')

    