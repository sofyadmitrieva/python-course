#Задание 1
birth = int(input("Введите год рождения "))
current_year = int(input("Введите текущий год "))
age = current_year - birth
print('Вам', age, 'лет', sep=' ')

#Задание 2
rub = float(input('Сумма в рублях: '))
kurs = float(input('Курс доллара: '))
dollar = rub / kurs
print(rub, 'рублей по курсу ', kurs, '= ', dollar) 

#Задание 3
number = int(input('Введите число: '))
thousand = number // 1000
hundred = number // 100 % 10
ten = number % 100 // 10
unit = number % 10
print (number, '->', thousand, ' тысячи', hundred,  ' сотен', ten, ' десятков', unit, ' единиц')