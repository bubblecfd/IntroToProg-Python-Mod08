# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Tao Ye,6.2.2020,Modified code to complete assignment 8
# Tao Ye,6.3.2020,revision
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ""

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Tao Ye,6.2.2020,Modified code to complete assignment 8
    """
    pass

    # Constructor -----------------
    def __init__(self):
        self.__product_name = ""
        self.__product_price = 0.0

    # Properties ------------------
    # product_name
    @property               # (getter or accessor)
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter    # (setter or mutator)
    def product_name(self, name):
            self.__product_name = name

    # product_price
    @property               # (getter or accessor)
    def product_price(self):
        return self.__product_price

    @product_price.setter   # (setter or mutator)
    def product_price(self, value):
        self.__product_price = value
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Tao Ye,6.3.2020,Modified code to complete assignment 8
    """
    pass

    @staticmethod
    def read_data_from_file(file_name):
        """
        Desc - Reads data from a file into a list of products

        :param file_name: (string) with name of file
        :return: (list) of product objects
        """

        list_of_objects=[]
        try:
            file = open(file_name, "r")
            for line in file:
                objProduct = Product()  # create an object of Product class
                data = line.split(",")  # data has the list of name and price strings
                objProduct.product_name = data[0]
                objProduct.product_price = float(data[1])
                list_of_objects.append(objProduct)  # add the object to the list
            file.close()
            return list_of_objects
        except FileNotFoundError:
            print("File", file_name, "does not exist yet.")
            return list_of_objects

    @staticmethod
    def save_data_to_file(file_name, list_of_objects):
        """
        Desc - Save a list of products to a file

        :param file_name: (string) with name of file
        :param list_of_objects: (list) you want to save to the file
        """
        file = open(file_name, "w")
        for objProduct in list_of_objects:
            file.write(objProduct.product_name + "," + str(objProduct.product_price) + "\n")
        file.close()
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for perform Input and Output

    methods:
        OutputMenuItems():
        InputMenuChoice():
        ShowCurrentObjectsInList(list_of_objects):
        InputProductAndPrice():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Tao Ye,6.3.2020,Modified code to complete assignment 8
    """
    pass

    @staticmethod
    def OutputMenuItems():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new product data.
        3) Save Data to File and Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentObjectsInList(list_of_objects):
        """ Shows the current list of products

        :param list_of_objects: (list) of product objects you want to display
        :return: nothing
        """
        print("******* The current product lists are: *******")
        for objProduct in list_of_objects:
            print(objProduct.product_name + " (price: " + str(objProduct.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def InputProductAndPrice():
        """ Ask the user to enter product name and price

        :param none:
        :return: (string) product name and price
        """
        product = input("What is the product? - ").strip()

        while True:  # Ask user for price as a floating number
            try:
                price = float(input("What is the price? - ").strip())
                break
            except ValueError:
                print("Price must be a floating number; try again...")
                continue
        return product, price
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# When the program starts, Load data from products.txt.
# If the file already exists, load data from the file

lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

# Display a menu of choices to the user
while True:
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Process user's menu choice
    if (strChoice.strip() == '1'):      # Show current list of product objects
        IO.ShowCurrentObjectsInList(lstOfProductObjects)
        continue  # to show the menu

    elif (strChoice.strip() == '2'):    # Add a new product to the list of the objects
        # Ask user for new product and price
        strProduct, floatPrice = IO.InputProductAndPrice()
        print()  # Add an extra line for looks

        # Add new object to the List
        objProduct = Product()  # A new product object
        objProduct.product_name = strProduct    # setter property for product_name
        objProduct.product_price = floatPrice   # setter property for product_price
        lstOfProductObjects.append(objProduct)  # add the new object to the list

        # Show current list of product objects
        IO.ShowCurrentObjectsInList(lstOfProductObjects)
        continue  # to show the menu

    elif (strChoice.strip() == '3'):    # save the data to the file and exit
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        input("Data saved to file! Press the [Enter] key to return to exit.")
        break   # exit

    else:
        print("Invalid choice; try again...")
        continue
# Main Body of Script  ---------------------------------------------------- #