# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов
old_txt = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_txt = []
for el in old_txt:
    if el.isdigit():
        number = int(el)
        new_txt.extend(['"', f'{number: 02d}', '"'])
    elif (el.startswith('-') or el.startswith('+')) and el[1:].isdigit():
        number = int(el[1:])
        new_txt.extend(['"', f'{el[0]}{number: 02d}', '"'])
    else:
        new_txt.append(el)
        new_txt.append(' ')
text = ' '.join(new_txt).strip()
print(text)
