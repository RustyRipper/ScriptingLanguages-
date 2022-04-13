from FileViewer import FileViewer
from TextBuffer import TextBuffer
from TextStats import TextStats
import subprocess as sp


class TextViewer(FileViewer, TextBuffer):
    _stats: TextStats

    def __init__(self, path):

        FileViewer.__init__(self, path)
        TextBuffer.__init__(self, path)
        self._stats = TextStats(self.text)

    def view(self):
        program_name = "notepad.exe"
        sp.Popen([program_name, self.path])

    def get_data(self):
        return self._stats





