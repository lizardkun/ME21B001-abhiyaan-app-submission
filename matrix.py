m = int(input("rows: "))
n = int(input("columns: "))

a = []

for i in range(m):
    row =[]
    for j in range(n):
    	row.append(int(input('A[' + str(i+1) + ',' + str(j+1) +']: ')))
    a.append(row)

print()

for i in range(m):
    for j in range(n):
        print(a[i][j], end = " ")
    print()

k=int(input("enter number"))
z=0
for i in range(m):
    for j in range(n):
        if k==a[i][j]:
            print(i+1,",",j+1)
            z=1
            print("true")
        
        
if z==0:
    print("False")
else:
    print("done")


        