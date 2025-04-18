import random

def number_guessing_game():
    secret_number = random.randint(0, 100)
    guesses = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            ask = int(input("Enter your guess: "))
            if ask > 100 or ask < 1:
                print("It's not valid. you have to choose between 0 to 100")
            elif ask > secret_number:
                print("It's to high!")
                guesses +=1
            elif ask < secret_number:
                print("It's to low!")
                guesses +=1
            else:
                print("you win!")
                print(f"Number of guess: {guesses}")
                break
        except ValueError:
            print("Add Valid number!")

        

if __name__ == "__main__":
    number_guessing_game()