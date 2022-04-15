from MultipleAccumulate import MultipleAccumulate
from TextViewer import TextViewer
from ViewerCreator import ViewerCreator


class Runtime:
    @staticmethod
    def main():
        image = ViewerCreator().create_viewer("C:\\Users\\makar\\Desktop\\1.jpg")
        text: TextViewer = ViewerCreator().create_viewer("D:\\GIT\\JezykiS\\lab3\\lab3Ex2\\f2.txt")

        text.view()

        print(text.get_data())
        image.view()

        sum = lambda a, b: a + b
        sum.__name__ = 'sum'
        mul = lambda a, b: a * b
        mul.__name__ = 'mul'
        div = lambda a, b: a / b
        div.__name__ = 'div'

        list_of_values = [1, 2, 3, 4]

        m_a = MultipleAccumulate(list_of_values, sum, mul, div)

        for duck in m_a, text:
            print(duck.get_data())


if __name__ == '__main__':
    Runtime().main()

