# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k. Пример: 
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import json

def get_polynomial(n):
    result = []
    coefficients = []

    for _ in range(n + 1):
        coefficients.append(randint(0, 100))
    print(f'Коэффициенты: {coefficients}')

    count = 0
    for i in range(n, 0, -1):
        if coefficients[count] == 0:
            count += 1
            continue
        if i == 1:
            result.append(f'{coefficients[count]}*x + ')
            count += 1
        else:
            result.append(f'{coefficients[count]}*x^{i} + ')
            count += 1
            
    result.append(f'{coefficients[count]} = 0')
    return result

def save():
    with open('equation.json', 'w') as fh:
        fh.write(json.dumps(equation))

k = int(input('k = '))
equation = "".join(get_polynomial(k))
print(equation)
save()
