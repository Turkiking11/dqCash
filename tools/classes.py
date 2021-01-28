# Classes and price variables for the DQ menu

# Imports
from datetime import datetime
import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import tools.functions as fxn

# ------------------------------------------ Global Price Vars --------------------------------------------------- #

# Extras
core = 1.09  # Add a blizzard core
nutPrice = 1.25  # Add nuts

# Blizzard prices
miniBliz = 3.99
smallBliz = 4.99
medBliz = 5.99
largeBliz = 6.99
miniRoyBliz = 4.99
smallRoyBliz = 5.99
medRoyBliz = 6.99
largeRoyBliz = 7.99

# Sundae prices
smallSun = 3.49
medSun = 4.29
largeSun = 4.79

# Cone prices
kidCone = 1.99
smallCone = 2.89
medCone = 3.59
largeCone = 3.99
kidConeDip = 2.09
smallConeDip = 3.39
medConeDip = 3.99
largeConeDip = 4.49

# Shake prices
smallShake = 3.99
medShake = 4.29
largeShake = 4.99

# Fry prices
regFry = 2.79
largeFry = 3.49
basketFry = 5.99

# Onion ring prices
regRing = 3.19
largeRing = 6.09
basketRing = 6.09

# Poutine prices
regPoutine = 4.99
largePoutine = 7.99

# Pretzel stick prices
regPretzel = 2.99
largePretzel = 5.49

# Snack prices
meltPrice = 2.99
wrapPrice = 2.99
saladPrice = 2.49

# Soda prices
smallSoda = 1.99
medSoda = 2.19
largeSoda = 2.99

# Misty slush prices
smallMisty = 2.19
medMisty = 2.49
largeMisty = 2.99

# Float prices
smallFloat = 3.99
medFloat = 4.39
largeFloat = 4.99

# Smoothie prices
smallSmoothie = 3.99
medSmoothie = 4.39
largeSmoothie = 4.99

# Julius prices
smallJulius = 3.59
medJulius = 3.99
largeJulius = 4.59

# Cake Prices
logCake = 25.99
treatzaPizza = 15.99
eightBlizzCake = 36.99
tenBlizzCake = 41.99
eightInsertCake = 30.99
tenInsertCake = 35.99

# Baskets
fourPiece = 8.49
sixPiece = 11.49
twelvePiece = 16.49
glaze = 0.40
drink = 1.40

# --------------------------------------------- Soft Serve ------------------------------------------------------- #
softServeFlavours = ["Vanilla", "Chocolate"]


# Soft serve item
class SoftServe:

    sizes = ["S", "M", "L"]  # Sizes

    # Initialize
    def __init__(self, size, flavour, softServe):
        self.size = size  # Size
        self.softServe = softServe  # Soft serve flavour
        self.flavour = flavour  # Item flavour
        self.price = None  # Item price

    # Add object
    def __add__(self, other):
        return self.price + other.price

    # Set flavour
    def set_flavour(self, flavour):
        self.flavour = flavour


# Normal blizzards
class Blizzard(SoftServe):

    flavours = ["Oreo",
                "Strawberry Cheesecake",
                "Cookie Dough",
                "Mint Oreo",
                "Choco Brownie Extreme",
                "Turtles",
                "Reeses Peanut Butter Cups",
                "Skor",
                "Smarties"]  # Flavour list
    sizes = ["Mini", "S", "M", "L"]  # Sizes list

    # Initialize
    def __init__(self, size, flavour, softServe):
        super().__init__(size, flavour, softServe)
        self.flavour = flavour  # Flavour of blizzard
        self.calculate_price()  # Calculate price on initialization
        self.type = "Blizzard"  # Item type

    # Calculate price
    def calculate_price(self):

        if self.size == "S":  # Small
            self.price = smallBliz

        elif self.size == "M":  # Medium
            self.price = medBliz

        elif self.size == "L":  # Large
            self.price = largeBliz

        else:  # Mini
            self.price = miniBliz

    # Print
    def __str__(self):
        return f"{self.flavour} {self.type} ({self.size}) - ${self.price}" \
               f"\n{self.softServe}"


# Royal blizzards
class RoyalBlizzard(Blizzard):

    flavours = ["Reeses PB Brownie",
                "Oreo Fudge"]  # Flavours

    # Initialize
    def __init__(self, size, flavour, softServe):
        super().__init__(size, flavour, softServe)
        self.calculate_price()  # Calculate price on initialization
        self.type = "Royal Blizzard"  # Item type

    # Calculate price
    def calculate_price(self):

        if self.size == "S":  # Small
            self.price = smallRoyBliz

        elif self.size == "M":  # Medium
            self.price = medRoyBliz

        elif self.size == "L":  # Large
            self.price = largeRoyBliz

        else:  # Mini
            self.price = miniRoyBliz


# Sundaes
class Sundae(SoftServe):

    flavours = ["Chocolate",
                "Caramel",
                "Cherry",
                "Strawberry",
                "Pineapple",
                "Hot Fudge"]  # Flavours

    # Initialize
    def __init__(self, size, flavour, softServe, nuts):
        super().__init__(size, flavour, softServe)
        self.nuts = nuts  # Are there nuts added?
        self.type = "Sundae"
        self.calculate_price()  # Calculate price on initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "S":  # Small
            self.price = smallSun

        elif self.size == "M":  # Medium
            self.price = medSun

        else:  # Large
            self.price = largeSun

        if self.nuts != "No nuts":
            self.price += nutPrice

    # Print
    def __str__(self):

        if self.nuts != "No nuts":  # Nuts added
            return f"{self.flavour} {self.type} ({self.size}) - ${self.price}" \
                   f"\n{self.softServe}" \
                   f"\nAdd nuts"

        else:  # No nuts
            return f"{self.flavour} {self.type} ({self.size}) - ${self.price}" \
                   f"\n{self.softServe}"


