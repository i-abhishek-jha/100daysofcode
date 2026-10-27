# Calculator using function, dict and recursion
import art

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

calculator_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


def calculator():
    print(art.logo)
    f_num = float(input("Your first number: "))
    recalculate = True
    
    while recalculate:
        for symbol in calculator_dict:
            print(symbol)
            
        operator = str(input("Choose the mathematical operator: "))
        s_num = float(input("Your second number: "))

        result = calculator_dict[operator](f_num, s_num)
        print(f"{f_num} {operator} {s_num} = {result}")

        calculation_continue = str(input(f"If you want to continue working with the previous result {result} then press \"y\" for yes or \"n\" for no")).lower()

        if calculation_continue == "y":
            f_num = result

        else:
            recalculate = False
            print("\n" * 20)
            calculator()
            
            
calculator()
