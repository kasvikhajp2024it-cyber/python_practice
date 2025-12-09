#Armstrong number using FOR LOOP

num=input("enter an 3 or 4 digit number : ")
n=len(num)
sum=0
for i in num:
    sum +=int(i)**n


if(sum==int(num)):
    print(num,"is an Armstrong number")
else:
    print(num,"is NOT an Armstrong number")


#Armstrong number using WHILE LOOP

num=int(input("enter an 3 or 4 digit number : "))
n=len(str(num))
sum=0
while num>0:
    temp=num%10
    sum +=temp**n
    num//=10

if(sum==num):   
    print(num,"is an Armstrong number")
else:
    print(num,"is NOT an Armstrong number") 

    