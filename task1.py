money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
counter = 0
delta=spend-salary
while (delta < money_capital):
    delta=spend-salary
    money_capital-=delta
    spend+=spend*counter*increase
    counter+=1
counter+=1 #прибавка к счетчику за первый месяц
print("Количество месяцев, которое можно протянуть без долгов:", counter)

