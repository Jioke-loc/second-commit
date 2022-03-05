# while loop
i = 1
while i <= 9:
    print('*' * i)
    i = i + 1
print("Done")

# This is a guessing game, the variable secret_number is  the hidden number we want users to guess correctly
# guess_count is 0 as no guesses have been made but will be incremented by 1 until it gets to the guess limit number
# Guess_limit is the number of times a user has to make a guess before a verdict for winning or losing is declared.
secret_number = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('Winner!')
        break
else:
    print('Loser Loser!')

# car simulation game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Optimus Prime is already started")
        else:
            started = True
            print("welcome, Optimus Prime has started")
    elif command == "stop":
        if not started:
            print("Optimus Prime has already stopped")
        else:
            started = False
            print("Optimus Prime has stopped")
    elif command == "help":
        print("""
Enter Start to Start Car
Enter Stop to Stop Car
Enter Quit to Quit Program
""")
    elif command == "quit":
        print("Optimus Prime Thanks you, bye")
        break
    else:
        print("I do not understand, sorry")



