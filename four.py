# Дан список, содержащий искажённые данные с должностями и именами сотрудников
roster = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for el in roster:
    out = el.rfind(' ')
    print(f"'Привет, {el[out + 1:].capitalize()}!'")
