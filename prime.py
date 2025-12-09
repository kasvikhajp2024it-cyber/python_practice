#Write a function to check if a number is prime

num=int(input("Enter a number : "))
if(num<=1):
    print(num," is not a prime")
else:
    for i in range(2,num):
        if(num%i==0):
            print(num," is not a prime")
            break
    else:
            print(num," is a prime")    
          

