#Automorphic Number
num=int(input("enter a number : "))
n=len(str(num))
sqr=num**2

if(sqr%10**n==num):   
    print(num,"is an Automorphic Number")
else:
    print(num,"is NOT an Automorphic Number") 