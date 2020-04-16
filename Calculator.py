
try:
    num1 = float(input('Enter 1st number: '))
    op = input('Enter operation: ')
    num2 = float(input('Enter 2nd number: '))
except ValueError:
    print('NaN')

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    print(num1 / num2)
elif op == '*':
    print(num1 * num2)
else:
    print('Invalid operator')

