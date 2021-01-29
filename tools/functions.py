# Important functions for the DQ cash registers

# Imports
import tools.classes as cls  # (contains tkinter)

# --------------------------------------------- General Functions -------------------------------------------------- #


# Navigate between tabs
def navigate(parent, tab):
    parent.select(tab)


# Collect input
def collect_input(inputField, window):
    data = inputField.get()
    window.destroy()

    return data


# Create window
def create_window(size):

    window = cls.Toplevel()  # Window base
    window.iconphoto(False, cls.PhotoImage(file="resources/DQLogo.png"))  # Window icon
    window.geometry(size)  # Window dimensions
    window.resizable(width=False, height=False)  # Can't be resized

    return window


# Add item to receipt and close window
def receipt_add(window, item):

    try:  # Item has an options window

        # Adding item to receipt
        window.master.children["!app"].children["!page"].receipt.add_item(item)

        # Closing window
        window.destroy()

    except KeyError:  # Item does not have an options window

        # Adding item to receipt
        window.master.master.receipt.add_item(item)


# Record item data, add it to the order and close the window
def close_window(window, variables, itemClass):

    # Four parameters
    if itemClass in [cls.Sundae, cls.Cone, cls.Milkshake, cls.Basket]:

        # Creating specifications from data collected
        paramOne, paramTwo, paramThree, paramFour = variables
        item = itemClass(paramOne, paramTwo, paramThree, paramFour)

    # Three parameters
    elif itemClass in [cls.Blizzard, cls.RoyalBlizzard]:

        # Creating specifications from data collected
        paramOne, paramTwo, paramThree = variables
        item = itemClass(paramOne, paramTwo, paramThree)

    # Dual parameter items
    elif itemClass in [cls.BlizzCake, cls.Wrap, cls.Soda, cls.Julius, cls.Misty, cls.Smoothie, cls.Float]:

        # Creating item from specifications
        paramOne, paramTwo = variables
        item = itemClass(paramOne, paramTwo)

    # Single parameter items
    else:

        # Creating item from specifications
        parameter = variables[0]
        item = itemClass(parameter)

    # Adding item to receipt and closing window
    receipt_add(window, item)


# Create options window
def options_window(itemClass, size):

    # Creating window based on size specifications
    window = create_window(size)

    # List of classes and their corresponding option page
    pages = {cls.Soda: cls.BeverageOptions,
             cls.Float: cls.BeverageOptions,
             cls.Julius: cls.BeverageOptions,
             cls.Misty: cls.BeverageOptions,
             cls.Smoothie: cls.BeverageOptions,
             cls.Blizzard: cls.BlizzardOptions,
             cls.RoyalBlizzard: cls.BlizzardOptions,
             cls.Sundae: cls.SundaeOptions,
             cls.Milkshake: cls.ShakeOptions,
             cls.Cone: cls.ConeOptions,
             cls.BlizzCake: cls.BlizzardCakeOptions,
             cls.InsertCake: cls.InsertCakeOptions,
             cls.TreatzaPizza: cls.TreatzaPizzaOptions,
             cls.Fries: cls.SidesOptions,
             cls.OnionRings: cls.SidesOptions,
             cls.PretzelStick: cls.SidesOptions,
             cls.Poutine: cls.SidesOptions,
             cls.Melt: cls.MeltOptions,
             cls.Wrap: cls.WrapOptions,
             cls.Salad: cls.SaladOptions,
             cls.Basket: cls.BasketOptions}

    # Opening adding appropriate page to window
    pageClass = pages[itemClass]  # Finding option page
    pageClass(window, itemClass).pack(expand=True, fill="both")  # Adding option page to screen


# Take payment
def take_payment(parent):

    # Navigate to payment window
    navigate(parent, 2)

    # Trigger order function
    parent.children["!paymentscreen"].take_payment()


# Return
def return_to_menu(parent, tab):

    # Remove all items from the order frame
    items = parent.children["!paymentscreen"].children["!frame"].children  # Order list

    for key in items.copy():
        items[key].destroy()

    # Return to menu page
    navigate(parent, tab)


# Calculate change
def change_calc(change, coins, memo):

    # Base cases ---------------------------------------

    if change in memo:  # If the change combo has already been calculated, do not recalculate
        return memo[change]

    elif change == 0:  # If change is zero, the combo is a sum of 0 of the coins
        return []

    elif change < 0:  # If the change is negative, there is no possible combination
        return None

    shortestCombo = None

    for coin in coins:  # Check each coin

        remainder = change - coin
        remainderCombo = change_calc(remainder, coins, memo)  # Return combos with remainder

        if remainderCombo is not None:  # If a combo exists for the remainder, then add the coin just used to the combo
            combo = remainderCombo.copy()
            combo.append(coin)

            if shortestCombo is None or len(combo) < len(shortestCombo):  # If the new combo is shorter, use it
                shortestCombo = combo

    memo[change] = shortestCombo  # Store the shortest combo in case it needs to be recalculated

    return shortestCombo


# Convert change
def convert_change(coins):

    # Coin totals and corresponding names
    types = [0 for _ in range(8)]
    coinNames = ["Nickels",
                 "Dimes",
                 "Quarters",
                 "Loonies",
                 "Toonies",
                 "Fives",
                 "Tens",
                 "Twenties",
                 "Fifties"]

    # Counting up
    for coin in coins:

        if coin == 5:
            types[0] += 1
        elif coin == 10:
            types[1] += 1
        elif coin == 25:
            types[2] += 1
        elif coin == 100:
            types[3] += 1
        elif coin == 200:
            types[4] += 1
        elif coin == 500:
            types[5] += 1
        elif coin == 1000:
            types[6] += 1
        elif coin == 2000:
            types[7] += 1
        else:
            types[8] += 1

    # Creating string
    string = ""
    for coin, name in zip(types, coinNames):

        if coin != 0:
            string += f"{name}: {coin}\n"

    return string
