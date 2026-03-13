op = input("Enter the operator: ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if op == "+":
    result = num1 + num2
    print(round(result, 2))

elif op == "-":
    result = num1 - num2
    print(round(result, 2))

elif op == "*":
    result = num1 * num2
    print(round(result, 2))

elif op == "/":
    result = num1 / num2
    print(round(result, 2))

else:
    print(f"The operator {op} dose not valid!")