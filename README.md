# DQ Cash Register

This program serves as a very basic recreation of the cash register system from Dairy Queen. It was my first attempt at
creating a GUI, and is meant to use concepts from my grade twelve computer science course. This documentation will [lay
out use](#how-to-use), some features, and how they relate to the [computer science concepts](#concepts-utilized) from 
this year's course.

## How to use

### Order Options
Food can be ordered as take out, eat in and delivery. Pressing any of the buttons will take you to a menu page, where
you can begin to fill out the order.

### Side Menu
On the left side of the screen, there is a menu bar with several navigation buttons. The first one is quit, which will
return you to the opening screen and allow you to choose a new order option. This does not clear the order list, it just
lets you return to change the order options.

The last button takes the payment, and will bring you to a new screen which is explained in 
[Payment Screen](#payment-screen).

All the buttons in between will change the [item menu](#item-menu) display to their corresponding section. For instance,
the "Cakes" but will trigger the cake selection to appear.

### Item Menu
The item menu takes up the center portion of the page screen. It is a notebook style frame, so it can switch dynamically
between categories without changing the [Side Menu](#side-menu) or the [Receipt](#receipt). This item menu will display
buttons for each individual item. Once clicked, they will open their corresponding [Option Page](#options-page), where
specifications can be made

### Receipt
The receipt is a white frame on the right side of the screen, designed to look like an actual receipt. It displays the
time at it's top, the order total at the bottom, and all the items in the order and their specifications in between.

To remove items from the order at any time, just click the item's name on the receipt. This will trigger the item to
delete itself, and its appearance on the receipt.

The receipt has an order limit of 12 items to prevent items from exceeding the display of the frame. Adding more items
will result in a warning pop-up, and they will not be added to the list or total.

### Options Page
The options page is a pop-up window that opens when its corresponding item button is clicked. It will display all the
item's specification options as Tkinter radio buttons (they look like multiple choice options for those of you who don't
speak code). It also contains a **_Done_** button which must be clicked in order to add the item to the receipt. The
traditional **_X_** to close button will just cancel the addition.

There is one item, the log cake, which does not have any specific options. Clicking that button will just add it to the
receipt directly.

The first option is always selected by default to prevent errors in trying to get values from empty variables.

### Payment Screen
The payment screen displays the order total in a larger size, as well as the order list on the right of the screen.
There is an input field to take the amount tendered. A return button is also displayed in case the cashier must make
changes in the order before collecting payment.

The **_Take Payment_** button must be clicked in order to collect the data from the input field. Hitting enter doesn't
do anything. Once this button is clicked, the order is final. The screen elements will disappear and be replaced with
instructions and the DQ logo.

If the amount tendered is lower than the amount due, the program will assume that the customer is paying by card, and 
it will display the total with the instructions "enter total into the card machine".

If the amount tendered is higher than the total, the program will display the change due as well as the least amount of
coins that make up the change total, using a [recursive algorithm](#recursion). If the recursion depth is exceeded 
because the amount of change is too large, only the change total will be displayed with the instructions of "return 
change to customer".

Once the program has calculated the change, you must click the **_X_** in order to terminate it, as there is no
navigation from the final page.

## Concepts Utilized

### UML Diagrams / Project Planning
In order to plan the concept for this program, I created a UML Diagram to plan all the attributes that each food item
would have (i.e., shakes will have a size, flavour, soft serve flavour, and an option for whipped cream). Because I was
referencing the pre-existing Dairy Queen cash register from my part-time job, I neglected to create rough sketches of
the GUI design or create UML diagrams for the GUI components (i.e., I already knew that the receipt should display time,
and have a method to delete items, as the DQ cash register already had such features implemented).

[The project planning can be viewed here.](https://www.notion.so/DQ-Cash-Register-9e622cc09ab4461b83a55a1c9f289d72)

### Object-Oriented Programming (OOP)
This entire program makes heavy use of OOP concepts taught in the grade twelve course. Because Tkinter is a program that
makes heavy use of highly customizable classes for GUI elements, it's best to tackle GUI building using a sub-class
approach, instead of defining a long list of variables for all the elements.

I organized my GUI using classes, with each page getting its own class that contains methods to add elements, its base
elements as attributes, etc. There is a hierarchical structure to the GUI layout that is better visualized by using
classes than by using variables.

For example, the receipt frame has its own class, with attributes for the total and the clock. The total and the clock
are their own classes as well, because the total requires a method to update itself when an item is added, and the clock
must update its time display after a certain period. The receipt also has its own methods to add and remove items.

```python
# Receipt
class Receipt(Frame):

    # Initialize
    def __init__(self, master):
        super().__init__(master, width=receiptWidth, height=height)
        self.pack_propagate(False)  # Don't resize when widgets are added
        self.timeStamp = Clock(self)  # Clock for top of receipt
        self.total = Total(self)  # Total tracker
        self.items = {}  # List of items in the order
        self.createWidgets()  # Add widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Add time to top of receipt
        self.timeStamp.pack(side="top")  # Add clock to top
        self.timeStamp.update_time()  # Update every 200ms

        # Add total to bottom of receipt
        self.total.pack(side="bottom")

    # Remove an item
    def remove_item(self, button):

        # Remove from total
        item = self.items[button]
        self.total.update_total(item, add=False)

        # Remove from list
        self.items.pop(button)

        # Delete button
        button.destroy()

    # Add an item
    def add_item(self, item):

        if len(self.items) < 12:  # Order limit of 12 items

            # Make button
            button = Button(self,
                            text=item,
                            font=font.Font(size=12),
                            bd=0)

            button.configure(command=lambda: self.remove_item(button))  # Add command after creation to pass button object

            button.pack()  # Add button to screen

            # Add item and corresponding button to list
            self.items[button] = item

            # Update the total
            self.total.update_total(item)

        else:

            messagebox.showwarning(title="Order Limit",
                                   message="Order limit exceeded! You have added the max number of items.")
```

In addition to just GUI elements, the items themselves have multiple attributes and are therefore designed as objects.
These include price, the item name, their size, flavours, etc. Items also contain methods, such as one to calculate 
their price based on their size, a method for when they're converted to a string, and a method to add themselves to
other objects for price totalling.

Essentially all components of this program are built from classes, except the functions module.

### Math Functions

This program made use of some math functions from the grade twelve course in order to perform some basic operations on
the item total. This includes the use of the `round()` function and the `%` (modulo) function. These were used to round
the item prices to two decimals (as floats are unpredictable), as well as round the item total to the nearest nickel for
cash transactions.

```python
# Change
change = tendered - round(self.receipt.total.total * 1.13, 2)  # Subtract total from tendered
change = int(change * 100)  # Turn change into integer to avoid floating point mistakes
change -= change % 5  # Round to nearest nickel
```

### Recursion
This program also made use of a recursive algorithm, commonly known as **_Best Sum_** in dynamic programming, to
calculate the lowest combination of coins the cashier should use to return the customer's change. Unfortunately this
cannot handle large change numbers because of the number of coins the algorithm uses, so if the stack is exceeded the 
program just shows the change total by itself.

This issue could have been solved by using the tabulated version of the algorithm, but it would not have demonstrated 
knowledge of the recursive concepts learned in the grade twelve course. Additionally, if the calculation took more than
a second, it would make the GUI appear slow, which is an unwanted outcome.

**The Recursive Best Sum Algorithm**
```python
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
```