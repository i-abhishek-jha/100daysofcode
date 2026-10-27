# Multiple Return Values in Function
def format_name(f_name, l_name):
    """take first name, last name and return them into Title formate """
    if f_name == "" or l_name == "":
        return "Invalid Input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What's your first name"), input("What's your last name")))
