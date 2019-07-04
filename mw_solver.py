import mysteryword as mw


def words_of_the_right_length(word_list, blankstring):
    length_of_word = len(blankstring)
    reduced_list = word_length_selector(length_of_word, length_of_word)
    return reduced_list


def words_with_right_letters(word_list, blankstring):
    reduced_list = [word for word in word_list if word_matches(blankstring)]
    return reduced_list


def word_matches(given_word, blankstring):
    word_comparison = zip(given_word, blankstring)
    for letter in word_comparison:
        if letter[1] == "_" or letter[0] == letter[1]:
            continue
        else:
            return False
    return True
