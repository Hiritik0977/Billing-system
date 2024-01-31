from read import laptops

L_sold = {}
#  function

def sell(laptops, L_sold):
    print("Available laptops:")
    while True:
        try:
            for i, name in enumerate(laptops.keys()):
                print(str(i+1) + ". " + name)
            Choice= int(input("Select the S.N of the laptop you want to sell to the customer: "))
            if 1 <= Choice<= len(laptops):
                L_Name = list(laptops.keys())[Choice- 1]
                laptop = laptops[L_Name]
                laptop_ram = laptop['ram']
                L_Price = laptop['price']
                print("\nSpecifications of the " + L_Name + " are:")
                print("--------------------------------------------------------")
                print("Brand: " + laptop['brand'])               
                print("RAM: " + str(laptop['ram']) + " GB")
                print("GPU: " + laptop['gpu'])
                print("Price: $" + str(laptop['price']))
                print("Availability: " + str(laptop['available_laptop']))
                
                while laptop['available_laptop'] == 0:
                    print(f"Sorry, {L_Name} laptop is currently unavailable.")
                    for i, name in enumerate(laptops.keys()):
                        print(str(i+1) + ". " + name)
                    Choice= int(input("Select the S.N of the laptop you want to sell to the customer:"))
                    L_Name = list(laptops.keys())[Choice- 1]
                    laptop = laptops[L_Name]
                    print(f"\nSpecifications of the {L_Name} laptop:")
                    print("--------------------------------------------------------")
                    print(f"Brand: {laptop['brand']}")
                    print(f"RAM: {laptop['ram']} GB")
                    print(f"GPU: {laptop['gpu']}")
                    print(f"Price: ${laptop['price']}")
                    print(f"Availability: {laptop['available_laptop']}")

                while True:
                    try:
                        Quantity = int(input("Please enter the quantity you like to sell. "))
                        if Quantity <= laptop['available_laptop']:
                            L_sold[L_Name] = {'price': L_Price, 'quantity': Quantity}
                            laptops[L_Name]['available_laptop'] -= Quantity
                            with open("laptops.txt", "w") as file:
                                for name, details in laptops.items():
                                    file.write(f"{name}, {details['brand']}, ${details['price']}, {details['available_laptop']}, {details['ram']}, {details['processor']}, {details['gpu']}\n")
                            file.close()
                            print("Sold " + str(Quantity) + " " + L_Name + " laptops for $" + str(Quantity * L_Price) + ".")
                            break
                        else:
                            print("Sorry, only " + str(laptop['available_laptop']) + " " + L_Name + " laptops are available.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        
                        
                while True:
                    try:
                        Continue = input("Would you like to sell another  laptop? (y/n) ")
                        if Continue == 'n':
                            return
                        elif Continue == 'y':
                                    break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            else:
                print("Invalid input. Please enter a number between 1 and " + str(len(laptops)) + ".")
        except ValueError:
            print("Invalid input. Please enter a number.")


Laptop_P = {}

def purchase(laptops, Laptop_Ps):
    while True:
        Step = input("Would you like to add a new laptop to the stock or buy an existing one? (A to add /B for existing): ")

        if Step.upper() == "A":
            try:
                L_Name = input("Please enter the name of the new laptop: ")
                L_brand= input("Please enter the brand of the new laptop: ")
                L_Price = float(input("Please enter the price of the new laptop: "))
                laptop_ram = int(input("Please enter the RAM of the new laptop (in GB): "))
                laptop_processor = input("Please enter the processor of the new laptop: ")
                laptop_gpu = input("Please enter the GPU of the new laptop: ")
                L_purchased = int(input("Please enter the number of available laptops: "))
                laptops[L_Name] = {
                    'brand': L_brand,
                    'price': L_Price,
                    'ram': laptop_ram,
                    'processor': laptop_processor,
                    'gpu': laptop_gpu,
                    'available_laptop': L_purchased
                }
                with open("laptops.txt", "w") as file:
                    for name, details in laptops.items():
                        file.write(f"{name}, {details['brand']}, ${details['price']}, {details['available_laptop']}, {details['ram']}, {details['processor']}, {details['gpu']}\n")
                file.close()
                Laptop_Ps[L_Name] = {'price': L_Price, 'quantity': L_purchased}
            except:
                print("Invalid input. Please try again.")

        elif Step.upper() == "B":
            try:
                print("Laptops in stock:")
                for i, name in enumerate(laptops.keys()):
                    print(f"{i+1}. {name}")

                Choice= int(input("Enter the S.N of the laptop you would like to order from distributor: "))
                L_Name = list(laptops.keys())[Choice- 1]
                laptop = laptops[L_Name]
                print(f"\nThe specifications of the {L_Name} are:")
                print("--------------------------------------------------------")
                print(f"Brand: {laptop['brand']}")
                print(f"Price: ${laptop['price']- 600} without VAT")
                print(f"RAM: {laptop['ram']} GB")
                print(f"Processor: {laptop['processor']}")
                print(f"GPU: {laptop['gpu']}")
                print(f"Availability: {laptop['available_laptop']}")

                L_purchased = int(input("How many you want to purchase: "))
                laptops[L_Name]['available_laptop'] += L_purchased
                Laptop_Ps[L_Name] = {'price': laptops[L_Name]['price'], 'quantity': L_purchased}
                with open("laptops.txt", "w") as file:
                    for name, details in laptops.items():
                        file.write(f"{name}, {details['brand']}, ${details['price']}, {details['available_laptop']}, {details['ram']}, {details['processor']}, {details['gpu']}\n")
                file.close()
                
                
                print("Purchased successfully!!")
                
                buy_more = input("Would you like to buy more laptops (Y/N)?: ")
                if buy_more.upper() == "Y":
                    continue
                elif buy_more.upper() == "N":
                    return
                else:
                    print("Invalid input. Please enter Y or N.")
                    return

            except ValueError:
                print("Invalid input. Please enter a number.")  


        else:
            print("Invalid input detected. Please choose an option from A and B")
            continue

    

           
