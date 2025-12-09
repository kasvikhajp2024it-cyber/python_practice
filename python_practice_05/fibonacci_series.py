#without TEMP varible

num=int(input("enter a number : "))
a,b=0,1
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b


#with TEMP varible

num=int(input("enter a number : "))
a,b=0,1

for i in range(num):
    print(a , end=" ")
    temp=a+b
    a=b 
    b=temp