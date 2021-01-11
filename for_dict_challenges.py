# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

cnt_name = {}

for student in students:
  for key, value in student.items():
    if value not in cnt_name:
      cnt_name[value] = 1
    else:
      cnt_name[value] += 1

for key, value in cnt_name.items():
  print(f'{key}: {value}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
cnt_name = {}
for name in students:
  for key, value in name.items():
    if value not in cnt_name:
      cnt_name[value] = 1
    else:
      cnt_name[value] += 1

max_cnt = max(cnt_name.values())
final_dict = sorted(cnt_name.items(), key=lambda x :x[1], reverse=True)[0]
print(f'Самое частое имя среди учеников: {final_dict[0]}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

cnt_name = []

for name in school_students:
  counter = {}
  for student in name:
    if student['first_name'] in counter:
      counter[student['first_name']] += 1
    else:
      counter[student['first_name']] = 1
  #print(counter)
  cnt_name.append(counter)
  #print(cnt_name)

for i in cnt_name:
  print(f'The most frequent name in class {cnt_name.index(i) + 1}: {max(i, key=i.get)}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for clas in school:
  girls = 0
  for name in clas['students']:
    if is_male[name['first_name']] == False:
      girls += 1
  boys = len(clas['students']) - girls
  print(f'В классе {clas["class"]} {girls} девочки и {boys} мальчика.')


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for clas in school:
  girls = 0
  for name in clas['students']:
    if is_male[name['first_name']] == False:
      girls += 1
  boys = len(clas['students']) - girls
  if girls < boys:
    print(f'Больше всего мальчиков в классе {clas["class"]}')
  else:
    print(f'Больше всего девочек в классе {clas["class"]}')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
