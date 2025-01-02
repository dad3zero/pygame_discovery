import random
import string

print("Robot Missile")

print("Type the correct code (letter (A-Z) to defuse the missile, you have 4 chances")

code_to_guess = random.choice(string.ascii_uppercase)

for _ in range(4):
    guess = input("Your guess: ").upper()

    if guess == code_to_guess:
        print("Correct!")
        break
    else:
        print(f'{'later' if guess < code_to_guess else 'earlier'} than {guess}')

else:
    print("Booom")
    print(f"The correct answer was {code_to_guess}")