# Cones
class Cone(SoftServe):

    flavours = ["Chocolate",
                "Churro",
                "Cotton Candy",
                "Plain"]  # Cone dip flavours
    sizes = ["Kid's Cone",
             "S",
             "M",
             "L"]  # Cone sizes

    # Initialize
    def __init__(self, size, flavour, softServe, cup):
        super().__init__(size, flavour, softServe)
        self.cup = cup  # Is cone in a cup (default no)
        self.type = "Cone"  # Item type
        self.calculate_price()  # Calculate price on initialization

    # Calculate price
    def calculate_price(self):

        if self.flavour != "Plain":  # Cone is dipped

            if self.size == "S":  # Small
                self.price = smallCone

            elif self.size == "M":  # Medium
                self.price = medCone

            elif self.price == "L":  # Large
                self.price = largeCone

            else:  # Kid's size
                self.price = kidCone

        else:  # Cone is plain

            if self.size == "S":  # Small
                self.price = smallConeDip

            elif self.size == "M":  # Medium
                self.price = medConeDip

            elif self.price == "L":  # Large
                self.price = largeConeDip

            else:  # Kid's size
                self.price = kidConeDip

    # Print itself
    def __str__(self):

        if self.flavour != "Plain":  # Dipped

            if self.cup != "In a cup":  # In a cone
                return f"{self.flavour} Dipped {self.type} ({self.size}) - ${self.price}" \
                       f"\n{self.softServe}"

            else:  # In a cuo
                return f"{self.flavour} Dipped {self.type} ({self.size}) - ${self.price}" \
                       f"\n{self.softServe}" \
                       f"\nIn a cup"
        else:

            if self.cup != "In a cup":  # In a cone
                return f"{self.flavour} {self.type} ({self.size}) - ${self.price}" \
                       f"\n{self.softServe}"

            else:  # In a cuo
                return f"{self.flavour} {self.type} ({self.size}) - ${self.price}" \
                       f"\n{self.softServe}" \
                       f"\nIn a cup"


# Milkshakes
class Milkshake(SoftServe):

    flavours = ["Chocolate",
                "Vanilla",
                "Hot Fudge",
                "Caramel",
                "Strawberry",
                "Cherry",
                "Pineapple"]  # Flavours

    # Initialize
    def __init__(self, size, flavour, softServe, whipCream):
        super().__init__(size, flavour, softServe)
        self.whipCream = whipCream  # Whipped cream on top?
        self.type = "Milkshake"  # Item type
        self.calculate_price()  # Calculate price on initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "S":  # Small
            self.price = smallShake

        elif self.size == "M":  # Medium
            self.price = medShake

        else:  # Large
            self.price = largeShake

    # Print self
    def __str__(self):
        return f"{self.flavour} {self.type} ({self.size}) - ${self.price}" \
               f"\n {self.softServe}" \
               f"\n {self.whipCream}"


# ------------------------------------------------ Sides --------------------------------------------------------- #


# Base side
class Side:

    # Initialize
    def __init__(self, size):
        self.size = size
        self.price = None
        self.type = None

    # Add
    def __add__(self, other):
        return self.price + other.price

    # Print itself
    def __str__(self):
        return f"{self.type} ({self.size}) - ${self.price}"


# Fries
class Fries(Side):

    sizes = ["R", "L", "Basket"]  # Fry sizes

    # Initialize
    def __init__(self, size):
        super().__init__(size)
        self.type = "Fries"  # Side type
        self.calculate_price()  # Calculate price on initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "R":  # Regular
            self.price = regFry

        elif self.size == "L":  # Large
            self.price = largeFry

        else:  # Basket fry
            self.price = basketFry


# Onion rings
class OnionRings(Side):

    sizes = ["R", "L", "Basket"]  # Onion ring sizes

    # Initialize
    def __init__(self, size):
        super().__init__(size)
        self.type = "Onion rings"  # Side type
        self.calculate_price()  # Calculate price on initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "R":  # Regular
            self.price = regRing

        elif self.size == "L":  # Large
            self.price = largeRing

        else:  # Basket
            self.price = basketRing


# Poutine
class Poutine(Side):

    sizes = ["R", "L"]  # Poutine sizes

    # Initialize
    def __init__(self, size):
        super().__init__(size)
        self.type = "Poutine"  # Item type
        self.calculate_price()  # Calculate price on initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "R":  # Regular
            self.price = regPoutine

        else:  # Large
            self.price = largePoutine


# Pretzel sticks
class PretzelStick(Side):

    sizes = ["3 sticks", "6 sticks"]  # Sizes

    # Initialize
    def __init__(self, size):
        super().__init__(size)
        self.type = "Pretzel sticks"  # Side type
        self.calculate_price()  # Calculate price on initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "3 sticks":  # 3 pretzel sticks
            self.price = regPretzel

        else:  # 6 pretzel sticks
            self.price = largePretzel


# ----------------------------------------------- Snacks --------------------------------------------------------- #

# Melts
class Melt:

    flavours = ["Buffalo", "BBQ"]  # Flavours

    # Initialize
    def __init__(self, flavour):
        self.flavour = flavour  # Sauce
        self.type = "Melt"  # Item type
        self.price = meltPrice  # Price

    # Add itself
    def __add__(self, other):
        return self.price + other.price

    # Print itself
    def __str__(self):
        return f"{self.flavour} {self.type} - ${self.price}"


# Wrap
class Wrap:

    flavours = ["Ranch", "Flame"]

    # Initialize
    def __init__(self, flavour, chicken):
        self.flavour = flavour  # Flame sauce or ranch
        self.chicken = chicken  # Grilled chicken or crispy chicken
        self.type = "Wrap"
        self.price = wrapPrice  # Price

    # Add itself
    def __add__(self, other):
        return self.price + other.price

    # Print itself
    def __str__(self):
        return f"{self.flavour} {self.type} - ${self.price}" \
               f"\n{self.chicken}"


