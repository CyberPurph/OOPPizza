#Classes
class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return f"^^USER^^ \nName - {self.name} \nEmail - {self.email} \nAddress - {self.address}"
    
#Input
user_name = input("Who's ordering? ")
user_email = input("What is your email? ")
user_address = input("Where do you live? ")

#Objects
user = User(user_name, user_email, user_address)

#Display
print(user)