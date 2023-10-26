from art import logo


# Adding function
def add(n1, n2):
    return n1 + n2


# Substraction function
def substract(n1, n2):
    return n1 - n2


# Multiplication function
def multiply(n1, n2):
    return n1 * n2


# Divide function
def divde(n1,n2):
  if n2==0:
    print("Invalid entry: Division by Zero")
    return n1
  else: return n1/n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divde}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    operation_symbols = input("Pick up operation symbol from the list above:\n")
    num2 = float(input("What's the second number?: "))

    function = operations[operation_symbols]
    anwser = function(num1, num2)

    print(f"{num1} {operation_symbols} {num2} = {anwser} ")

    continue_calc = input("Would you like to continue with more calculations? (y/n): ")

    num_loop = 0
    anwser_lopp = anwser
    while continue_calc == "y":
        if continue_calc == "n":
            break
        anwser_lopp = function(anwser_lopp, num_loop)
        operation_symbols = input("Pick up operation symbol:\n")
        num_loop = float(input("What's the next number?: "))
        function = operations[operation_symbols]
        anwser2 = function(anwser_lopp, num_loop)

        print(f"{anwser_lopp} {operation_symbols} {num_loop} = {anwser2} ")
        continue_calc = input(
            "Do you want to continue with the calculations? (y/n). If you want to start over, use 'r': ")
        if continue_calc == "r":
            calculator()


calculator()
print("I appreciate your use of the calculator. Thank you")