import csv
from collections import Counter


# aux function 1 - thiago guarino
def restaurant_output(path_to_file):
    restaurant_dishes, restaurant_days = set(), set()

    with open(path_to_file) as csvfile:
        fieldnames = ['cliente', 'pedido', 'dia']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if row["pedido"]:
                restaurant_dishes.add(row["pedido"])
            if row["dia"]:
                restaurant_days.add(row["dia"])
    return {
        "1": restaurant_dishes,
        "2": restaurant_days,
    }


# aux function 2 - thiago guarino
def maria_output(path_to_file):
    maria_orders = list()

    with open(path_to_file) as csvfile:
        fieldnames = ['cliente', 'pedido', 'dia']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if row["cliente"] == "maria":
                maria_orders.append(row["pedido"])
    return {
        "1": maria_orders,
    }


# aux function 3 - thiago guarino
def arnaldo_output(path_to_file):
    arnaldo_orders = list()

    with open(path_to_file) as csvfile:
        fieldnames = ['cliente', 'pedido', 'dia']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if row["cliente"] == "arnaldo":
                arnaldo_orders.append(row["pedido"])

    return {
        "1": arnaldo_orders,
    }


# aux function 4 - thiago guarino
def joao_output(path_to_file):
    joao_fav_dishes, joao_restaurant_days = set(), set()

    with open(path_to_file) as csvfile:
        fieldnames = ['cliente', 'pedido', 'dia']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if row["cliente"] == "joao":
                joao_fav_dishes.add(row["pedido"])
                joao_restaurant_days.add(row["dia"])
    return {
        "1": joao_fav_dishes,
        "2": joao_restaurant_days
    }


# task 1 - thiago guarino
def analyze_log(path_to_file):
    if (path_to_file.endswith('.csv')) is not True:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        rest_results = restaurant_output(path_to_file)
        maria_results = maria_output(path_to_file)
        arnaldo_results = arnaldo_output(path_to_file)
        joao_results = joao_output(path_to_file)

        maria = f"Q 1: {Counter(maria_results['1']).most_common()[0][0]}\n"
        arnaldo = f"Q 2: {Counter(arnaldo_results['1'])['hamburguer']}\n"
        joao1 = f"Q 3: {rest_results['1'].difference(joao_results['1'])}\n"
        joao2 = f"Q 4: {rest_results['2'].difference(joao_results['2'])}\n"

        question1 = "Q 1: Qual o prato mais pedido por 'maria'?\n"
        question2 = "Q 2: Quantas vezes 'arnaldo' pediu 'hamburguer'?\n"
        question3 = "Q 3: Quais pratos 'joao' nunca pediu?\n"
        question4 = "Q 4: Quais dias 'joao' nunca foi à lanchonete?\n"

        results_arr = [maria, arnaldo, joao1, joao2]

        report_questions = [
            question1,
            question2,
            question3,
            question4
        ]

        output_new_file = open("data/mkt_campaign.txt", "w+")
        output_new_file.writelines(report_questions)
        output_new_file.writelines("\n")
        output_new_file.writelines(results_arr)
        output_new_file.close()
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
