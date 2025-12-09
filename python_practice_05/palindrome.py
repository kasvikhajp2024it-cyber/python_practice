#Palindrome number

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if reverse == num:
    print(num, "is a Palindrome number")
else:
    print(num, "is NOT a Palindrome")


#Palindrome STRING

text=input("enter a string : ")

if(text==text[::-1]):
    print(text," is a Palindrome ")
else:
    print(text," is not a Palindrome ")    
