import requests
from bs4 import BeautifulSoup
import time


class VocabularyList:
    """Vocabulary list class."""

    def __init__(self, url: str) -> None:
        self.url = url
        self.words = []
        self.get_words()

    def __repr__(self) -> str:
        return f"VocabularyList({self.url})"

    def __str__(self) -> str:
        return str(self.words)

    @property
    def url(self) -> str:
        """Get the url of the word."""
        self._url

    @url.setter
    def url(self, u: str) -> str:
        if not u.startswith("https://www.vocabulary.com/lists/"):
            raise ValueError("Invalid url")
        try:
            requests.get(u)
        except requests.exceptions.ConnectionError:
            raise ValueError("Invalid url")
        self._url = u

    @url.getter
    def url(self) -> str:
        return self._url

    def get_words(self) -> None:
        """Get vocabulary list from a given url."""
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            words_list = soup.find(id="wordlist").find_all("a", class_="word")
            self.words = [word.text.strip() for word in words_list]
        except AttributeError:
            raise ValueError("Invalid url")


class Word:
    """A class to represent a word."""

    def __init__(self, word: str) -> None:
        self.word = word
        self._url = f"https://www.vocabulary.com/dictionary/{self.word}"
        self._soup = BeautifulSoup(requests.get(self.url).text, "html.parser")

    def __repr__(self) -> str:
        return f"Word({self.word})"

    def __str__(self) -> str:
        return f"{self.word}"

    @property
    def url(self) -> str:
        """Get the url of the word."""
        return self._url

    @property
    def soup(self) -> BeautifulSoup:
        """Get BeautifulSoup object."""
        return self._soup

    def get_short_definition(self) -> str:
        """Get short definition of a word."""
        return self.soup.find("p", class_="short").text

    def get_long_definition(self) -> str:
        """Get long definition of a word."""
        return self.soup.find("p", class_="long").text

    def get_examples(self) -> list:
        """Get example sentences containing the word."""
        examples = self.soup.find_all("div", class_="example")
        return [
            example.text.replace("\n", "")  # remove new line characters
            .replace("”", "")  # remove the quotation marks
            .replace("“", "")  # remove the quotation marks
            .capitalize()  # capitalize the first letter
            + "."  # add a period at the end of the sentence
            for example in examples
        ]