# Side salad
class Salad:

    # Initialize
    def __init__(self, chicken):
        self.chicken = chicken  # Grilled or crispy chicken (default crispy)
        self.type = "Salad"
        self.price = saladPrice  # Price

    # Add itself
    def __add__(self, other):
        return self.price + other.price

    # Print itself
    def __str__(self):
        return f"{self.type} - ${self.price}" \
               f"\n{self.chicken} chicken"


# ----------------------------------------------- Drinks --------------------------------------------------------- #

# Base drink
class Drink:

    sizes = ["S", "M", "L"]  # Drink sizes

    # Initialize
    def __init__(self, size, flavour):
        self.size = size  # Size
        self.flavour = flavour  # Flavour
        self.price = None  # Price
        self.type = None  # Item name

    # Add itself
    def __add__(self, other):
        return self.price + other.price

    # Assign flavour
    def set_flavour(self, flavour):
        self.flavour = flavour

    # Printed
    def __str__(self):
        return f"{self.flavour} {self.type} ({self.size}) - ${self.price}"


# Soda
class Soda(Drink):

    flavours = ["7up",
                "Pepsi",
                "Diet Pepsi",
                "Root Beer",
                "Iced Tea",
                "Orange Crush"]  # Flavours of soda

    # Initialize
    def __init__(self, size, flavour):
        super().__init__(size, flavour)
        self.type = "Soda"  # Item name
        self.calculate_price()  # Calculate price upon initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "S":  # Small
            self.price = smallSoda

        elif self.size == "M":  # Medium
            self.price = medSoda

        else:  # Large
            self.price = largeSoda


# Misty Slush
class Misty(Drink):

    flavours = ["Grape",
                "Cherry",
                "Blue Raspberry",
                "Lemon Lime",
                "Strawberry Kiwi"]  # Flavours

    # Initialize
    def __init__(self, size, flavour):
        super().__init__(size, flavour)
        self.type = "Misty Slush"  # Item type
        self.calculate_price()  # Calculate price upon initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "S":  # Small
            self.price = smallMisty

        elif self.size == "M":  # Medium
            self.price = medMisty

        else:  # Large
            self.price = largeMisty


# Float
class Float(Misty):

    # Initialize
    def __init__(self, size, flavour):
        super().__init__(size, flavour)
        self.type = "Float"  # Item type
        self.calculate_price()  # Calculate price upon initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "S":  # Small
            self.price = smallFloat

        elif self.size == "M":  # Medium
            self.price = medFloat

        else:  # Large
            self.price = largeFloat


# Smoothie
class Smoothie(Drink):

    flavours = ["Mango Pineapple",
                "Strawberry Banana",
                "Strawberry"]  # Flavours

    # Initialize
    def __init__(self, size, flavour):
        super().__init__(size, flavour)
        self.type = "Smoothie"  # Item type
        self.calculate_price()  # Calculate price upon initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "S":  # Small
            self.price = smallSmoothie

        elif self.size == "M":  # Medium
            self.price = medSmoothie

        else:  # Large
            self.price = largeSmoothie


# Julius
class Julius(Drink):

    flavours = ["Orange",
                "Mango Pineapple",
                "Strawberry"]  # Flavours

    # Initialize
    def __init__(self, size, flavour):
        super().__init__(size, flavour)
        self.type = "Julius"  # Item type
        self.calculate_price()  # Calculate price upon initialization

    # Calculate price
    def calculate_price(self):

        if self.size == "S":  # Small
            self.price = smallJulius

        elif self.size == "M":  # Medium
            self.price = medJulius

        else:  # Large
            self.price = largeJulius


# ------------------------------------------------ Cakes --------------------------------------------------------- #

# Blizzard cake
class BlizzCake:

    flavours = ["Reeses Peanut Butter",
                "Cookie Dough",
                "Choco Brownie",
                "Strawberry Cheesecake",
                "Oreo"]  # Blizzard cake flavours
    sizes = ["8 inch", "10 inch"]

    # Initialize
    def __init__(self, size, flavour):
        self.size = size  # 10in or 8in
        self.flavour = flavour
        self.price = None  # Price
        self.type = "Blizzard Cake"
        self.calculate_price()  # Calculate price on initialization

    # Add itself
    def __add__(self, other):
        return self.price + other.price

    # Calculate price
    def calculate_price(self):

        if self.size == "8 inch":  # Eight inch cake
            self.price = eightBlizzCake

        else:  # Ten inch cake
            self.price = tenBlizzCake

    # Print itself
    def __str__(self):
        return f"{self.flavour} {self.type} ({self.size}) - ${self.price}"


# Insert cake
class InsertCake:

    sizes = ["8 inch", "10 inch"]

    # Initialize
    def __init__(self, size):
        self.size = size  # 10in or 8in
        self.price = None  # Price
        self.type = "Insert Cake"  # Item type
        self.calculate_price()  # Calculate price on initialization

    # Add itself
    def __add__(self, other):
        return self.price + other.price

    # Calculate price
    def calculate_price(self):

        if self.size == "8 inch":  # 8 inch
            self.price = eightInsertCake

        else:  # 10 inch
            self.price = tenInsertCake

    # Print itself
    def __str__(self):
        return f"{self.type} ({self.size}) - ${self.price}"


# Treatza pizza
class TreatzaPizza:

    flavours = ["Reeses Peanut Butter",
                "Skor",
                "Choco Brownie",
                "Smarties"]  # All flavours

    # Initialize
    def __init__(self, flavour):
        self.flavour = flavour  # Flavour of instance
        self.price = treatzaPizza  # Price
        self.type = "Treatza Pizza"  # Item type

    # Add itself
    def __add__(self, other):
        return self.price + other.price

    # Print itself
    def __str__(self):
        return f"{self.flavour} {self.type} - ${self.price}"


# Log cake
class LogCake:

    # Initialize
    def __init__(self):
        self.price = logCake  # Price

    # Add itself
    def __add__(self, other):
        return self.price + other.price

    # Print itself
    def __str__(self):
        return f"Log cake - ${self.price}"


