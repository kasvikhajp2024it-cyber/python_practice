# Write a function to find factorial of a number using recursion

num=int(input("Enter a number : "))
a,b=0,1
for i in range(num+1):
    print(a,end=" ")
    a,b=b,a+b
    