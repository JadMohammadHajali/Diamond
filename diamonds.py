print("Enter the value of row to create the diamond shape")
n=int(input("Enter n : "))

for i in range(n):
    print(" "*(n-i)+"*"*(2*i+1))
for j in range (n-2,-1,-1):
    print(" "*(n-j)+"*"*(2*j+1))


