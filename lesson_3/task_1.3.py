"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших 
двух аргументов.
"""
def my_func(a,b,c):
    my_list = [a,b,c]
    summ = sum(my_list)- min(my_list)
    print(summ)

my_func(5,3,10)