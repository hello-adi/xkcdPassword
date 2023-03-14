# open word.txt and add words to a list
def get_word_list(empty_list):
    with open("word.txt", "r") as f:
        empty_list = f.readlines()
        empty_list = [line.rstrip() for line in empty_list]
    return empty_list


english_words = []


def password(word_list):
    from random import randrange

    four_words = ""
    four_words_nospace = ""

    for i in range(4):
        random_word = word_list[randrange(0, len(word_list))]
        # search string
        four_words = four_words + random_word.capitalize() + " "

        # password ()
        four_words_nospace = four_words_nospace + random_word.capitalize()

    # print(four_words)
    # print(four_words_nospace)

    # return array with four_words, four_words_no_space
    return four_words, four_words_nospace


# # print(password())
# password()


# generates four word password and returns list containing the generated
# password and the search query
def generate_password():
    english_words = get_word_list(english_words)
    four_word_pass = list(password(english_words))
    return four_word_pass
