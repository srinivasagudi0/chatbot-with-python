def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print("Please, remind me your name.")
    name = input("> ")
    print(f"What a great name you have, {name}!")


def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    while True:
        try:
            rem3 = int(input("Remainder when divided by 3: "))
            rem5 = int(input("Remainder when divided by 5: "))
            rem7 = int(input("Remainder when divided by 7: "))
            break
        except ValueError:
            print("Please enter valid integers.")

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    print("Now I will prove to you that I can count to any number you want.")
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    for curr in range(num + 1):
        print(f"{curr}!")


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print('''1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.''')

    while True:
        try:
            answer = int(input("Enter your answer as an integer: "))
            if answer == 2:
                print("You have reached your answer.")
                print("Completed, have a nice day!")
                break
            else:
                print("Let's try again.")
        except ValueError:
            print("Please enter a valid integer.")


def end():
    print("Congratulations, have a nice day!")
    input("Press Enter to exit...")


# Main program
if __name__ == "__main__":
    greet("Aid", "2025")
    remind_name()
    guess_age()
    count()
    test()
    end()