# ------------------------------------------------ Baskets --------------------------------------------------------- #

# Chicken strip basket
class Basket:

    dips = ["Ranch",
            "Gravy",
            "Sweet & Sour",
            "Honey Mustard",
            "BBQ",
            "Buffalo",
            "Flame",
            "No dip"]  # List of dips
    glazes = ["Honey BBQ",
              "Sweet & Tangy",
              "Honey Hot",
              "No glaze"]  # List of glazes
    sizes = ["4pc", "6pc", "12pc"]  # Sizes

    # Initialize
    def __init__(self, size, dipSauce, glazeFlavour, beverage):
        self.size = size  # 3pc, 4pc, 6pc or 12pc
        self.glazeFlavour = glazeFlavour  # What glaze flavour (default no glaze)
        self.dipSauce = dipSauce  # What dip flavour (default no dip)
        self.beverage = beverage  # Which drink (default none)
        self.price = None  # Price
        self.type = "Chicken Strip Basket"  # Item type
        self.calculate_price()

    # Add itself
    def __add__(self, other):
        return self.price + other.price

    # Calculate price
    def calculate_price(self):

        if self.size == "4pc":  # 4pc
            self.price = fourPiece

        elif self.size == "6pc":  # 6pc
            self.price = sixPiece

        else:  # 12pc
            self.price = twelvePiece

        # Strips are glazed
        if self.glazeFlavour != "No glaze":
            self.price += glaze

        # Comes with drink
        if self.beverage != "No drink":
            self.price += drink

        # Rounding price since this object seems to have issues with floats
        self.price = round(self.price, 2)

    # Print itself
    def __str__(self):

        string = f"{self.size} {self.type} - ${self.price}" \
                 f"\nFries (R)" \
                 f"\n{self.dipSauce}"

        if self.glazeFlavour != "No glaze":
            string += f"\n{self.glazeFlavour}"

        if self.beverage != "None":
            string += f"\n{self.beverage} (R)"

        return string


# ------------------------------------------------ Tkinter --------------------------------------------------------- #

# Important variables

# Dimensions
height = 900
width = 1600
receiptWidth = 400

# Colours
dqRed = "#ea1c2d"
dqBlue = "#0063a8"
dqOrange = "#f99d1b"
offWhite = "#ede6e6"

# ---------------------- Home Page ----------------------- #


# Home page
class Home(Frame):

    # Initialize
    def __init__(self, master):
        super().__init__(master)

        # Background
        self.configure(background=dqBlue)

        # Create page widgets
        self.createWidgets()

    # Create widgets
    def createWidgets(self):

        # Buttons to navigate to other tabs
        deliveryButton = Button(self,
                                text="Delivery",
                                fg="white",
                                bg=dqRed,
                                font=font.Font(family="Helvetica", size=40),
                                width=10,
                                command=lambda: fxn.navigate(self.master, 1))
        deliveryButton.place(relx=0.5, rely=0.35, anchor=CENTER)

        toGoButton = Button(self,
                            text="To Go",
                            fg="white",
                            bg=dqRed,
                            font=font.Font(family="Helvetica", size=40),
                            width=10,
                            command=lambda: fxn.navigate(self.master, 1))
        toGoButton.place(relx=0.5, rely=0.65, anchor=CENTER)

        eatInButton = Button(self,
                             text="Eat In",
                             fg="white",
                             bg=dqRed,
                             font=font.Font(family="Helvetica", size=40),
                             width=10,
                             command=lambda: fxn.navigate(self.master, 1))
        eatInButton.place(relx=0.5, rely=0.5, anchor=CENTER)


# ----------------------- Receipt ------------------------ #


# Clock (displays time on receipt)
class Clock(Label):

    # Initialize
    def __init__(self, master):
        super().__init__(master)
        self.currentTime = datetime.now().strftime("%A %d %B - %I:%M%p")  # Time when window is launched
        self.configure(text=self.currentTime)  # Set time
        self.configure(font=font.Font(size=16))  # Change font size

    # Update time
    def update_time(self):
        self.currentTime = datetime.now().strftime("%A %d %B - %I:%M%p")  # Getting new time
        self.configure(text=self.currentTime)  # Setting text to current time
        self.after(200, self.update_time)


# Total (displays total of items on receipt)
class Total(Label):

    # Initialize
    def __init__(self, master):
        super().__init__(master)
        self.total = 0  # Total is $0 to start
        self.configure(text=f"Total: ${self.total}")  # Current total displayed ($0 initially)
        self.configure(font=font.Font(size=16))  # Change font size

    # Update total
    def update_total(self, item, add=True):

        if add:
            self.total += item.price  # Add new item to total

        else:
            self.total -= item.price  # Subtract item from price

        self.configure(text=f"Total: ${round(self.total * 1.13, 2):.2f}")  # Display new total (two decimal places)


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


# ----------------------- Payment Screen ------------------------ #


