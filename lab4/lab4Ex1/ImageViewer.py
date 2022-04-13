from PIL import Image
from FileViewer import FileViewer


class ImageViewer(FileViewer):

    def __init__(self, path):
        super().__init__(path)

    def view(self):
        if self.path.__contains__('.jpg') or self.path.__contains__('.png'):
            img = Image.open(self.path)
            img.show()

        else:
            print('It couldnt happen')
