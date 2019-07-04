import random


def word_getter(remove_proper_nouns=True):
    the_word = ""
    word_list = get_list_of_all_possible_words()
    if remove_proper_nouns:
        word_list = [word for word in word_list if not word[0].isupper()]
    the_word = random.choice(word_list)
    return the_word


def get_list_of_all_possible_words():
    the_word_list = []

    with open("/usr/share/dict/words") as word_file:
        the_word_string = word_file.read()

    the_word_list = the_word_string.split()
    return the_word_list


def word_display(guessed_string, secret_word):
    display_string = ""
    for letter in secret_word:
        if letter in guessed_string:
            display_string += letter.upper()
        else:
            display_string += "_"
    print(display_string)
    return display_string


def user_input_is_correct(input_str):
    if len(input_str) > 1:
        return False
    elif len(input_str) == 0:
        return False
    elif not input_str.isalpha():
        return False
    else:
        return True


def guess_is_new(guessed_string, user_input):
    if user_input in guessed_string:
        return False
    else:
        return True


def guess_appender(guessed_string, user_input):
    guess_string = guessed_string + user_input
    return guess_string


def not_incorrect_or_repeat_guess(guessed_string, user_input):
    if not guess_is_new(guessed_string, user_input):
        print("You already guessed that!")
        return False
    elif not user_input_is_correct(user_input):
        print("Nope, give me a single letter")
        return False
    else:
        return True


def is_correct_guess(secret_word, current_guess):
    if current_guess in secret_word:
        print("You got one!")
        return "You got one!"
    else:
        pass


def guess_display(guessed_string, secret_word, max_guesses):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    guesses_list = []
    guesses_string = ""
    for letter in alphabet:
        if letter not in guessed_string:
            guesses_list.append(letter.upper())
        else:
            pass
    guesses_string = "".join(sorted(guesses_list))
    guesses_remain = max_guesses - spent_guesses(guessed_string, secret_word)
    print_string = "Letters remaining: {} Guesses remaining: {}."
    print(print_string.format(guesses_string, guesses_remain))
    return print_string.format(guesses_string, guesses_remain)


def you_win(guessed_string, secret_word):
    for letter in secret_word:
        if letter not in guessed_string:
            return False
    return True


def you_lose(guessed_string, secret_word, max_guesses):
    if spent_guesses(guessed_string, secret_word) >= max_guesses:
        return True
    else:
        return False


def spent_guesses(guessed_string, secret_word):
    """Given the word and the string of guesses, return how many guesses
    have been spent."""
    right_guesses = 0
    for letter in guessed_string:
        if letter in secret_word:
            right_guesses += 1
    total_guesses = len(guessed_string)
    spent_guesses = total_guesses - right_guesses
    return spent_guesses


def check_win_lose(guessed_string, secret_word, max_guesses):
    if you_win(guessed_string, secret_word):
        print("You win!")
        print("Your word was: {}".format(secret_word.upper()))
        return "You win!"

    elif you_lose(guessed_string, secret_word, max_guesses):
        print("You lose!")
        print("Your word was: {}".format(secret_word.upper()))
        return "You lose!"
    else:
        pass


def word_length_selector(*args):
    all_words = get_list_of_all_possible_words()
    some_words = [word for word in all_words if not word[0].isupper()]
    if len(args) == 1:
        some_words = [word for word in some_words if len(word) > args[0]]
    else:
        some_words = [
            word for word in some_words if len(word) > args[0] and len(word) < args[1]
        ]
    the_word = random.choice(some_words)
    return the_word


if __name__ == "__main__":
    print("Welcome to Mystery Word!")
    print(
        "Select a difficulty: [E]asy (4-6 letters), [M]edium (6-10 "
        + "letters), or [H]ard (10+ letters)"
    )
    difficulty_selection = input("E/M/H >")
    secret_word = ""
    if difficulty_selection.upper() == "E":
        secret_word = word_length_selector(4, 6)
    elif difficulty_selection.upper() == "M":
        secret_word = word_length_selector(6, 10)
    elif difficulty_selection.upper() == "H":
        secret_word = word_length_selector(10)
    else:
        secret_word = word_getter()
    print("Your word is {} letters long!".format(len(secret_word)))
    max_guesses = 8  # set to 8, but use 26 to test
    guessed_string = ""
    while True:
        word_display(guessed_string, secret_word)
        guess_display(guessed_string, secret_word, max_guesses)
        curr_guess = input("Guess a letter: ")
        curr_guess = curr_guess.lower()
        if not_incorrect_or_repeat_guess(guessed_string, curr_guess):
            guessed_string = guess_appender(guessed_string, curr_guess)
            print(guessed_string)
            is_correct_guess(secret_word, curr_guess)
        win_state = check_win_lose(guessed_string, secret_word, max_guesses)
        if win_state is not None:
            break
