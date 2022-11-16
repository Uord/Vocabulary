
# Vocabulary

Scrape Vocabulary.com sites for list of words. You can also check word definition and sentence examples.

Implemented in Python with BeautifulSoup library.




## Usage/Examples

```python
from Vocabulary import VocabularyList, Word

url = "https://www.vocabulary.com/lists/165401"

word_list = VocabularyList(url)

print(word_list.words)
# ['integrity', 'attain', 'incidentally', 'defray', 'campaign',\
#  'behalf', 'constituent', 'finance', 'critical', 'stenographer',\
#  'unbiased', 'expose', 'conscience', 'subterfuge', 'audit', 'pertinent',\
#  'statute', 'disbursement', 'reimburse', 'constitute', 'unprecedented',\ 
#  'circumstances', 'enterprise', 'commendation', 'economist', 'estate',\
#  'engagement', 'policy', 'bond', 'mortgage', 'modest', 'supplement',\
#  'condemn', 'casualty', 'corruption', 'red herring', 'bureau', 'prosperity',\
#  'crusade', 'abide by']

word = Word("hello")

print(f"Word: {word}")
#Word: hello

print(f"Short definition: {word.get_short_definition()}")
#Short definition: Hello! Hi! How are you doing?\
#Hello is a salutation or greeting commonly used to begin conversations or telephone calls.

print(f"Long definition: {word.get_long_definition()}")
#Long definition: Hello has been used as an English greeting since the 19th century.\
#Most agree that it is related to the older French exclamation “Holà” — which means essentially\
#“Ho there!” — like you might say to a horse to tell it to stop. Nowadays it’s still used to get\
#someone’s attention but instead of stopping you’re starting something — usually a chat.\
#Hallo and Hullo are variations of Hello used by British English speakers.

print(f"Examples: {word.get_examples()}")
#Examples: ['Every morning they exchanged polite hellos.']

```

