#The calculator app
#Task 1

def add (a, b):
    return a + b 

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b != 0:
        return a / b 
    else:
        return "Error: Division by zero"
    
#Task 2
operation = input("Enter the operation (+, -, *, /:)")

try:
    num1 = (input("Enter the first number:"))
    num2 = (input)("Enter the second number:)")
except ValueError:
    print("Invalid input. Please enter numeric values.")
if operation =="+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation =="*":
    result = multiply(num1, num2)

elif operation =="/":
    result = divide(num1, num2)

    print(f"The result of {num1} {operation} {num2} is: {result}" )
    

    #Task 3

    # Value error included in task 2

#2 The shopping list maker

#Task 1
shopping_list = []
def display_list():
    print(shopping_list)
def add_to_shopping_list(): 
    item = input("Enter an item to add to the shopping_list(or type 'done' to finish):")
    if item.lower() == 'done':
        display_list()
    else:
        shopping_list.append(item)
        print(f" '{item}' has been added to the shopping list.")

def main():
    choice = input("Press a to add an item, press d to display")
    if choice == 'a':
        add_to_shopping_list()
    elif choice == 'd':
        display_list()
    else:
        print("Invalid input")
main()