# Payment screen
class PaymentScreen(Frame):

    # Initialize
    def __init__(self, master):
        super().__init__(master)
        self.receipt = self.master.children["!page"].receipt  # Simplify accessing receipt

        # Order frame
        self.orderFrame = Frame(self, bg="white", width=receiptWidth)
        self.orderFrame.pack_propagate(False)  # Don't resize this frame

        # Total frame
        self.totalFrame = Frame(self, bg=offWhite)

        # Total
        self.totalLabel = Label(self.totalFrame, bg=offWhite, font=font.Font(size=100), text="$0.00", pady=100)

        # Create widgets on initialization
        self.createWidgets()

    # Take payment
    def take_payment(self):

        # Adding items to order frame
        for button in self.receipt.items:
            item = self.receipt.items[button]
            Label(self.orderFrame,
                  text=item,
                  font=font.Font(size=12),
                  bg="white").pack()

        # Showing total
        self.totalLabel.configure(text=f"${round(self.receipt.total.total * 1.13, 2):.2f}")

    # Collect input
    def collect_input(self, var):

        # Getting a valid tendered amount -------------------------------------------------------

        cont = False  # Assume invalid
        tendered = 0

        # Convert to float
        try:
            tendered = float(var.get())
            tendered = round(tendered, 2)

            if tendered < 0:  # Float less than zero
                self.totalFrame.children["!entry"].insert(0, "Input a number 0 or higher!")

            else:  # Valid float
                cont = True

        # Not a number
        except ValueError:

            if var.get() == "secret":  # Easter egg
                self.totalFrame.children["!entry"].insert(0, "You've been Dairy Creamed! -Jenn")
            else:
                self.totalFrame.children["!entry"].insert(0, "Input a number!")

        # If valid tender is given -----------------------------------------------------------------
        if cont:

            # Change
            change = tendered - round(self.receipt.total.total * 1.13, 2)  # Subtract total from tendered
            change = int(change * 100)  # Turn change into integer to avoid floating point mistakes
            change -= change % 5  # Round to nearest nickel

            if change > 0:  # Not on card

                try:  # Attempt to find exact amounts for change
                    # Exact coins/bills
                    coins = [5, 10, 25, 100, 200, 500, 1000, 2000, 5000]  # Coins and bills in cents
                    changeInCoins = fxn.change_calc(change, coins, {})  # Find lowest amount of coins for change

                    # Convert change in coins to numbers of coins
                    changeInCoins = fxn.convert_change(changeInCoins)

                except RecursionError:  # If stack exceeded, just display change and have cashier figure it out
                    changeInCoins = ""

                # Remove screen items
                self.orderFrame.destroy()
                self.totalFrame.destroy()

                # Add text displaying change ------------------------------------------------------

                # Heading with instructions
                heading = Label(self,
                                text=f"Return change to customer!\n${(change / 100):.2f}",
                                font=font.Font(size=40),
                                pady=50)
                heading.pack(fill="both")

                # Change amounts
                changeLabel = Label(self,
                                    text=changeInCoins,
                                    font=font.Font(size=20),
                                    pady=10)
                changeLabel.pack(fill="both")

            else:  # On card

                # Delete screen items
                self.orderFrame.destroy()
                self.totalFrame.destroy()

                # Show total
                totalLabel = Label(self,
                                   font=font.Font(size=100),
                                   text=f"${round(self.receipt.total.total * 1.13, 2):.2f}",
                                   pady=50)
                totalLabel.pack()

                # Show instructions
                heading = Label(self,
                                text="Enter total into card machine!",
                                font=font.Font(size=40),
                                pady=50)
                heading.pack()

            # Logo
            dqLogo = PIL.Image.open("resources/DQLogo.png")
            dqLogo = PIL.ImageTk.PhotoImage(dqLogo)
            dqLogoLabel = Label(self, image=dqLogo)
            dqLogoLabel.image = dqLogo
            dqLogoLabel.pack()

    # Create widgets
    def createWidgets(self):

        # Add order frame to screen
        self.orderFrame.pack(side="right", fill="y")

        # Add total frame to screen
        self.totalFrame.pack(expand=True, fill="both", side="left")
        self.totalFrame.columnconfigure(0, weight=5)  # Center the column
        self.totalFrame.rowconfigure(4, weight=5)  # Push the last button down
        self.totalFrame.rowconfigure(3, weight=1)  # Space between button and input field

        # Add total to screen
        self.totalLabel.grid(row=0, column=0)

        # Label for input field
        text = Label(self.totalFrame, text="Amount tendered:", font=font.Font(size=28), bg=offWhite)
        text.grid(row=1, column=0)

        # Input field
        inputField = Entry(self.totalFrame, width=30, bd=4)
        inputField.insert(0, "0.00")  # Default is no tender, for taking cards
        inputField.grid(row=2, column=0)

        # Button to collect input
        inputButton = Button(self.totalFrame,
                             text="Take Payment",
                             pady=30,
                             command=lambda: self.collect_input(inputField),
                             bg=dqRed,
                             fg=offWhite,
                             font=font.Font(size=14))
        inputButton.grid(row=3, column=0)

        # Return button
        returnButton = Button(self.totalFrame,
                              text="Return",
                              pady=15,
                              command=lambda: fxn.return_to_menu(self.master, 1),
                              bg=dqRed,
                              fg=offWhite,
                              font=font.Font(size=14))
        returnButton.grid(row=4, column=0)


# ---------------------- Item Categories ------------------------ #


# Items category page
class Category(Frame):

    # Initialize
    def __init__(self, master):
        super().__init__(master)

        # Background
        self.configure(background=dqBlue)


# Item button
class ItemButton(Button):

    # Initialize
    def __init__(self, master, text, itemClass=None, size=None, command=fxn.options_window):
        super().__init__(master)
        self.text = text  # Button text

        # The command is the default
        if command == fxn.options_window:
            self.command = lambda: command(itemClass, size)  # Button command

        # A different command has been chosen
        else:
            self.command = command

        # Configure
        self.configure(text=text)  # Set text
        self.configure(background=dqOrange)  # Background colour
        self.configure(font=font.Font(family="Helvetica", size=14))  # Font size and style
        self.configure(foreground="white")  # Text colour
        self.configure(width=15)  # Button width
        self.configure(command=self.command)  # Button command


# Custom options button
class OptionButton(Radiobutton):

    # Initialize
    def __init__(self, master, text, value, variable):
        super().__init__(master)

        # Colour and font
        self.configure(background=dqBlue, font=font.Font(size=18))

        # Important parameters
        self.configure(text=text, value=value, variable=variable)


