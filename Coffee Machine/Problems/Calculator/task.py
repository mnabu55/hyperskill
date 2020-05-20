# put your python code here
first_number = float(input())
second_number = float(input())
operand = input()

answer = 0.0

if second_number == 0. and (operand == "/" or operand == "mod" or operand == "div"):
    print("Division by 0!")
else:
    if operand == "+":
        answer = first_number + second_number
    elif operand == "-":
        answer = first_number - second_number
    elif operand == "/":
        answer = first_number / second_number
    elif operand == "*":
        answer = first_number * second_number
    elif operand == "mod":
        answer = first_number % second_number
    elif operand == "pow":
        answer = first_number ** second_number
    elif operand == "div":
        answer = first_number // second_number
    else:
        print("no definition case")
    print("{}".format(answer))
