# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

import random

def get_list(n):
    result_list = []
    for i in range(n):
        result_list.append(random.randint(0, 9))
    return result_list

def sort_list(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def delet_same_element(list1):
    list1 = sort_list(list1)
    element = []
    for i in range(len(list1)-1):
            if list1[i] == list1[i+1]:
                element.append(list1[i])
    for e in element:
        list1.remove(e)
    return list1

try:
    m = int(input('Размерность списка = '))
    my_list = get_list(m)
    print(f'Исходный список: {my_list}')
    my_list = delet_same_element(my_list)
    print(f'Результат: {my_list}')
except:
    print('Ошибка, введите целое число')