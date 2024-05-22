# условные опреаторы
# if else
# is_rainy=True
# if is_rainy:
#     print("Беру зонт")
#     print("надеть сапоги")
# else
#     print("не беру зонт")
# print("Иду гулять")

# if без else
# is_rainy = True
# if is_rainy:
#     print("беру зонт")
# print("иду гулять")
#вложенное условие
# a= True
# b= False
# if a:
#     if b:
#         print("ok")
#     else:
#         print("no_ok")
# else:
#     print("xoxoxoxoxoxoxxoxoxoxoxo")
# print("kgkgkdk")
#Операторы сравнения
# !=  неравенство
print("5>3", 5>3)#True
print("длинна слова равна 1", len("hello")==1)#False
#in is
str_1='test'
str_2="test"
str_3='''test'''
str_4="""test"""
print(str_1 == str_2 == str_3 == str_4)
print(
    (str_1 == str_2)
    and (str_2 == str_3)
    and (str_3 == str_4)
)
# if-elif-else
if a > 10:
    print('a больше 10')
elif a<10:
    print('a меньше 10')
else:
    print("a равно 10")