# Options page
class OptionsPage(Frame):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master)
        self.itemClass = itemClass  # Getting class of item to access flavours and sizes, etc

        # Background frame
        self.frame = Frame(self, bg=dqBlue)
        self.frame.pack(fill="both", expand=True)  # Adding frame to screen

    # Create option buttons list
    def create_options(self, variable, iterable, column):

        # Creating options
        buttonArray = []  # List to store radio buttons
        for item in iterable:
            buttonArray.append(OptionButton(self.frame,
                                            text=item,
                                            value=item,
                                            variable=variable))
        # Getting buttons on screen
        for index, button in enumerate(buttonArray):
            button.grid(column=column, row=index)

        # Select first button
        buttonArray[0].select()

    # Quit button
    def quit_button(self, variables, row, column, columnspan=None, pady=None, sticky=None):

        # Quit button
        done = Button(self.frame,
                      text="Done",
                      font=font.Font(size=20),
                      bg=dqRed,
                      fg="white",
                      command=lambda: fxn.close_window(self.master,
                                                       [variable.get() for variable in variables],
                                                       self.itemClass))

        done.grid(row=row, column=column, columnspan=columnspan, pady=pady, sticky=sticky)


# ------------------------------------


# Soft serve page
class SoftServePage(Category):

    # Initialize
    def __init__(self, master):
        super().__init__(master)
        self.blizzWindowSize = "600x450"
        self.royalWindowSize = "500x300"
        self.sundaeWindowSize = "600x450"
        self.shakeWindowSize = "700x400"
        self.coneWindowSize = "650x350"
        self.createWidgets()  # Adding widgets on creation

    # Creating widgets
    def createWidgets(self):

        # Blizzards button
        blizzardsButton = ItemButton(self,
                                     "Blizzards",
                                     Blizzard,
                                     self.blizzWindowSize)
        blizzardsButton.place(x=50, y=50)

        # Royal blizzards button
        royalBlizzardsButton = ItemButton(self,
                                          "Royal Blizzards",
                                          RoyalBlizzard,
                                          self.royalWindowSize)
        royalBlizzardsButton.place(x=350, y=50)

        # Sundae button
        sundaeButton = ItemButton(self,
                                  "Sundaes",
                                  Sundae,
                                  self.sundaeWindowSize)
        sundaeButton.place(x=50, y=250)

        # Cone button
        coneButton = ItemButton(self,
                                "Cones",
                                Cone,
                                self.coneWindowSize)
        coneButton.place(x=350, y=250)

        # Cone button
        shakeButton = ItemButton(self,
                                 "Shakes",
                                 Milkshake,
                                 self.shakeWindowSize)
        shakeButton.place(x=650, y=50)


# Blizzard options page
class BlizzardOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Flavour options
        itemFlavour = StringVar()
        self.create_options(variable=itemFlavour, iterable=self.itemClass.flavours, column=0)

        # Size options
        itemSize = StringVar()
        self.create_options(variable=itemSize, iterable=self.itemClass.sizes, column=1)

        # Soft serve flavour options
        softServe = StringVar()
        self.create_options(variable=softServe, iterable=softServeFlavours, column=2)

        # Quit button
        self.quit_button(variables=[itemSize, itemFlavour, softServe], row=10, column=0, pady=15, columnspan=3)


# Shakes option page
class ShakeOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Flavour options
        itemFlavour = StringVar()
        self.create_options(variable=itemFlavour, column=0, iterable=self.itemClass.flavours)

        # Size options
        itemSize = StringVar()
        self.create_options(variable=itemSize, column=1, iterable=self.itemClass.sizes)

        # Soft serve options
        softServe = StringVar()
        self.create_options(variable=softServe, column=2, iterable=softServeFlavours)

        # Whipped cream options
        whipCream = StringVar()
        self.create_options(variable=whipCream, column=3, iterable=["Whipped cream", "No whipped cream"])

        # Add quit button
        self.quit_button([itemSize, itemFlavour, softServe, whipCream], len(self.itemClass.flavours), 0, columnspan=5)


# Sundae option page
class SundaeOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Flavour options
        itemFlavour = StringVar()
        self.create_options(variable=itemFlavour, iterable=self.itemClass.flavours, column=0)

        # Size options
        itemSize = StringVar()
        self.create_options(variable=itemSize, iterable=self.itemClass.sizes, column=1)

        # Soft serve flavour options
        softServe = StringVar()
        self.create_options(variable=softServe, iterable=softServeFlavours, column=2)

        # Add nuts option
        nuts = StringVar()
        self.create_options(variable=nuts, iterable=["Add nuts", "No nuts"], column=3)

        # Quit button
        self.quit_button(variables=[itemSize, itemFlavour, softServe, nuts],
                         row=len(self.itemClass.flavours),
                         column=0,
                         columnspan=4)


# Cone option page
class ConeOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Cone dip flavour options
        itemFlavour = StringVar()
        self.create_options(variable=itemFlavour, iterable=self.itemClass.flavours, column=0)

        # Size options
        itemSize = StringVar()
        self.create_options(variable=itemSize, iterable=self.itemClass.sizes, column=1)

        # Soft serve options
        softServe = StringVar()
        self.create_options(variable=softServe, iterable=softServeFlavours, column=2)

        # In a cup or in a cone
        cup = StringVar()
        self.create_options(variable=cup, iterable=["In a cup", "In a cone"], column=3)

        # Quit button
        self.quit_button(variables=[itemSize, itemFlavour, softServe, cup],
                         row=len(self.itemClass.flavours),
                         column=0,
                         columnspan=4,
                         pady=25)


# ------------------------------------


