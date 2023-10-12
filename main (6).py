class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} - Price: {self.price}, Quantity: {self.quantity}"

def linear_search(products, attribute):
    for i in range(len(products)):
        if attribute == "name":
            key = products[i].name
        elif attribute == "price":
            key = products[i].price
        elif attribute == "quantity":
            key = products[i].quantity
        else:
            raise ValueError("Invalid attribute")
        
        j = i - 1
        while j >= 0 and key < products[j].name:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = products[i]

# Example usage
products = [
    Product("ProductB", 30, 5),
    Product("ProductA", 20, 3),
    Product("ProductC", 25, 7)
]

print("Products before sorting:")
print(products)

# Sort products by name using linear search
linear_search(products, "name")

print("\nProducts after sorting by name:")
print(products)
