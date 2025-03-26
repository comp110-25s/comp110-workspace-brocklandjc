"""A fun worlde exercise to practice writing code."""

__author__: str = "730470079"


def contains_char(search_string: str, target_char: str) -> bool:
    """checks to see if the target character is present in the users guess."""
    assert len(target_char) == 1, f"len('{target_char}') is not 1"
    for char in search_string:
        if char == target_char:
            return True
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Checks the accuracy of the guess compared to the secret word."""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    emoji_result = ""

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX

    return emoji_result


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess of the correct length and ensures it is valid."""
    guess = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    MAX_TURNS = 6
    turn = 1
    has_won = False

    while turn <= MAX_TURNS and not has_won:
        print(f"=== Turn {turn}/{MAX_TURNS} ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)

        if guess == secret:
            has_won = True
        else:
            turn += 1

    if has_won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
