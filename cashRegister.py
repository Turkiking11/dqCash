# DQ cash register

# Imports
from tools.classes import *  # Classes (contains tkinter too)

# Main root
root = Tk()
root.title("DQ Cash Register")  # Window title
root.iconphoto(False, PhotoImage(file="resources/DQLogo.png"))  # Window icon
root.geometry("1600x900")  # Window size, in standard computer aspect ratio
root.resizable(width=False, height=False)  # Not resizable

# Home Screen
homeScreen = App(root)
homeScreen.pack(expand=True, fill="both")

# Main loop for root
root.mainloop()
