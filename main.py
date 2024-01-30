from read import print_laptops, laptops

from write import write_to_file_sale, write_to_file_purchase


while True:
    print("****************************************************")
    print("              Welcome to PC HUB!         ")
    print("****************************************************")
    print("|===================================================|")
    print("|  S.N       |         Option you have              |")
    print("|===================================================|")
    print("|    1       |        Display all laptops           |")
    print("|    2       |          Sell a laptop               |")
    print("|    3       |         Purchase a laptop            |")
    print("|    4       |              EXIT                    |")
    print("|===================================================|")

    try:
        
        Option = int(input("Enter the number of your preferred selection: "))
        if Option == 1:
            print_laptops(laptops)
        elif Option == 2:
            write_to_file_sale()
        elif Option == 3:
            write_to_file_purchase()
        elif Option == 4:
            break
        else:
            
            print('The number you entered is invalid. Please select valid option.')
    except ValueError:
        
        # Handle invalid input
        print('Invalid input detected. Please select again.')

