class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def display_info(self):
        print(f"{self.name} - ${self.price} (Stock: {self.stock_quantity})")


class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_to_cart(self, product, quantity):
        if product.product_id in self.cart:
            self.cart[product.product_id] += quantity
        else:
            self.cart[product.product_id] = quantity

    def remove_from_cart(self, product, quantity):
        if product.product_id in self.cart:
            self.cart[product.product_id] = max(0, self.cart[product.product_id] - quantity)

    def display_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your Shopping Cart:")
            for product_id, quantity in self.cart.items():
                product = products[product_id]
                print(f"{product.name} - Quantity: {quantity}")

    def calculate_total(self):
        total = 0
        for product_id, quantity in self.cart.items():
            product = products[product_id]
            total += product.price * quantity
        return total


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.shopping_cart = ShoppingCart()
        self.order_history = []

    def login(self, entered_password):
        return entered_password == self.password

    def view_order_history(self):
        if not self.order_history:
            print("No order history available.")
        else:
            print("Order History:")
            for order in self.order_history:
                print(order)

    def place_order(self):
        total = self.shopping_cart.calculate_total()
        if total == 0:
            print("Cannot place an empty order.")
            return

        order_summary = f"Order Total: ${total}\nItems:"
        for product_id, quantity in self.shopping_cart.cart.items():
            product = products[product_id]
            order_summary += f"\n- {product.name} x {quantity}"

        self.order_history.append(order_summary)
        print("Order placed successfully!")
        self.shopping_cart = ShoppingCart()


# Sample Products
products = {
    1: Product(1, "Laptop", 1000, 10),
    2: Product(2, "Smartphone", 500, 20),
    3: Product(3, "Headphones", 50, 30),
}

# Sample Users
users = {
    "user1": User("user1", "password1"),
    "user2": User("user2", "password2"),
}

# Sample Usage
current_user = None

while True:
    print("\n1. Login")
    print("2. Browse Products")
    print("3. View Cart")
    print("4. Place Order")
    print("5. View Order History")
    print("6. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username].login(password):
            current_user = users[username]
            print(f"Welcome, {current_user.username}!")
        else:
            print("Invalid username or password.")

    elif choice == "2":
        if current_user:
            print("\nAvailable Products:")
            for product_id, product in products.items():
                product.display_info()

            product_id = int(input("Enter the product ID to add to cart: "))
            quantity = int(input("Enter the quantity: "))
            if product_id in products and quantity > 0:
                current_user.shopping_cart.add_to_cart(products[product_id], quantity)
                print("Product added to cart.")
            else:
                print("Invalid product or quantity.")

    elif choice == "3":
        if current_user:
            current_user.shopping_cart.display_cart()
        else:
            print("Please login first.")

    elif choice == "4":
        if current_user:
            current_user.place_order()
        else:
            print("Please login first.")

    elif choice == "5":
        if current_user:
            current_user.view_order_history()
        else:
            print("Please login first.")

    elif choice == "6":
        break

    else:
        print("Invalid choice. Try again.")
