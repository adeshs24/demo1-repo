print('Enter the number')
n=int(input())
print('Multiplication Table of '+str(n)+' :')
for i in range(1,11):
    print(str(n)+' * '+str(i)+' = '+ str(i*n))
