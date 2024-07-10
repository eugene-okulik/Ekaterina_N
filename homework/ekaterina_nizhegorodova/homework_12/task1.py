class Flowers:
    def __init__(self, color, stem_length, fresh, life_time, smell):
        self.__color = color
        self.stem_length = stem_length
        self.fresh = bool(fresh)
        self.__life_time = life_time
        self.__smell = smell

    @property
    def color(self):
        return self.__color

    @property
    def life_time(self):
        return self.__life_time

    @property
    def smell(self):
        return self.__smell


class Lily(Flowers):
    def __init__(self, color, stem_length, fresh, life_time, smell):
        super().__init__(color, stem_length, fresh, life_time, smell)
        self.name = "Lily"
        self.price = 10

    def __str__(self):
        return (f'{self.name}, price: {self.price}, color: {self.color}, stem length: {self.stem_length}, '
                f'smell: {self.smell}, fresh: {self.fresh}, life time: {self.life_time}')

    def __repr__(self):
        return (f'{self.name}, price: {self.price}, color: {self.color}, stem length: {self.stem_length}, '
                f'smell: {self.smell}, fresh: {self.fresh}, life time: {self.life_time}')


class Iris(Flowers):
    def __init__(self, color, stem_length, fresh, life_time, smell):
        super().__init__(color, stem_length, fresh, life_time, smell)
        self.name = "Iris"
        self.price = 7

    def __str__(self):
        return (f'{self.name}, price: {self.price}, color: {self.color}, stem length: {self.stem_length}, '
                f'smell: {self.smell}, fresh: {self.fresh}, life time: {self.life_time}')

    def __repr__(self):
        return (f'{self.name}, price: {self.price}, color: {self.color}, stem length: {self.stem_length}, '
                f'smell: {self.smell}, fresh: {self.fresh}, life time: {self.life_time}')


class Tulip(Flowers):
    def __init__(self, color, stem_length, fresh, life_time, smell):
        super().__init__(color, stem_length, fresh, life_time, smell)
        self.name = "Tulip"
        self.price = 3

    def __str__(self):
        return (f'{self.name}, price: {self.price}, color: {self.color}, stem length: {self.stem_length}, '
                f'smell: {self.smell}, fresh: {self.fresh}, life time: {self.life_time}')

    def __repr__(self):
        return (f'{self.name}, price: {self.price}, color: {self.color}, stem length: {self.stem_length}, '
                f'smell: {self.smell}, fresh: {self.fresh}, life time: {self.life_time}')


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower: Flowers):
        self.flowers.append(flower)
        return self.flowers

    def calculate_total_price(self):
        total_price = 0
        for flower in self.flowers:
            total_price += flower.price
        return total_price

    def avg_life_time(self):
        total_life = 0
        for flower in self.flowers:
            total_life += flower.life_time
        return total_life // len(self.flowers)

    def sort_flowers(self, key):
        if key == "price":
            self.flowers.sort(key=lambda flower: flower.price)
        if key == "color":
            self.flowers.sort(key=lambda flower: flower.color)
        if key == "stem_length":
            self.flowers.sort(key=lambda flower: flower.stem_length)
        if key == "fresh":
            self.flowers.sort(key=lambda flower: flower.fresh, reverse=True)
        return self.flowers

    def filter(self, param, value):
        search_result = []
        if param == "life_time":
            search_result = [flower for flower in self.flowers if flower.life_time == value]
        if param == "color":
            search_result = [flower for flower in self.flowers if flower.color == value]
        return search_result


iris1 = Iris("blue", 12, True, 6, "spicy")
iris2 = Iris("blue", 13, True, 6, "spicy")
iris3 = Iris("blue", 12, False, 6, "spicy")
lily1 = Lily("white", 13, True, 5, "sweet")
lily2 = Lily("white", 12, True, 5, "sweet")
lily3 = Lily("white", 14, False, 4, "sweet")
tulip1 = Tulip("yellow", 10, True, 5, "sweet")
tulip2 = Tulip("yellow", 10, True, 5, "sweet")
tulip3 = Tulip("white", 10, False, 5, "fresh")


bouquet1 = Bouquet()
bouquet1.add_flower(iris1)
bouquet1.add_flower(iris2)
bouquet1.add_flower(iris3)
bouquet1.add_flower(lily1)
bouquet1.add_flower(lily2)
bouquet1.add_flower(lily3)
bouquet1.add_flower(tulip1)
bouquet1.add_flower(tulip2)
bouquet1.add_flower(tulip3)
print(bouquet1.flowers)
print(bouquet1.calculate_total_price())
print(bouquet1.avg_life_time())
print(bouquet1.sort_flowers("price"))
print(bouquet1.sort_flowers("fresh"))
print(bouquet1.filter("life_time", 4))
print(bouquet1.filter("color", "white"))
