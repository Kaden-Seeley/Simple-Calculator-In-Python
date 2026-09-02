import time

dev_debugs = True


def main():
    loading(loading_time=2)

    first_num = user_input(prompt="FIRST_NUMBER")
    second_num = user_input(prompt="SECOND_NUMBER")
    operation = user_input(prompt="OPERATION")

    answer = calculate(first_num, second_num, operation)

    print(f"Answer: {answer}")


def loading(loading_time):
    print("Loading...")
    time.sleep(loading_time)
    print("Loaded.")


def user_input(prompt):
    if prompt == "FIRST_NUMBER":
        first_number = input("First Number: ")
        return validate_input(first_number)

    if prompt == "SECOND_NUMBER":
        second_number = input("Second Number: ")
        return validate_input(second_number)

    if prompt == "OPERATION":
        return input("Operation (*,/,+,-): ")


def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    if op == "-":
        return num1 - num2
    if op == "*":
        return num1 * num2
    if op == "/":
        return num1 / num2


def validate_input(users_input):
    try:
        number = float(users_input)

        if dev_debugs:
            print(f"Valid number found: {number}")

        return number

    except ValueError:
        print("Error: Input contains letters or is not a valid number.")


main()
