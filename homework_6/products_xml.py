import xml.etree.ElementTree as ET


# Function to read XML and print product names and quantities
def read_xml(file):
    try:
        tree = ET.parse(file)
        root = tree.getroot()

        for product in root.findall('product'):
            name = product.find('name').text
            quantity = product.find('quantity').text
            price = product.find('price').text
            print(f"Product: {name}, Quantity: {quantity}, Price: {price}")
    except FileNotFoundError:
        print("File not found.")
        return


# Function to modify product quantity and save the changes
def modify_quantity(file, product_name, new_quantity, new_price):
    try:
        tree = ET.parse(file)
        root = tree.getroot()

        for product in root.findall('product'):
            name = product.find('name').text
            if name == product_name:
                product.find('quantity').text = str(new_quantity)
                product.find("price").text = str(new_price)
                break

        # Save the updated XML back to the file
        tree.write(file)
    except FileNotFoundError:
        print("File not found.")
        return


# Reading the XML file and displaying products and their quantities
print("Initial Product List:")
read_xml('products.xml')

# Modifying the quantity of a specific product
try:
    product_name = input("Enter product to update: ")
    product_qty = int(input("Enter new quantity: "))
    product_price = int(input("Enter new price: "))
    modify_quantity('products.xml', product_name, product_qty, product_price)
except ValueError as e:
    print(f"please enter valid data {e}")
except Exception as e:
    print(f"An error occurred: {e}")


