import csv
from pubsub import pub
from inventory_control import InventoryControl
from track_orders import TrackOrders
from analyze_log import analyze_log


def print_info(tracker, control):
    print('==========ORDER AND INVENTORY REPORT===============')
    print('\n')
    insight1 = "I1: most ordered dish per customer (maria): "
    insight2 = "I2: never ordered dish per customer (joão): "
    insight3 = "I3: days never visited per customer (joão): "
    insight4 = "I4: busiest day at the restaurant: "
    insight5 = "I5: least busy day at the restaurant: "
    insight6 = "I6: available dishes at the moment: "
    insight7 = "I7: quantities to buy per dishes: "

    print(insight1)
    print(insight2)
    print(insight3)
    print(insight4)
    print(insight5)
    print(insight6)
    print(insight7)
    print('\n')
    print("---------------------- OUTPUTS ----------------------")
    print('\n')
    print(f"I1: {tracker.get_most_ordered_dish_per_customer('maria')}")
    print(f"I2: {tracker.get_never_ordered_per_customer('joao')}")
    print(f"I3: {tracker.get_days_never_visited_per_customer('joao')}")
    print(f"I4: {tracker.get_busiest_day()}")
    print(f"I5: {tracker.get_least_busy_day()}")
    print(f"I6: {control.get_available_dishes()}")
    print(f"I7: {control.get_quantities_to_buy()}")
    print('\n')
    print("---------------------- --------------------------------")


def main():
    topic = 'order'
    path = input("digite o path do CSV: ")

    tracker = TrackOrders()
    control = InventoryControl()
    subs = [tracker.add_new_order, control.add_new_order]

    for sub in subs:
        pub.subscribe(sub, topic)

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for customer, order, day in csv_reader:
            pub.sendMessage(topic, customer=customer, order=order, day=day)

    analyze_log(path)

    print_info(tracker, control)


if __name__ == "__main__":
    main()
