#Classes
class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return f"^^USER^^ \nName - {self.name} \nEmail - {self.email} \nAddress - {self.address}"
    
class Pizza:
    def __init__(self, size, price, num):
        self.size = size
        self.price = price
        self.num = num

    def total(self):
        if self.num >= 3:
            total = self.num * self.price * 0.85

    def __str__(self):
        return f"^^PIIZAS^^ \nSize - {self.size} \nPrice - {self.price} \nQuantity {self.num}"
    
#Input
user_name = input("Who's ordering? ")
user_email = input("What is your email? ")
user_address = input("Where do you live? ")

pizza_size = input("Which size of pizza would you like? [Small, Medium, Large, X-Large] ")
pizza_price = {
    "Small": 10,
    "Medium": 12,
    "Large": 15,
    "X-Large": 18
}
if pizza_size not in pizza_price:
    print("Please enter pizza size as shown. Try again.")

pizza_num = input("Enter the amount of pizzas you want ")

#Objects
user = User(user_name, user_email, user_address)
pizza = Pizza(pizza_size, pizza_price[pizza_size], pizza_num)

#Display
print(user)
print(pizza)