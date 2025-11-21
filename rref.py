import numpy as np
def hzj(A):
    row , column = A.shape
    A=A.astype('float')
    zero=1e-8
    c=0
    r=0

    while c<column and r<row:

        if np.max(abs(A[r:,c]))<zero:
            c+=1
            continue

        if np.argmax(abs(A[r:,c]))!=0:
            A[[r,np.argmax(abs(A[r:,c]))+r]] = A[[np.argmax(abs(A[r:,c]))+r, r]]
        A[r]/=(A[r,c])

        for i in range(row):
            if i!=r : A[i]-=A[r]*A[i,c]

        r+=1
        c+=1

    A[np.abs(A) < 1e-10] = 0
    return A

row = int(input("输入矩阵行数: "))
col = int(input("输入矩阵列数: "))

A = []

for i in range(row):
    row = list(map(float, input(f"输入第{i+1}行的 {col} 个数字，用空格分隔: ").split()))
    A.append(row)

A = np.array(A)

print(A)

print(hzj(A))