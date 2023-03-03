#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity
    
    def to_file(self):
        return f'''{self.country},{self.code},{self.product},{self.cost},{self.quantity}'''

    def __str__(self):
        return f'''----------------
Country: {self.country}
Code: {self.code}
Product: {self.product}
Cost: {self.cost}
Quantity in stock: {self.quantity}
'''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

# File name as global variable
file_name = "inventory.txt"


#==========Functions outside the class==============
def read_shoes_data(): 
    '''
    This function will open the file inventory.txt
    and read the data from this file (by skipping the first line), then create a
    shoes object with this data and append this object into the shoes list. 
    One line in this file represents data to create one object of shoes. 
    '''   
    # Open the file
    try:
        complete_file = open(file_name, "r")
    except:
        raise FileNotFoundError(f"{file_name} was not found or is a directory")

    # Read and manipulate file
    file = complete_file.readlines()[1:]
    for lines in file:
        line = lines.strip()
        item = line.split(",")

        # Give proper names to each attribute
        country = item[0]
        code = item[1]
        product = item[2]
        cost = item[3]
        quantity = item[4]

        # Create shoes object and append it to the shoe_list
        shoes = Shoe(country, code, product, int(cost), int(quantity))
        shoe_list.append(shoes)


def capture_shoes():
    '''
    This function will allow a user to capture data about a shoe and 
    use this data to create a shoe object and append this object inside the shoe list.
    '''
    print("Add another shoe to the stock")

    # Prompt the user for inputs
    country = input("Enter the country: ")
    code = input("Enter the product code: ")
    product = input("Enter the product name: ")
    cost = int(input("Enter how much it costs: "))
    quantity = int(input("Enter how much you will have in stock: "))
    
    # Create shoes object and append it to the shoe_list
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

    # Add to the file
    update_file()


def view_all(): 
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__ function. 
    '''
    for item in shoe_list:
        print(item)


def re_stock(): 
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. 
    '''
    # Starting with the first item in the list of objects to use it as comparison
    lowest_quantity_shoe = shoe_list[0]  

    # Iterate over the items in the shoe_list to find the item with the lowest stock
    for item in shoe_list:
        if (int(item.quantity)) < int(lowest_quantity_shoe.quantity):
            lowest_quantity_shoe = item

    return lowest_quantity_shoe


def add_stock(lowest_quantity_shoe, add_qty):      
    '''
    Gets the shoe object with the lowest quantity of shoes in stock and
    adds a quantity to it, which is a user input.
    It returns the updated quantity in stock.
    '''
    # Iterate over the items in the shoe_list to find the item with the lowest quantity in stock
    # by using the value returned by the function 're_stock'
    # Then adds a specific quantity to it according to user input
    for item in shoe_list:
        if item == lowest_quantity_shoe:
            item.quantity = item.quantity + add_qty
    
    return item.quantity


def update_file():
    '''
    This function will update the file with the new changes using 
    a method called to_file().
    '''
    file_update = open(file_name, "w")
    file_update.write("Country,Code,Product,Cost,Quantity")
    for item in shoe_list:
        file_update.write(f"\n{item.to_file()}")


def search_shoe(code):
    '''
     This function will search for a shoe from the list
     using the shoe code (user input) and return this object so that it will be printed.
    '''   
    for item in shoe_list:
        if item.code == code:
            return item
            

def value_per_item(): 
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for item in shoe_list:
        print(f"Code: {item.code}, Product: {item.product}, Value: ${(item.cost) * (item.quantity)}")


def highest_qty(): 
    '''
    Code determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Starting with the first item in the list of objects to use it as comparison
    highest_quantity_shoe = shoe_list[0]  

    for item in shoe_list:
        if (int(item.quantity)) > int(highest_quantity_shoe.quantity):
            highest_quantity_shoe = item

    print(f"{highest_quantity_shoe.product.upper()} is on sale!")


def menu(): 
    menu = "---------------------\n"
    menu += "\tMENU\n"
    menu += "---------------------\n"
    menu += "'cs' to capture shoes\n"
    menu += "'va' to view all shoes\n"
    menu += "'re' to re-stock\n"
    menu += "'ss' search shoes by code\n"
    menu += "'vi' to display value per item\n"
    menu += "'os' to view shoes on sale\n"
    menu += "'e' to exit"
    print(menu)


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

choice = ""

while choice != "e":
    read_shoes_data()

    # Display menu
    menu()

    # Get user input from the menu
    choice = input(": ").lower()

    
    if choice == "cs":
        capture_shoes()
        

    elif choice == "va":
        view_all()
        

    elif choice == "re":
        lowest = re_stock()
        print(lowest)
        
        add_shoes = input("Do you want to add shoes to the stock? (Y/N): ").upper()
        if add_shoes == "N":
            break

        elif add_shoes == "Y":
            add_qty = int(input("How many do you want to add to the stock? "))
            add_stock(lowest, add_qty)
            update_file()
            

    elif choice == "ss":
        code = input("Enter code: ").upper()
        shoe = search_shoe(code)
        if shoe != None:
            print(shoe)
            
        else:
            print("This code doesn't exist. Try again...")
            

    elif choice == "vi":
        value_per_item()
        

    elif choice == "os":
        highest_qty()
        

    elif choice == "e":
        exit()


    else:
        print(f"'{choice}' is not an option. Please try again...")    
        

