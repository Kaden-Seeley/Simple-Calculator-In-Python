import time

dev_debugs = True

def main():
    loading(loading_time=2)
    first_num = user_input(prompt="FIRST_NUMBER")
    second_num = user_input(prompt="SECOND_NUMBER")
    operation = user_input(prompt="OPERATION")
    calculate(first_num, second_num, operation)
    
def loading(loading_time):
    print("test terminal loading...")
    time.sleep(loading_time)
    print("loaded.")

def user_input(prompt):
    if prompt == "FIRST_NUMBER":
        first_number = input("First Number: ")
        validate_input(users_input=first_number)

    if prompt == "SECOND_NUMBER":
        second_number = input("Second Number: ")
        validate_input(users_input=second_number)

    if prompt == "OPERATION":
        operation = input("Operation (*,/,+,-): ")

def calculate(num1,num2,op):
    if op == "+":
        ans = num1 + num2
        print(ans)
    if op == "-":
        pass
    if op == "*":
        pass
    if op == "/":
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