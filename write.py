from read import laptops
from function import sell, purchase
import datetime



def write_to_file_sale():

# Define the L_solddictionary
    L_sold= {}
    
# Calling the function
    sell(laptops, L_sold)
    
    Full_name = input("Please enter the customer's name: ")

    while not Full_name.isalpha():
        Full_name = input("Please enter your valid name: ")
    
   # Inquire whether the consumer wants their shipment.

    Shipping = input("Want your product shipped 'y' for yes 'n' for no: ")

    #ask for the distance and calculate the shipping price, if neeeded

    if Shipping.lower() == "y":
        distance = float(input("Enter the distance in kms between the store and your location: "))
        if distance > 10:
            S_Price = 50
        elif distance > 1:
            S_Price = 10
        else:
            S_Price = 0
        print("Your shipping price is:", S_Price)
    else:
        #set the shipping price to 0, if not required

        S_Price = 0
        print("Shipping not required. Shipping price is:", S_Price)

        
    # Calculate the total price
    
    Total_Sum = sum([laptop_sold['price']*laptop_sold['quantity'] for laptop_sold in L_sold.values()])
    Discount = 0.1 * Total_Sum
    
    now = datetime.datetime.now()
    line = "-" * 65
    line = "**************************************************************"

    print(line)
    print("                        Silicon Technology            ")
    print("                            Kathmandu               ")
    print("                              Nepal              ")
    print(line)
    print(f"Customer Name: {Full_name:<15} Date: {datetime.date.today()}")
    print(f" Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
    print(line)
    print("Laptop Name       Quantity      Unit Price    Total Price")
    for laptop_name, laptop_sold in L_sold.items():
        print(f"{laptop_name:<18}{laptop_sold['quantity']:<13}${laptop_sold['price']:<14}${laptop_sold['quantity']*laptop_sold['price']:<12}")
    print(line)
    print(f"Net Amount: ${Total_Sum:<10}")
    print(f"Discount: ${Discount:<15}")
    print(f"Shipping Charge: {S_Price:<15}")
    print(f"VAT: {' ':<15}")
    print(line)
    print(f"Grand Total: ${Total_Sum - Discount + S_Price:<10}")
    print(line)
    print(f"{' ':<45}Hiritik")
    print(f"{' ':<45}Seller ")
    print('\n===========================================')
    print("Thank you for choosing PC HUB!")
    print('===========================================\n\n\n')


    Name = "sale_" + Full_name + now.strftime('%Y-%m-%d-%H-%M-%S') + ".txt"
    with open(Name, "w") as file:
        file.write("******************************************************************\n")
        file.write("                    Silicon Technology             \n")
        file.write("                        Kathmandu            \n")
        file.write("                          Nepal             \n")
        file.write("******************************************************************\n")
        file.write(f"Customer Name: {Full_name:<15} Time: {datetime.datetime.now().strftime('%H:%M:%S')}\n")
        file.write("                                                        \n")
        file.write(f" Date: {datetime.date.today()}\n")
        file.write("-----------------------------------------------------------------\n")
        file.write("Laptop Name       Quantity      Unit Price    Total Price\n")
        for laptop_name, laptop_sold in L_sold.items():
            file.write(f"{laptop_name:<18}{laptop_sold['quantity']:<13}${laptop_sold['price']:<14}${laptop_sold['quantity']*laptop_sold['price']:<12}\n")
        file.write("------------------------------------------------------------------\n")
        file.write(f"Net Amount: ${Total_Sum:<10}\n")
        file.write(f"Discount: ${Discount:<15}\n")
        file.write(f"Shipping Charge: {S_Price:<15}\n")
        file.write(f"VAT: {' ':<15}\n")
        file.write("--------------------------------------------------------------------\n")
        file.write(f"Grand Total: ${Total_Sum - Discount + S_Price:<10}\n")
        file.write("--------------------------------------------------------------------\n")
        file.write(f"{' ':<45}Hiritik \n")
        file.write(f"{' ':<45}Seller Signature\n\n\n")
        file.write(f"Congratulations! Your new laptop is almost ready to be delivered, \n and I'm pleased to inform you that the total price, including shipping and other fees is, ${Total_Sum - Discount + S_Price:<10}.\n  ")
        file.write('\n===========================================================\n')
        file.write("Thank you for choosing Us. We will like to serve you again!\n")
        file.write('=============================================================\n')


    file.close()



def write_to_file_purchase():
    Laptop_Ps = {}
    purchase(laptops, Laptop_Ps)
    
    discount_percentage = int(input("Enter the discount percentage: "))
    print("Note that there is a VAT of 13% on the total amount.")

    # Total price

    Total_Sum = sum([Laptop_Ps['price']*Laptop_Ps['quantity'] for Laptop_Ps in Laptop_Ps.values()])
    Discount = (discount_percentage/100) * Total_Sum
    Net_sum = Discount + Total_Sum
    VAT = 0.13 * Total_Sum


    Supplier_Name = input("Please enter the supplier's name: ")
    while not Supplier_Name.isalpha():
        Supplier_Name = input("Please enter a valid name: ")

    
    now = datetime.datetime.now()

    Name = "purchase_" + Supplier_Name + now.strftime('%Y-%m-%d-%H-%M-%S') + ".txt"
    with open(Name, "w") as file:
        print(" |-----------------------------------------------------------------\n")

        file.write(f"                       {Supplier_Name}                       \n")
        

        file.write(" -----------------------------------------------------------------\n")
        file.write(f"Name: PC HUB!          Date: {datetime.date.today()}\n")
        file.write(f"Contact: 982437****              Time: {datetime.datetime.now().strftime('%H:%M:%S')}|\n")
        file.write(" -----------------------------------------------------------------\n")
        file.write("Laptop Name       Quantity      Unit Price    Total Price          \n")
        for laptop_name, Laptop_Ps in Laptop_Ps.items():
            file.write(f"{laptop_name:<18}{Laptop_Ps['quantity']:<13}${Laptop_Ps['price']:<14}${Laptop_Ps['quantity']*Laptop_Ps['price']:<12}\n")

        file.write(" ------------------------------------------------------------------\n")
        file.write(f"Discount: ${Discount:<10}                                   \n")
        file.write(f"Net Amount (after discount): ${Net_sum :<10}                    \n")
        file.write(f"VAT: ${VAT:<20}                                             \n")
        file.write(" --------------------------------------------------------------------\n")
        file.write(f"Total Amount (including VAT): ${Total_Sum:<10}                  \n")
        file.write(" --------------------------------------------------------------------\n")
        file.write(f"{' ':<45}{Supplier_Name.split()[0]}                             \n")
        file.write(f"{' ':<45}Supplier                                    \n")
        file.write(f"Thank you. Please visit again!!")
        
    file.close()
    
    print("Bill Generated Successfully.")