from TextViewer import TextViewer
from ViewerCreator import ViewerCreator

image = ViewerCreator().create_viewer("C:\\Users\\makar\\Desktop\\1.jpg")
text: TextViewer = ViewerCreator().create_viewer("D:\\GIT\\JezykiS\\lab3\\lab3Ex2\\f2.txt")

text.view()
print(text.get_data())

image.view()

