import mimetypes as mt

from FileViewer import FileViewer
from ImageViewer import ImageViewer
from TextViewer import TextViewer


class ViewerCreator:
    def __init__(self):
        pass

    def create_viewer(self, path):
        try:
            instance: FileViewer = self.__detect_viewer_type(path)(path)
            return instance
        except TypeError or AttributeError:
            print('cant cast')
            print(path)
            print('-------')
            return None

    @staticmethod
    def __detect_viewer_type(path):

        ext_of_file = mt.MimeTypes().guess_type(path)[0]
        if ext_of_file is None:
            return None

        if ext_of_file.__contains__('text/'):
            return TextViewer
        elif ext_of_file.__contains__('image/'):
            return ImageViewer
