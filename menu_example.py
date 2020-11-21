
def showMenu():
    while True:
            try:
                user_order = int(input(f"Please, select an option (1, 2 or 3):\n1.Add new order\n2.List orders\n3.Exit\n>> "))
                if user_order == 1:
                    inputOrder()
                    break
                elif user_order == 2:
                    orderList()
                    break
                elif user_order == 3:
                    print("Thank you for your order!")
                    break
                else:
                    print("Invalid option. Please enter 1, 2 or 3\n>>")
                    showMenu()
            except ValueError:
                print("Invalid option. Please enter 1, 2 or 3\n>>")
    exit 
def checkMenu():
    try:
        with open ("orders.txt", "r") as check:
            check.read()
            print("Welcome to 'MacHackburger'! Please, check our menu :)")
            showMenu()    
    except FileNotFoundError:
        print("Critical error occured.\nPlease, contact helpdesk at 555 555 555.")     
def inputOrder():
    with open("orders.txt", "a") as file:
        try:
            name = str(input("Enter customer's name\n>>"))
            burgers = int(input("Enter amount of burgers\n>>"))
            fries = int(input("Enter amount of fries\n>>"))
            coke = int(input("Enter amount of coke\n>>"))
            order = (f"{name}|{burgers}|{fries}|{coke}\n")
            file.write(order)
        except:
            print("Invalid input. Please, enter right amount.\n")
            inputOrder()            
    showMenu()
def orderList():
    try:
        with open("orders.txt", "r") as order_list:
            counter = 0
            for lines in order_list.readlines():
                counter+=1
                n, b, f, c = lines.strip().split("|")
                show_list = (f"{counter}. {n}, \t{b} Burgers, {f} Fries, {c} Cokes")
                print(show_list)
    except:
        print("No orders recorded.")        
    showMenu()
checkMenu()