# Basket/Sides page
class BasketPage(Category):

    # Initialize
    def __init__(self, master):
        super().__init__(master)
        self.friedWindowSize = "150x200"
        self.sideWindowSize = "150x170"
        self.meltWindowSize = "150x170"
        self.wrapWindowSize = "230x170"
        self.saladWindowSize = "150x170"
        self.basketWindowSize = "700x500"
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Fries button
        friesButton = ItemButton(self,
                                 "Fries",
                                 Fries,
                                 self.friedWindowSize)
        friesButton.place(x=50, y=50)

        # Poutine button
        poutineButton = ItemButton(self,
                                   "Poutine",
                                   Poutine,
                                   self.sideWindowSize)
        poutineButton.place(x=350, y=50)

        # Onion ring button
        onionButton = ItemButton(self,
                                 "Onion Rings",
                                 OnionRings,
                                 self.friedWindowSize)
        onionButton.place(x=50, y=250)

        # Pretzel stick button
        pretzelButton = ItemButton(self,
                                   "Pretzel Sticks",
                                   PretzelStick,
                                   self.sideWindowSize)
        pretzelButton.place(x=350, y=250)

        # Melt button
        meltButton = ItemButton(self,
                                "Snack Melts",
                                Melt,
                                self.meltWindowSize)
        meltButton.place(x=50, y=450)

        # Wrap button
        wrapButton = ItemButton(self,
                                "Wraps",
                                Wrap,
                                self.wrapWindowSize)
        wrapButton.place(x=350, y=450)

        # Salad button
        wrapButton = ItemButton(self,
                                "Side Salad",
                                Salad,
                                self.saladWindowSize)
        wrapButton.place(x=650, y=450)

        # Chicken strip baskets button
        basketButton = ItemButton(self,
                                  "Chicken Strips",
                                  Basket,
                                  self.basketWindowSize)
        basketButton.place(x=50, y=650)


# Sides options page
class SidesOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Size options
        itemSize = StringVar()
        self.create_options(variable=itemSize, iterable=self.itemClass.sizes, column=0)

        # Quit button
        self.quit_button(variables=[itemSize], row=len(self.itemClass.sizes), column=0, pady=15)


# Melt options page
class MeltOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Flavour
        itemFlavour = StringVar()
        self.create_options(variable=itemFlavour, iterable=self.itemClass.flavours, column=0)

        # Quit button
        self.quit_button(variables=[itemFlavour], row=len(self.itemClass.flavours), column=0, pady=15)


# Wraps option page
class WrapOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Flavour options
        itemFlavour = StringVar()
        self.create_options(variable=itemFlavour, iterable=self.itemClass.flavours, column=0)

        # Chicken options
        chicken = StringVar()
        self.create_options(variable=chicken, iterable=["Crispy", "Grilled"], column=1)

        # Quit button
        self.quit_button(variables=[itemFlavour, chicken],
                         row=len(self.itemClass.flavours),
                         column=0,
                         columnspan=2,
                         pady=15)


# Salad options page
class SaladOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Chicken options button
        chicken = StringVar()
        self.create_options(variable=chicken, iterable=["Crispy", "Grilled"], column=0)

        # Quit button
        self.quit_button(variables=[chicken], row=3, column=0, pady=15)


# Basket options page
class BasketOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Sizes
        itemSize = StringVar()
        self.create_options(variable=itemSize, iterable=self.itemClass.sizes, column=0)

        # Glaze flavours
        glazeFlavour = StringVar()
        self.create_options(variable=glazeFlavour, iterable=self.itemClass.glazes, column=1)

        # Dip flavours
        dip = StringVar()
        self.create_options(variable=dip, iterable=self.itemClass.dips, column=2)

        # With drink
        beverage = StringVar()
        beverageFlavours = Soda.flavours
        beverageFlavours.append("None")
        self.create_options(variable=beverage, iterable=beverageFlavours, column=3)

        # Quit button
        self.quit_button(variables=[itemSize, dip, glazeFlavour, beverage],
                         row=len(self.itemClass.dips),
                         column=0,
                         pady=15,
                         columnspan=4)


# ------------------------------------


# Beverages page
class BeveragePage(Category):

    # Initialize
    def __init__(self, master):
        super().__init__(master)
        self.windowSize = "400x400"  # Size for pop up window
        self.createWidgets()  # Add widgets to page on initialization

    # Create widgets
    def createWidgets(self):

        # Soda button
        sodaButton = ItemButton(self,
                                "Soda",
                                command=lambda: fxn.options_window(Soda, self.windowSize))
        sodaButton.place(x=50, y=50)

        # Misty slush button
        mistyButton = ItemButton(self,
                                 "Misty Slush",
                                 command=lambda: fxn.options_window(Misty, self.windowSize))
        mistyButton.place(x=350, y=50)

        # Float button
        floatButton = ItemButton(self,
                                 "Float",
                                 command=lambda: fxn.options_window(Float, self.windowSize))
        floatButton.place(x=650, y=50)

        # Smoothie button
        smoothieButton = ItemButton(self,
                                    "Smoothie",
                                    command=lambda: fxn.options_window(Smoothie, self.windowSize))
        smoothieButton.place(x=50, y=250)

        # Julius button
        juliusButton = ItemButton(self,
                                  "Julius",
                                  command=lambda: fxn.options_window(Julius, self.windowSize))
        juliusButton.place(x=350, y=250)


# Beverage options page
class BeverageOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Flavour options
        itemFlavour = StringVar()  # Storage variable
        self.create_options(variable=itemFlavour, column=0, iterable=self.itemClass.flavours)

        # Size options
        itemSize = StringVar()  # Storage variable
        self.create_options(variable=itemSize, column=1, iterable=self.itemClass.sizes)

        # Quit button
        self.quit_button(variables=[itemSize, itemFlavour], row=10, column=0, columnspan=3, pady=15, sticky="E")


# ------------------------------------


# Cake page
class CakePage(Category):

    # Initialize
    def __init__(self, master):
        super().__init__(master)
        self.blizzCakeWindowSize = "450x350"
        self.insertCakeWindowSize = "200x200"
        self.treatzaWindowSize = "300x300"
        self.createWidgets()  # Add widgets to page on initialization

    # Create widgets
    def createWidgets(self):

        # Blizzard cake button
        blizzCakeButton = ItemButton(self,
                                     "Blizzard Cakes",
                                     BlizzCake,
                                     self.blizzCakeWindowSize)
        blizzCakeButton.place(x=50, y=50)

        # Insert cake button
        insertCakeButton = ItemButton(self,
                                      "Insert Cakes",
                                      InsertCake,
                                      self.insertCakeWindowSize)
        insertCakeButton.place(x=350, y=50)

        # Log cake button
        logCakeButton = ItemButton(self,
                                   "Log Cake",
                                   command=lambda: fxn.receipt_add(self, LogCake()))
        logCakeButton.place(x=50, y=250)

        # Treatza pizza button
        treatzaButton = ItemButton(self,
                                   "Treatza Pizzas",
                                   TreatzaPizza,
                                   self.treatzaWindowSize)
        treatzaButton.place(x=350, y=250)


