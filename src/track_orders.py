from collections import Counter


# task 2 - thiago guarino
class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        counter = Counter()
        total_customers_order = list()
        menu = set()
        for client_order in self.orders:
            total_customers_order.append(client_order[1])
            for order_data in client_order:
                menu.add(order_data[1])
                if order_data in total_customers_order:
                    counter[order_data] += 1
        dish_most_common = counter.most_common()
        return dish_most_common[0][0]

    def get_never_ordered_per_customer(self, customer):
        customer_ordered_dishes = set()
        total_ordered_dishes = list()
        dishes_available = set()
        for client_order in self.orders:
            total_ordered_dishes.append(client_order[1])
            for dish in total_ordered_dishes:
                dishes_available.add(dish)
            for order_data in client_order:
                if order_data == customer:
                    customer_ordered_dishes.add(client_order[1])
                    dishes_available.difference(customer_ordered_dishes)
        return dishes_available.difference(customer_ordered_dishes)

    def get_days_never_visited_per_customer(self, customer):
        customer_days = set()
        days_week_visitation_count = list()
        days_week = set()
        for client_order in self.orders:
            days_week_visitation_count.append(client_order[2])
            for day in days_week_visitation_count:
                days_week.add(day)
            for order_data in client_order:
                if order_data == customer:
                    customer_days.add(client_order[2])
                    days_week.difference(customer_days)
        return days_week.difference(customer_days)

    def get_busiest_day(self):
        counter = Counter()
        days_week = [
          'domingo',
          'segunda-feira',
          'terça-feira',
          'quarta-feira',
          'quinta-feira',
          'sexta-feira',
          'sábado'
        ]
        for client_order in self.orders:
            for order_data in set(client_order):
                if order_data in days_week:
                    counter[order_data] += 1
        day_most_common = counter.most_common()
        return day_most_common[0][0]

    def get_least_busy_day(self):
        counter = Counter()
        days_week = [
          'domingo',
          'segunda-feira',
          'terça-feira',
          'quarta-feira',
          'quinta-feira',
          'sexta-feira',
          'sábado'
        ]
        for client_order in self.orders:
            for order_data in set(client_order):
                if order_data in days_week:
                    counter[order_data] += 1
        day_most_common = counter.most_common()
        return day_most_common[-1][0]
