import time

print('Добро пожаловать в билетную кассу!')
time.sleep(2)
print()
print('У нас для вас акция - при покупке от 4 билетов, вы получаете скидку в 10%!!!')
time.sleep(2)
print()
number_of_tickets = int(input("Введите количество билетов: "))
total_price = 0
for i in range(number_of_tickets):
    i += 1
    while True:
        age_of_the_visitor = int(input(f'Введите возраст {i}-го посетителя: '))
        if age_of_the_visitor < 18:
            print('Вход бесплатный!')
        elif 18 <= age_of_the_visitor < 25:
            total_price += 990
            print('Цена за вход - 990 руб.')
        else:
            total_price += 1390
            print('Цена за вход - 1390 руб.')
        if type(age_of_the_visitor) == int:
            break
if total_price == 0:
    print("Вам повезло! Вход для Вас бесплатный!")
elif number_of_tickets >= 4:
    total_price = total_price - ((total_price / 100) * 10)
    print(f"Общая стоимость билетов с учётом скидки - {total_price} руб. ")
else:
    print(f"Итого к оплате - {total_price} руб. ")
