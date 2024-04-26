# # create
# a = "hi" #одинарные или двойные кавычки
# b = "hi'hi hi'"#так нельзя
# d = 'hi"ho ho"' #так можно
# # read
# # строка (str)
# # список (list)
# # кортеж (tuple)
# # множество (set, frozenset)
# # словарь (dict)
# # байты (bytes)
# # последовательность байтов (bytearray)
# print(a)
# print ("ho ho ho")
# # можно вызвать символ по индексу
# v = "пончик"
# v[0]
# # update/delete
# # изменение
# m = [75, 76, 77, 78]
# m[0] = 3
# print(m)
# # удоление
# del a[1] #удоление по индексу
# l=457
# del l #полностью удалить переиеную
# # действия со строками
# r = 4
# y = 5
# e = r+y



# a = 1, 2, 3
# b = str(a)
# print(b)
# print(type(b))
#
#
#
# q = 1, 5.5, "hi"
# e = list(q)
# print(e)
# print(type(e))

a=int(input("Введите четное число: "))
if a%2 == 0:
    print(f"Число {a} четное")
else:
    print (f"число {a} не является четным ")

b=str(input("Введите строку"))
len(b)
print(len(b))