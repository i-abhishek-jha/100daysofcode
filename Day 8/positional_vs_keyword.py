# Positional vs Keyword Arguments

# Multiple Inputs
def greet_with(name, loc):
    print(f"Hello {name}!")
    print(f"What is it like in {loc}?")

# Positional Arguments
greet_with("Abhi","Chennai")

# Keyword Arguments
greet_with( loc= "Bangalore", name = "Ritik")