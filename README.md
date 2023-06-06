## Trybe Project 36 - Restaurant Orders


## PROJECT OVERVIEW

  This is project #6 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/). This is the last project of the Module.

  A lanchonete baguette_bread cook Pão na Chapa baguette_bread cook possui um sistema de faturamento de pedidos de clientes que salva o nome da pessoa, o pedido realizado e o dia da semana do atendimento. A gerência da lanchonete quer aumentar suas vendas e melhorar sua gestão interna e, para isso, te contratou para implementar um projeto de melhorias, o Projeto `Restaurant Orders`. Em um primeiro momento (requisitos obrigatórios), você deverá atuar para que o sistema gere relatórios com informações sobre os pedidos e as pessoas clientes que frequentam a lanchonete. Estes dados irão auxiliar o trabalho de uma agência de marketing com o objetivo de alavancar as vendas e o número de pessoas clientes.
  Em um segundo momento (requisitos bônus), o foco do projeto deverá ser o controle do estoque de ingredientes para garantir que o cardápio digital da baguette_bread cook Pão na Chapa baguette_bread cook sempre ofereça produtos que estão disponíveis no estoque, evitando frustrações por parte das pessoas clientes.
  O projeto está estruturado em duas etapas obrigatórias e duas etapas bônus, totalizando 4 requisitos. 

  Stack: Python3.

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>

## PROJECT TASKS

<details>
  <summary>
    <b>Tasks and Status</b>
  </summary>

  *description* | *status*
  --- | :---:
  1.1 - when executing the `analyze_log` method, the data is correctly filled in the `data/mkt_campaign.txt` file | :heavy_check_mark:
  1.2 - when executing the `analyze_log` method with a non-existent file, the method returns an error | :heavy_check_mark:
  1.3 - when executing the `analyze_log` method with an invalid extension, the method returns an error | :heavy_check_mark:
  2.1 - when instantiating the `TrackOrders` class for the first time, the len() method returns the number of orders equal to zero | :heavy_check_mark:
  2.2 - when executing the `add_new_order` method, the method must add an order | :heavy_check_mark:
  2.3 - when executing `get_most_ordered_dish_per_costumer`, the method returns the most ordered dish | :heavy_check_mark:
  2.4 - when executing `get_never_ordered_per_costumer`, the method returns the order that the customer never madez | :heavy_check_mark:
  2.5 - when executing `get_days_never_visited_per_costumer`, the method returns the days that the customer never visited | :heavy_check_mark:
  2.6 - when executing the `get_busiest_day` method, the method returns the busiest day | :heavy_check_mark:
  2.7 - when executing the `get_least_busy_day` method, the method returns the least busy day | :heavy_check_mark:
  3.1 - when executing the `get_quantities_to_buy` method, the method returns the updated list of ingredients | :heavy_check_mark:
  3.2 - when executing the `get_quantities_to_buy` method, the method returns the amount of ingredients that need to be bought for hamburger | :heavy_check_mark:
  3.3 - when executing the `get_quantities_to_buy` method, the method returns the updated list of ingredients that use different recipes | :heavy_check_mark:
  4.1 - when executing the add_new_order method for an order with a dish that does not have enough ingredients in stock, the method returns False | :heavy_check_mark:
  4.2 - when executing the get_available_dishes method, the method returns all the dishes that have enough ingredients for their preparation | :heavy_check_mark:
  4.3 - when executing the get_available_dishes method, the method does not return dishes whose ingredients are not enough for their preparation | :heavy_check_mark:

</details>


## HOW TO RUN THE APP

  1. clone the repository

  - `git clone git@github.com:thiagoguarino/trybe-project36-restaurant-orders.git`
  
  2. enter the project's folder 

  - `cd trybe-project36-restaurant-orders`

  3. create and open the project's virtual environment

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  4. install dependencies

  - `python3 -m pip install -r dev-requirements.txt`

  5. To execute the app

    a - the files: file_management.py, file_process.py, word_search.py 

    b - set the params: `a = txt_importer('data/nome_pedro.txt')`, then print it: `print(a)`

    c - instance a new queue - `project = Queue()`, call `process("data/arquivo_teste.txt", project)`

    d - declare var `word1 = exists_word("pedro", project)`, `word2 = search_by_word("pedro", project)`

    e - print them - `print(word1)` and `print(word2)`

  6. how to execute the functions:

      a - `python3 ting_file_management/file_management.py`
      
      b - `python3 ting_file_management/file_process.py`

      c - `python3 word_searches/word_search.py`
