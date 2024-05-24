# month = 15
# if month in [12,1,2]:
#     print("winter")
# elif month in [3,4,5]:
#     print("spring")
# elif month in [6,7,8]:
#     print("summer")
# elif month in [9,10,11]:
#     print("autumn")
# else:
#     print("Некорректный номер месяца ")

# is_logged_in = True
# has_items_in_cart = True
# has_shipping_address = False
# has_order = False
# is_first_order = False
# min_purchase = 1000
# total_purchase = 1000
# if is_logged_in and has_items_in_cart and has_shipping_address:
#     print("все критерии для оформлления заказа")
#     has_order = True
# else:
#     print("не все критерии выполненны для оформления заказа, пожалуйста проверти информацию")
# if has_order and (is_first_order or total_purchase >= min_purchase):
#     print("Выполучаете скидку")
# else:
#     print("Вы не получаете скидку")

    #
numbers = 7
if numbers in [7, 13, 21]:
    print("Счасливое число")
elif numbers in range(1, 101):
    print("Число в указанном диапазоне")
else:
    print("Вам не повезло")