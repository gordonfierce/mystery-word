import mysteryword as mw

def test_word_getter_got_something():
    word = mw.word_getter()
    assert word is not None

def test_word_getter_got_string():
    word = mw.word_getter()
    assert type(word) == str

def test_get_list_got_list():
    a_list = mw.get_list_of_all_possible_words()
    assert type(a_list) == list

def test_strings_are_in_list():
    a_word = mw.get_list_of_all_possible_words()[0]
    assert type(a_word) == str

def test_some_words_are_in_all_words():
    a_list = mw.get_list_of_all_possible_words()
    some_words = ["waterfall", "rain", "aardvark"]
    for word in some_words:
        assert word in a_list

def test_user_input_is_alpha():
    user_input = mw.user_input_is_correct("#")
    assert not user_input
    user_input = mw.user_input_is_correct("t")
    assert user_input

def test_user_input_is_no_longer_than_one():
    user_input = mw.user_input_is_correct("o")
    assert user_input
    user_input = mw.user_input_is_correct("nots")
    assert not user_input

def test_user_input_isnt_empty():
    user_input = mw.user_input_is_correct("")
    assert not user_input

def test_word_display():
    display_string = mw.word_display("bcmdq","bombard")
    assert display_string == "B_MB__D"
    display_string = mw.word_display("lew","waterfall")
    assert display_string == "W__E___LL"

def test_guess_display():
    displaystring = mw.guess_display("bomar", "bombard", 8)
    assert displaystring == "Letters remaining: CDEFGHIJKLNPQSTUVWXYZ Guesses remaining: 8."
    displaystring = mw.guess_display("b", "bombard", 8)
    assert displaystring == "Letters remaining: ACDEFGHIJKLMNOPQRSTUVWXYZ Guesses remaining: 8."
    displaystring = mw.guess_display("bomarq", "bombard", 8)
    assert displaystring == "Letters remaining: CDEFGHIJKLNPSTUVWXYZ Guesses remaining: 7."

def test_guess_is_new():
    assert not mw.guess_is_new("axo", "a")
    assert mw.guess_is_new("axot", "q")

def test_guess_appender():
    new_guess_string = mw.guess_appender("ax", "o")
    assert new_guess_string == ("axo")

def test_not_incorrect_or_repeat_guess():
    result = mw.not_incorrect_or_repeat_guess("bomar", "b")
    assert not result
    result = mw.not_incorrect_or_repeat_guess("bomar", "!")
    assert not result

def test_you_win():
    assert mw.you_win("bomard","bombard")
    assert not mw.you_win("bomar", "bombard")

def test_you_lose():
    assert mw.you_lose("qbcef", "toward", 5)
    assert not mw.you_lose("abcef", "toward", 5)

def test_spent_guesses():
    spent_num = mw.spent_guesses("bcmdq","bombard")
    assert spent_num == 2

def test_check_win_lose():
    game_eval = mw.check_win_lose("qbcef", "toward", 5)
    assert game_eval == "You lose!"
    game_eval = mw.check_win_lose("bomard","bombard", 5)
    assert game_eval == "You win!"
    game_eval = mw.check_win_lose("abcef", "toward", 5)
    assert game_eval == None

def test_is_correct_guess():
    guess_eval = mw.is_correct_guess("bombard","a")
    assert guess_eval == "You got one!"
