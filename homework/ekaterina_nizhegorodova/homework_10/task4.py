PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price = [item.split() for item in PRICE_LIST.split("\n")]
new_dict = {key: int(value[:-1]) for key, value in price}
print(new_dict)
