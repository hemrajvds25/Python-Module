import random

LOW, HIGH = 1, 100
MAX_ATTEMPTS = 7


def play_round():
    secret = random.randint(LOW, HIGH)
    attempts = 0
    print(f"\nI'm thinking of a number between {LOW} and {HIGH}.")
    print(f"You have {MAX_ATTEMPTS} attempts.\n")

    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{MAX_ATTEMPTS} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1

        if guess == secret:
            score = (MAX_ATTEMPTS - attempts + 1) * 10
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            print(f"Round score: {score}")
            return score
        elif guess > secret:
            print("Too High!")
        else:
            print("Too Low!")

    print(f"Out of attempts! The number was {secret}.")
    print("Round score: 0")
    return 0


def main():
    total_score = 0
    best_score = 0
    rounds_played = 0

    print("=== NUMBER GUESSING GAME ===")

    while True:
        round_score = play_round()
        rounds_played += 1
        total_score += round_score
        best_score = max(best_score, round_score)

        print(f"Total score so far: {total_score}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        while again not in ("y", "n"):
            again = input("Please type y or n: ").strip().lower()
        if again == "n":
            break

    print("\n=== FINAL RESULT ===")
    print(f"Rounds played : {rounds_played}")
    print(f"Total score : {total_score}")
    print(f"Best round : {best_score}")
    print(f"Average score : {total_score / rounds_played:.1f}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
