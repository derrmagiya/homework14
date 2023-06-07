#Question 2 

#Turn the shopping cart program from last week into an object-oriented program
#The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.

# Create a class called cart that retains items and has methods to add, remove, and show​
class Cart:
    def __init__(self):
        self.items = []

    def show_list(self):
        if len(self.items) == 0:
            print("Your shopping cart is empty.")
        else:
            print("Your shopping cart:")
            for item in self.items:
                print("- " + item)

    def add_item(self):
        item = input("Enter the item you want to add: ")
        self.items.append(item)
        print(item + " has been added to your shopping cart.")

    def delete_item(self):
        item = input("Enter the item you want to delete: ")
        if item in self.items:
            self.items.remove(item)
            print(item + " has been removed from your shopping cart.")
        else:
            print(item + " is not in your shopping cart.")

    def shopping_program(self):
        while True:
            print("\nOptions:")
            print("1. Show cart")
            print("2. Add item")
            print("3. Delete item")
            print("4. Quit")

            choice = input("What would you like to do? ")
            if choice == "1":
                self.show_list()
            elif choice == "2":
                self.add_item()
            elif choice == "3":
                self.delete_item()
            elif choice == "4":
                print("Your final shopping cart:")
                self.show_list()
                break
            else:
                print("Invalid choice. Please try again.")
Cart = Cart()
Cart.shopping_program()

# Question 2

# Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case¶

class StringProcessor:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print("String in uppercase: ", self.string.upper())


processor = StringProcessor()

processor.get_String()

processor.print_String()


