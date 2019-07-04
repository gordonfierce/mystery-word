from mysteryword import word_getter
from mysteryword import get_list_of_all_possible_words

word_list = []

for count in range(1, 20):
    word_list.append(word_getter(remove_proper_nouns=True))

word_string = " ".join(word_list)

print(word_string)
