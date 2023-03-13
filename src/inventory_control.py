from collections import Counter


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    # tasks 3 and 4 - thiago guarino
    def __init__(self):
        self.ingredients_to_buy = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }
        self.orders = []

    def add_new_order(self, customer, order, day):
        for i in self.INGREDIENTS[order]:
            if self.MINIMUM_INVENTORY[i] <= self.ingredients_to_buy[i]:
                return False

        self.orders.append([customer, order, day])

        ingredients_counter = Counter()

        for order in self.orders:
            for order_data in order:
                if order_data in self.INGREDIENTS.keys():
                    order_ingredients = self.INGREDIENTS[order_data]
                    for ingredient in order_ingredients:
                        ingredients_counter[ingredient] += 1

        for ingredient in self.MINIMUM_INVENTORY.keys():
            if ingredient not in ingredients_counter.keys():
                ingredients_counter.update({ingredient: 0})

        aa = ingredients_counter.most_common()

        for ingredient_data in aa:
            self.ingredients_to_buy[ingredient_data[0]] = ingredient_data[1]

    def get_quantities_to_buy(self):
        return self.ingredients_to_buy

    def is_ingredient_available(self, order):
        quant_to_buy = self.get_quantities_to_buy()
        for ingredient in self.INGREDIENTS[order]:
            if quant_to_buy[ingredient] >= self.MINIMUM_INVENTORY[ingredient]:
                return False
            return True

    def get_available_dishes(self):
        result = set()
        for dish in self.INGREDIENTS.keys():
            if self.is_ingredient_available(dish) is True:
                result.add(dish)
        return result
