 #How to print “Hello World” on Python?
print("Hello World")

# How to print “Hello + Username” with the user’s name on Python?
name=input("enter your name:")
print("Hello",name)

#How to add 2 numbers entered on Python?
n1=input("1st number:")
n2=input("2nd number:")
sum=float(n1)+float(n2)
print(sum)

print(sum/2)     # Average of 2 Entered Numbers

#How to calculate the Entered Visa and Final Grade Average on Python?


# Average of 3 Written Grades
grade1=float(input("enter grade 1 : "))
grade2=float(input("enter grade 2 : "))
grade3=float(input("enter grade 3 : "))
list=[grade1,grade2,grade3]
print(list)
sum=grade1+grade2+grade3
if len(list)>0:
    average=sum/len(list)
    print(average)
else:
    print("invalid")    

#Class Pass Status (PASSED — FAILED) of the Student whose Written Average
if(average>50):
    print("student PASSED")
else:
    print("student")    

# odd or even 
NUM=int(input("enter a number"))
if(NUM % 2==0):
    print("EVEN")
else:
    print("ODD")    


#Class Pass Status (PASSED — FAILED) of the Student whose Written Average
if(average>50):
    print("student PASSED")
else:
    print("student")   

# number is Positive, Negative, or 0 
number=input("enter a number :")
if(number>0):
    print("POSITIVE")
elif(number==0):
    print("ZERO")    
else:
    print("NEGATIVE")    

#calculate body mass INDEX
weight=input("enter your weight :")
height=input("enter your height :")
BMI=weight/height**2
print(BMI)

#age is entered can get a driver’s license 
age=int(input("entre your age"))
if(age>18):
    print("can get license")
else:
    print("not permitted")    

    #List Even Numbers 1–100 
    for i in range(101):
       if(i%2==0) :
           print(i)

#Odd Numbers from 1–100
for i in range(101):
       if(i%2!=0) :
           print(i)


#numbers between 1 and 100 that are divided by 3 and 5 
if(number%3==0 & number%5==0):
    print(number)

# 1 to User-Entered Number
for i in range(1,int(number)+1):
    print(i)

#ine char after another
word="KASVIKHA"
for i in word:
    print(i)

#sum of numbers between two numbers the user has entered
num1=int(input('enter a number :'))
num2=int(input('enter a number :'))
for i in range()