# Handle user input to divide two numbers safely .catch division by zero (Hint: Exception
#Handling)

try:
    num1 =7
    num2 =0

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")