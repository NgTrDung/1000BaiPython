# Bài 109: Viết chương trình in bảng cửu chương ra màn hình

for i in range(1,10,1):
    for j in range(2,11,1):
        if j==10:
            print()
        else:
            print('{0} x {1} = {2:2} |'.format(j,i,j*i),end='')