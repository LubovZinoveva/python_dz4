# Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух числел

def obshii_delitel(x, y):
    if y == 0:
        return x
    else:
        return obshii_delitel(y, x % y)

def kratnoe(a1, a2, delitel):
    return round(a1*a2 / delitel)

a = int(input('a = '))
b = int(input('b = '))
delit = obshii_delitel(a, b)
print(f'Наименьший общий делитель = {delit}')
my_kratnie = kratnoe(a, b, delit)
print(f'Наименьшее общее кратное = {my_kratnie}')