from textwrap import dedent


snakes_cafe_orders = {
    "Wings":0,
    "Cookies":0,
    "Spring Rolls":0,
    "Salmon":0,
    "Steak":0,
    "Meat Tornado":0,
    "A Literal Garden":0,
    "Ice Cream":0,
    "Cake":0,
    "Pie":0,
    "Coffee": 0,
    "Tea":0,
    "Unicorn Tear":0,
}

def snakes_cafe_welcome_customer():
    welcome = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """
    print(dedent(welcome))

def snakes_cafe_menu():
    menu = """
    Appetizers
    ----------
    {}
    {}
    {}

    Entrees
    -------
    {}
    {}
    {}
    {}

    Desserts
    --------
    {}
    {}
    {}

    Drinks
    ------
    {}
    {}
    {}
    """.format(
        *snakes_cafe_orders
    )
    print (dedent(menu))

def snakes_cafe_prompt_customer():
    prompt = """
    ***********************************
    ** What would you like to order? **
    ***********************************
    """

    while True:
        order = input(dedent(prompt)).title()
        if order == "Quit":
            break

        if order not in snakes_cafe_orders:
            print(f"Sorry we dont serve {order}")
        else:
            snakes_cafe_orders[order] = snakes_cafe_orders[order]+1
            if snakes_cafe_orders[order] ==1:
                print(f"{snakes_cafe_orders[order]} order of {order} have been added to your meal")
            else:
                print(f"{snakes_cafe_orders[order]} orders of {order} have been added to your meal")

            

    print("Thanks for coming!")
def main():
    snakes_cafe_welcome_customer()
    snakes_cafe_menu()
    snakes_cafe_prompt_customer()

if __name__ == "__main__":
    main()



