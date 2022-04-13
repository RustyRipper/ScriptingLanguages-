from ViewerCreator import ViewerCreator

text = ViewerCreator().create_viewer("D:\\GIT\\JezykiS\\lab3\\lab3Ex2\\f2.txt")
image = ViewerCreator().create_viewer("C:\\Users\\makar\\Desktop\\1.jpg")
text.view()
print(text.get_data())

image.view()


