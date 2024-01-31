def read_laptop_file():
    laptops = {}

    # open the laptops.txt file in read mode 

    with open('laptops.txt') as file:
        for line in file:
            # split the line into individual values and assign the values 

            Name, Brand, Price, available_laptop, ram, processor, gpu= line.strip().split(', ')
            
            # create a dictionary to store the laptop information 
            laptops[Name] = {'brand': Brand, 'price': float(Price.strip('$')), 'ram': ram, 'processor': processor, 'gpu': gpu, 'available_laptop': int(available_laptop)}

    
    file.close()

    return laptops


def print_laptops(laptops):
    print("%-20s %-15s %-15s %-10s %-20s %-15s %-10s" % ("Laptop Name", "Brand", "Price", "Available", "Ram", "Processor", "Graphics",))
    print("-" * 105)
    for Name, details in laptops.items():
        Brand = details["brand"]
        Price = details["price"]
        available = details["available_laptop"]
        ram = details["ram"]
        processor = details["processor"]
        graphics = details["gpu"]
        print("%-20s %-15s %-15s %-10s %-20s %-15s %-10s" % (Name, Brand, Price, available, ram, processor, graphics))


# calling the read_laptop_file function to read the laptop information from the text file

laptops = read_laptop_file()


