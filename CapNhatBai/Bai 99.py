# Bài 99: Viết chương trình nhập vào 3 số thực. Hãy in 3 số ấy ra màn hình theo thứ tự tăng dần mà chỉ dùng tối đa 1 biến phụ

a,b,c=map(float,input('Nhập 3 số thực a,b,c: ').split())
midNum=a+b+c-max(a,b,c)-min(a,b,c)
print(min(a,b,c),'<',midNum,'<',max(a,b,c))