# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# define function with multiple input
def greet_name_location(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# positional argument
greet_name_location("Nikhil", "Dhaka")

# keyboard argument
greet_name_location(location="Chittagong", name="Raihan")
