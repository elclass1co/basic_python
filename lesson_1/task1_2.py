# Создать список, состоящий из кубов нечётных чисел от 0 до 1000:

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем
# включать в сумму,
#  так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится
#  нацело на 7. Внимание: новый список не создавать!!!

a = []
b = []
c = []
sum = 0

for i in range(1, 1000, 2):
    a.append(i)
for y in range(len(a)):
    a[y] **= 3
for item in a:
    while item > 0:
        last_digit = item % 10
        sum += last_digit
        item = item // 10
    if sum % 7 == 0:
        b.append(sum)
print(f"Суммы чисел, сумма которых делится на 7: {len(b)}")

for x in range(len(a)):
    a[x] += 17
for item in a:
    while item > 0:
        last_digit = item % 10
        sum += last_digit
        item = item // 10
    if sum % 7 == 0:
        c.append(sum)
print(f"Суммы чисел, сумма которых делится на 7: {len(c)}")
