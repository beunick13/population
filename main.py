year = int(input('Введите год, для которого требуется рассчитать ожидаемую численность населения (больше 2015): '))
days = 365

# Населения России в 2015 году
population = 146300000
# Родилось в 2015 году
born = 1940579
# Умерло в 2015 году
die = 1908541
# Приехали в страну в 2015 году
arrive = 598617
# Уехали из страны в 2015 году
leave = 353233
# Коэффициенты рождаемости, смертности
pop_born = born/days*1000
pop_dead = die/days*1000

# Учитывается или нет миграция? Рассчет коэффициентов

migration = input('Требуется ли учитывать миграцию? (Да/Нет)')

if migration == 'Да':
    pop_arrived = arrive / days * 1000
    pop_leaved = leave / days * 1000
else:
    pop_arrived = 0
    pop_leaved = 0

exp_population = (year-2015)*365*(pop_born+pop_dead+pop_arrived+pop_leaved)
print(format(exp_population, '.0f'))
