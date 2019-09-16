# my_first_calculator.py by AceLewis

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')
num1 = float(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = float(input('Please choose your second number: '))
#will use input to give answer in less lines 
if sign == '+':
    print(num1,'+',num2,'=',(num1+num2))
elif sign == '-':
    print(num1,'',num2,'=',(num1-num2))
elif sign == '/':
    print(num1,'/',num2,'=',(num1/num2))
elif sign == '*':
    print(num1,'*',num2,'=',(num1*num2))
else:
    print('invalid value')    
    
print("Thanks for using this calculator, goodbye :)")
