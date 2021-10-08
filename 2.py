def переводвсистемусчисления(a, b):
    вывод = ''
    while a > 0:
       вывод += str(a % b)
       a = a // b
    вывод = вывод[::-1]
    return вывод
try:
    a = int(input('Ввод числа: '))
    b = int(input('Желаемая система счисления: '))
except ValueError as message:
 print('Ошибка')
else:
 print(a, '-->', переводвсистемусчисления(a, b))