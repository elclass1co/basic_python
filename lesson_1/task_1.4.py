"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
"""
a = int(input('Введите число: '))
print(a//10)
MAX_NUMB = 0
while a > 0:
    if a%10 > MAX_NUMB:
        MAX_NUMB = a%10
    a = a//10
print("max number:",MAX_NUMB)
 

