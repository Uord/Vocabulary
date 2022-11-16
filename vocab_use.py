from Vocabulary import VocabularyList, Word


url = "https://www.vocabulary.com/lists/165401"

word_list = VocabularyList(url)
print(word_list.words)

word = Word(word_list.words[0])

print(f"Word: {word}")
print(f"Short definition: {word.get_short_definition()}")
print(f"Long definition: {word.get_long_definition()}")
print(f"Examples: {word.get_examples()}")