# Blizzard cake options page
class BlizzardCakeOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Flavour options
        itemFlavour = StringVar()
        self.create_options(variable=itemFlavour, iterable=self.itemClass.flavours, column=0)

        # Size options
        itemSize = StringVar()
        self.create_options(variable=itemSize, iterable=self.itemClass.sizes, column=1)

        # Quit button
        self.quit_button(variables=[itemSize, itemFlavour],
                         row=len(self.itemClass.flavours),
                         column=0,
                         columnspan=2,
                         pady=15)


# Insert cake options page
class InsertCakeOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Size buttons
        itemSize = StringVar()
        self.create_options(variable=itemSize, iterable=self.itemClass.sizes, column=0)

        # Quit button
        self.quit_button(variables=[itemSize], row=3, column=0, pady=25)


# TreatzaPizza options page
class TreatzaPizzaOptions(OptionsPage):

    # Initialize
    def __init__(self, master, itemClass):
        super().__init__(master, itemClass)
        self.createWidgets()  # Create widgets on initialization

    # Create widgets
    def createWidgets(self):

        # Size buttons
        itemFlavour = StringVar()
        self.create_options(variable=itemFlavour, iterable=self.itemClass.flavours, column=0)

        # Quit button
        self.quit_button(variables=[itemFlavour], row=len(self.itemClass.flavours), column=0, pady=25)


# ------------------------ Sub-page Components -------------------------- #
# ---------------------- Delivery, To Go, Eat In  ----------------------- #


# Menu frame
class MenuFrame(Frame):

    # Initialize
    def __init__(self, master):
        super().__init__(master, width=80, height=height)

        # Background colour
        self.configure(background=dqBlue)


# Main screen with items
class Items(ttk.Notebook):

    # Initialize
    def __init__(self, master):
        super().__init__(master)

        # Category pages
        self.softServe = SoftServePage(self)
        self.baskets = BasketPage(self)
        self.beverages = BeveragePage(self)
        self.cakes = CakePage(self)

        # Add widgets on creation
        self.createWidgets()

    # Adding tabs
    def createWidgets(self):

        # Adding pages to notebook
        self.add(self.softServe, text="Soft Serve")
        self.add(self.baskets, text="Baskets/Sides")
        self.add(self.beverages, text="Beverages")
        self.add(self.cakes, text="Cakes")


# Standard page
class Page(Frame):

    # Initialize
    def __init__(self, master):
        super().__init__(master)
        self.receipt = Receipt(self)
        self.menuFrame = MenuFrame(self)
        self.itemScreen = Items(self)

        # Background colour
        self.configure(background=dqBlue)

        # Create page widgets
        self.createWidgets()

    # Create widgets
    def createWidgets(self):

        # Frame for menu buttons
        self.menuFrame.pack(side="left", fill="y")

        # Frame to show receipt
        self.receipt.pack(side="right")

        # Middle item screen
        self.itemScreen.pack(side="right", expand=True, fill="both")

        # Button to quit to home page
        quitButton = Button(self.menuFrame,
                            text="Quit",
                            bg=dqRed,
                            fg="white",
                            font=font.Font(family="Helvetica", size=20),
                            command=lambda: fxn.navigate(self.master, 0))
        quitButton.pack(expand=True, fill="both")

        # Button for soft serve
        softServeButton = Button(self.menuFrame,
                                 text="Soft Serve",
                                 bg=dqRed,
                                 fg="white",
                                 font=font.Font(family="Helvetica", size=20),
                                 command=lambda: fxn.navigate(self.itemScreen, 0))
        softServeButton.pack(expand=True, fill="both")

        # Button for baskets and sides
        basketButton = Button(self.menuFrame,
                              text="Baskets/Sides",
                              bg=dqRed,
                              fg="white",
                              font=font.Font(family="Helvetica", size=20),
                              command=lambda: fxn.navigate(self.itemScreen, 1))
        basketButton.pack(expand=True, fill="both")

        # Button for beverages
        beverageButton = Button(self.menuFrame,
                                text="Beverages",
                                bg=dqRed,
                                fg="white",
                                font=font.Font(family="Helvetica", size=20),
                                command=lambda: fxn.navigate(self.itemScreen, 2))
        beverageButton.pack(expand=True, fill="both")

        # Button for cakes
        cakeButton = Button(self.menuFrame,
                            text="Cakes",
                            bg=dqRed,
                            fg="white",
                            font=font.Font(family="Helvetica", size=20),
                            command=lambda: fxn.navigate(self.itemScreen, 3))
        cakeButton.pack(expand=True, fill="both")

        # Button for taking payment
        payButton = Button(self.menuFrame,
                           text="Take Payment",
                           bg=dqRed,
                           fg="white",
                           font=font.Font(family="Helvetica", size=20),
                           command=lambda: fxn.take_payment(self.master))
        payButton.pack(expand=True, fill="both")


# -------------------------- Main Application  --------------------------- #


class App(ttk.Notebook):

    # Initialize
    def __init__(self, master):
        super().__init__(master)

        # Setting notebook to have no tab bar
        ttk.Style().layout("TNotebook.Tab", [])

        # Adding pages
        self.add(Home(self))  # Home page (delivery, to go, eat in options)
        self.add(Page(self))  # Secondary page (show item roster, receipt)
        self.add(PaymentScreen(self))  # Screen to take order payment
