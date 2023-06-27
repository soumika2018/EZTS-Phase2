r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
matrix = []
print("Enter the elements:")
for i in range(r):
    a =[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = " ")
    print()
print("diagonal elements are:")
for i in range (r):
    for j in range (c):
        if i==j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()

print("non diagonal elements are:")
for i in range (r):
    for j in range (c):
        if i!=j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()

print("upper diagonal elements are:")
for i in range (r):
    for j in range (c):
        if i<j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("lower diagonal elements are:")
for i in range (r):
    for j in range (c):
        if i>j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()




#(or)


 
n=int(input("Enter row Size of the matrix:"))
m=int(input("Enter col size of the matrix:"))
if m==n:
    matrix=[]
    print("Enter the Martix below:")
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    diagonal=[]
    non_diagonal=[]
    lower_diagonal=[]
    upper_diagonal=[]
    for i in range(n):
        for j in range(m):
            if i==j:
                diagonal.append(matrix[i][j])
            elif i<j:
                upper_diagonal.append(matrix[i][j])
                non_diagonal.append(matrix[i][j])
            elif i>j:
                lower_diagonal.append(matrix[i][j])
                non_diagonal.append(matrix[i][j])
    print("Diagonal Elements:\n")
    for i in range(len(diagonal)):
        print(' '*i,diagonal[i])
    print()
    print("Non Diagonal Elements:\n")
    for i in range(n):
        for j in range(m):
            if i==j:
                print(' ',end='')
            else:
                print(matrix[i][j],end=' ')
        print()
    print("Upper Diagonal Elements:")
    for i in range(n):
        for j in range(m):
            if i<j:
                print(matrix[i][j],end=' ')
            else:
                print(' ',end=' ')
        print()
    print("Lower Diagonal Elements:")
    for i in range(n):
        for j in range(m):
            if i>j:
                print(matrix[i][j],end=' ')
        print()
else:
    print("It won't work for rectangular matrix")
