num1 = input("Enter your first number:")
op = input("Enter the operation:")
num2 = input("Enter your second number:")

num1 = int(num1)
num2 = int(num2)
if op == "+":
    print(f"{num1} {op} {num2} = {num1+num2}")
elif op == "-":
    print(f"{num1} {op} {num2} = {num1-num2}")
elif op == "*":
    print(f"{num1} {op} {num2} = {num1*num2}")
elif op == "/":
    print(f"{num1} {op} {num2} = {num1/num2}")
elif op == "//":
    print(f"{num1} {op} {num2} = {num1//num2}")
elif op == "**":
    print(f"{num1} {op} {num2} = {num1**num2}")
elif op == "%":
    print(f"{num1} {op} {num2} = {num1%num2}")
else:
    print("invalid operation")
# This is a comment
