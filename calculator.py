print("Welcome to the Calculator!")
def print_menu():
    print("Calculator menu: ")
    print("1 = addition")
    print("2 = subtraction")
    print("3 = multiplication")
    print("4 = division")
    print("5 = exponent")
    print("6 = modulo")

def complete_calculator():
    addition = lambda num1, num2: num1 + num2
    subtraction = lambda num1, num2: num1 - num2
    multiplication = lambda num1, num2: num1 * num2
    division = lambda num1, num2: num1 / num2
    exponent = lambda num1, num2: num1 ** num2
    modulo = lambda num1, num2: num1 % num2
    print_menu()
    choice = get_choice()
    if choice == '1':
        num1, num2 = user_input()
        sum = addition(num1, num2)
        print("Result of addition is", sum)
    elif choice == '2':
        num1, num2 = user_input()
        total = subtraction(num1, num2)
        print("Result of subtraction is", total)
    elif choice == '3':
        num1, num2 = user_input()
        total = multiplication(num1, num2)
        print("Result of multiplication is", total)
    elif choice == '4':
        num1, num2 = user_input()
        total = division(num1, num2)
        print("Result of division is", total)
    elif choice == '5':
        num1, num2 = user_input()
        total = exponent(num1, num2)
        print("Result of exponent function", total)
    elif choice == '6':
        num1, num2 = user_input()
        total = modulo(num1, num2)
        print("Result of modulo function:", total)
    else:
        print("Invalid input! Please try again")

def user_choice_y_n():
    choice = input("Do you want to use the calculator again? Please press y for yes or n for no: ")
    return choice

def get_choice():
    choice = input("Please enter a number from the menu: ")
    return choice

def user_input():
    num1 = input("Please enter the first number: ")
    num2 = input("Please enter the second number: ")
    num1 = float(num1)
    num2 = float(num2)
    return num1, num2

if __name__ == "__main__":
    while True:
        choice_y_n = user_choice_y_n()
        if choice_y_n == 'n':
            print("Exiting calculator")
            exit()
        elif choice_y_n == 'y':
            complete_calculator()
        else:
            print("Invalid input!")