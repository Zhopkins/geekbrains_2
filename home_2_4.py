# 4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# 1. Наносит урон. Это улучшенная версия функции из задачи 3.
# 2. Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа

import random
def attack(person1, person2): #функция атаки
    nice_shot = random.randint(1, 7)
    if nice_shot >= 3: # условие рандома
        person2['health'] -= new_damage(person1['damage'], person2['armor'])
        return person1, person2['health']
    else:
        person1['health'] -= new_damage(person2['damage'], person1['armor'])
        return person1['health'], person2

def new_damage (damage, armor): # новая функция для вычисления урона, для вызова нужно передать два параметра
    return damage / armor


my_wanzer = {
        'health': 100, 'damage': 30, 'armor': 1.2 ,'name':input('Введите имя Ванзера:')
         }
OCU = {
        'health': 140, 'damage': 20, 'armor': 1.8 , 'name':input('Введите противника Объединённого Океанического Союза:')
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