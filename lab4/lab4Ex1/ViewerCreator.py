import mimetypes as mt

from FileViewer import FileViewer
from ImageViewer import ImageViewer
from TextViewer import TextViewer


class ViewerCreator:
    def __init__(self):
        pass

    def create_viewer(self, path):
        file_viewer: FileViewer
        type_of_file = self.__detect_viewer_type(path)
        if type_of_file.__contains__('text/'):
            file_viewer = TextViewer(path)
            return file_viewer
        elif type_of_file.__contains__('image/'):
            file_viewer = ImageViewer(path)
            return file_viewer

    @staticmethod
    def __detect_viewer_type(path):
        return str(mt.MimeTypes().guess_type(path))
