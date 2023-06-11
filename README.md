## Trybe Project 36 - Restaurant Orders


## PROJECT OVERVIEW

  This is project #6 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/). This is the last project of the Module.

  The Pão na Chapa snack bar has a customer order system that saves the name of the person, the order placed and the day of the week of the service. The cafeteria's management wants to increase its sales and improve its internal management and, for that, it has hired you to implement an improvement project, the `Restaurant Orders` Project.
  
  For the main tasks, you will code the system that generates reports with information about the orders and the customers who frequent the snack bar. This data will help the work of a marketing agency in order to leverage sales and the number of customers. (output: "mkt_campain.txt" file)

  For the bonus tasks, the focus of the project should be controlling the stock of ingredients to ensure that the digital menu of Pão na Chapa always offers products that are available in stock, avoiding frustration on the part of customers. (output: console report)
  
  The project is structured in two mandatory task and two bonus tasks. Stack: Python3.

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>

  <details>
    <summary>
      <b>skills developed coding the project</b>
    </summary>
    <ul>
      <li>work with Hashmaps and Dict</li>
      <li>work with Sets</li>
    </ul>
  </details>

## PROJECT TASKS

<details>
  <summary>
    <b>Tasks and Status</b>
  </summary>

   * tasks 3 and 4 are bonus tasks

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
  4.1 - when executing the `add_new_order` method for an order with a dish that does not have enough ingredients in stock, the method returns False | :heavy_check_mark:
  4.2 - when executing the `get_available_dishes` method, the method returns all the dishes that have enough ingredients for their preparation | :heavy_check_mark:
  4.3 - when executing the `get_available_dishes` method, the method does not return dishes whose ingredients are not enough for their preparation | :heavy_check_mark:

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

<details>
  <summary><strong>How To Execute the App</strong></summary>

  As of this moment there is no way to 'execute' this app.

  - to open the Console Menu: `python3 src/main.py`

</details>