# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
  print(name)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
  cnt = len(name)
  print(f'{name} {cnt}') #print(name, len(name), sep=' ')


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
  if is_male[name] == True:
    print(f'{name} Male')
  else:
    print(f'{name} Female')

# for item in names:
#     gender = "мужской" if is_male.get(item) else "женский" 
#     print(f'Имя: {item}, пол: {gender}')

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

print(f'Всего {len(groups)} группы.')
for group in groups:
  print(f'В группе {len(group)} ученика')


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

# group_number = 1
# for group in groups:
#   print(f'Группа {group_number}: {group}'.replace('[', '').replace(']', '').replace("'",""))
#   group_number += 1

for idx, group in enumerate(groups):
  print(f'Группа {idx + 1}: {", ".join(group)}')