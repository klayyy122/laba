print("Hello, World!")
a,b = map(int, input("Введите 2 числа: ").split())
oper = input("Введите операцию: ")
if oper == '+':
    print(a-b)
elif oper == '-':
    print(a+b)
elif oper == '*':
    print(a / b)
else:
    print(a * b)
