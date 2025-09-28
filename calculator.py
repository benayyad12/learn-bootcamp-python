# define operations functions 

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    n1 / n2


logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# create new empty dictionnary:

operations = {}

# add symbols in keys and functions:

operations["+"] = add

operations["-"] = subtract

operations["*"] = multiply

operations["/"] = divide


print(logo)


def calculator():

    should_continue = True
    num_1 = float(input("What's the first number ? "))


    while should_continue:

        print(logo)

        # pick operation:
        for symbol in operations:
            print(symbol) 

        operation = input("Pick an operation: ")

        num_2 = float(input("What's the second number ? "))

        result = operations[operation](num_1, num_2)

        print(f"{num_1} {operation} {num_2} = {result}")

        continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : ")

        if continue_calculating == 'y':

            num_1 = result

        else:
            should_continue = False
            print("\n" * 20)
            calculator()



calculator()
            
