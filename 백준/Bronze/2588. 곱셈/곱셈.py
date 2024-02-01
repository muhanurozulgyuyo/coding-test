A = int(input())
B = int(input())

b = []

for i in str(B):
    b.append(i)

b.reverse()
    
for j in b:
    print(A * int(j))
    
print(A * B)

