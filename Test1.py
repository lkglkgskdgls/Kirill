#простые
a=1 #простое число
a=1.1 #вещзественное число
a= 1 + 1j #комплексное число
a=True #,ektjdt pyfxtybt
a= None #пустой тип
# Составное
a= "hello" #строка
a= [1, True, "Hello"] #список
a= (1, True, "hi")#кортеж
a= frozenset({1,1.0,"hi"})#неизвестное множество
a={"a":1, "b":2} #словарь
a= b"hi" #айтовый тип
a= bytearray(b"Hello")
# Вызываемые
a= [1, 1.0, "Hi"] #создаваемый список
help(a) #выводим информацию об a
print(a) #выводим на консоль
b= input("ведите число") #информацию вводит пользователь
len(a)#количесто объектов a
min(a)#минимальное значение a
max(a) #максимальное значение в a
type(a) #тип объектов a
# динамическая типизация
a=1
a="новое значение переменой a"
# неявная типизация
some_var:int=1
other_var:str= "Hi"
some_var=1
other_var= "Hello world"
# Сильная типизация
5+1,1 #6.1
5+"str" #ошибка