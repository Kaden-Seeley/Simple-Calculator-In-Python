import time
import math

dev_debugs = True

def main():
    loading(loading_time=2)
    user_input(prompt="FIRST_NUMBER")
 
def loading(loading_time):
    print("test terminal loading...")
    time.sleep(loading_time)
    print("loaded.")

def user_input(prompt):
    if prompt == "FIRST_NUMBER":
        first_number = input("First Number: ")
        validate_input(users_input=first_number)

    if prompt == "SECOND_NUMBER":
        pass

    if prompt == "EQUATION":
        pass

def calculate():
    pass

def validate_input(users_input):
    try:
        number = float(users_input)
        if dev_debugs == True:
            print(f"Valid number found: {number}")
        return number
    except ValueError:
        print("Error: Input contains letters or is not a valid number.")

main()