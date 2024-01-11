from randomSentences import sentences


def replace_word():

    word_to_replace = input("Enter the word you want to replace: ")
    word_replacement = input("Enter the word replacement: ")
    return sentences.replace(word_to_replace, word_replacement)


print(replace_word())