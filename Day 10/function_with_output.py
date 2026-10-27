# Function with Output
def formate_name(f_name, l_name):
    f_name_title = f_name.title()
    l_name_title = l_name.title()
    return f_name_title + " " + l_name_title

name_title = formate_name("hello", "ABHI")
print(name_title)


def function_1(text):
    return text + text


def function_2(text):
    return text.title()

output = function_2(function_1("Shek"))
print(output)

