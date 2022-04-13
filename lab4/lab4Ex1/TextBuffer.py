from pathlib import Path


class TextBuffer:
    text = ''

    def __init__(self, path):
        self.__read_from_file(path)

    def __read_from_file(self, path):
        try:
            self.text = Path(path).read_text()
        except FileNotFoundError:
            print('bad file')
