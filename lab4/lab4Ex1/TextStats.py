import re


class TextStats:

    def __init__(self, text):
        self.number_of_lines = 0
        self.number_of_words = 0
        self.number_of_nonalpha = 0
        self.__compute(text)

    def __compute(self, text):
        self.number_of_lines = text.count('\n')
        self.number_of_words = len(re.findall(r"[\w']+", text))
        s = ''.join(ch for ch in text if ch.isalpha())
        self.number_of_nonalpha = len(text) - len(s) - 1

    def __str__(self):
        return str(self.number_of_lines) + " " + (str(self.number_of_words)) + " " + (str(self.number_of_nonalpha))
