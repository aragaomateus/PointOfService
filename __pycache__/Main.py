''' Creating the restaurant pos program in python'''
from Table import Table

# Function for initializing the table objects assingning a number to it.
def initiateTables():
    tablesGrid = [Table(i) for i in range(21)]
    return tablesGrid

# Function for printing the floor map when needed.
def printTables(tables):
    for i in range(1,21):
        print(f'{tables[i].getNumber():2}', end = " | ")
        if i == 5 or i == 10 or i == 15 or i == 20:
            print("\n")

def mainMenu(tables):
    printTables(tables)
    option = input("a - Add Table:\no - Open Table:\n")
    return option


def main ():
    # variables declaration and initializations
    tables = initiateTables() 
    userPasswords = []
    userPasswords.append(1234)

    '''
    First page:
        Enter your password: '''
    password = 0

    while password not in userPasswords:
        password = int(input("Enter your password"))
        if password not in userPasswords:
            print("Wrong password type again")
            
    option = mainMenu(tables)

    if option == 'a':
        print("Opening add table...")
    elif option == 'o':
        print("Opening open table...")

    


    '''
        Main Menu view:
            a - Add Table:
                number of the table:
                number of people in the table:
                    Adding order to the table: for each seat: 
                    {print out the orders}
            o - Open Table:
                a - Add new order
                v - View orders
                p - print bill
    '''
main()
