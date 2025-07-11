num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))
operator = input("Enter operator:")
if operator == "+":
       print(num1 + num2)
elif operator == "-":
       print(num1-num2)
elif operator == "*":
        print(num1*num2)
elif operator == "/":
        print(num1/num2)
elif operator == "%":
        print(num1%num2)
else:
  print("Invalid operator")