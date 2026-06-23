def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    while True:
        n1 = float(input("Enter the first number: "))

        while True:
            for sign in operations:
                print(sign)

            operation_symbol = input("Pick an operation: ")
            n2 = float(input("Enter the next number: "))

            answer = operations[operation_symbol](n1, n2)

            print(f"{n1} {operation_symbol} {n2} = {answer}")

            ask_again = input(
                f"Type 'y' to continue with {answer}, 'n' for a new calculation, or 'q' to quit: "
            )

            if ask_again == "y":
                n1 = answer
            elif ask_again == "n":
                break
            elif ask_again == "q":
                return

calculator()
