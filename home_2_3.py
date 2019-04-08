# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name — строка, полученная от пользователя,
# health = 100,
# damage = 50.
#
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.




import random
def attack(person1, person2): #функция атаки
    nice_shot = random.randint(1, 7)
    if nice_shot >= 3: # условие рандома
        person2['health'] -= person1['damage'] #у второго параметра отнимаем значение damage, который будет прописан у первого
        return person1, person2['health']
    else:
        person1['health'] -= person2['damage'] #и наоборот
        return person1['health'], person2


my_wanzer = {
        'health': 100, 'damage': 30, 'name':input('Введите имя Ванзера:')
         }
OCU = {
        'health': 140, 'damage': 20, 'name':input('Введите противника Объединённого Океанического Союза:')
        }
turn = 1  # указываем ход

while my_wanzer['health'] <= 0 and OCU['health'] <= 0: #проверяем запас здоровья
    if turn % 2 != 0: # если ход четный, то ходит игрок (у нас он уже начинается с единицы, так что начинает игрок)
        my_wanzer,OCU = attack(my_wanzer,OCU)
    else:
        OCU,my_wanzer = attack(OCU,my_wanzer)
    turn += 1 # добавляем счетчик хода

else: # если у кого-то кончились жизни, то
    if my_wanzer['health'] > 0: # сравниваем ключ health из словаря player с нулём.
        print(f"{my_wanzer['name']} побелил. Поздравляем")# выводим результат, взяв ключ name из словаря игрока
    else:
        print(f"{OCU['name']} победил. Попробуй еще раз")# иначе победил противник