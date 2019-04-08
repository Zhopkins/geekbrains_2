# Создайте функцию, принимающую на вход 3 числа
# и возвращающую наибольшее из них.




def max_count(number1, number2, number3):
   counter = [number1, number2, number3]
   return max(counter)

number1 = int(input('Первое число: '))
number2 = int(input('Второе число: '))
number3 = int(input('Третье число: '))

print (max_count(number1, number2, number3))


