per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада: '))
deposit = []
percent = list(per_cent.values())
for key in percent:
    deposit.append(key * money / 100)

print('Deposit =', deposit)
print('Максимальная сумма, которую вы можете заработать -', max(deposit))
