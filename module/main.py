
#Create a simple module my_module.py with a function that returns a greeting, and import it in another script.
import my_module

name = input("Enter your name: ")
message = my_module.get_greeting(name)
print(message)