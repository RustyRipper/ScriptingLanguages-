class MultipleAccumulate:

    def __init__(self, data_list, *args):
        self.data_list = data_list
        self.accumulate_functions = args
        # print(self.accumulate_functions)

    def get_data(self):
        dict = {}
        for func in self.accumulate_functions:
            # print(func.__name__)
            dict[func.__name__] = self.__reduce(func, self.data_list)
        return dict

    @staticmethod
    def __reduce(func, iterable, initializer=None):
        it = iter(iterable)
        if initializer is None:
            value = next(it)
        else:
            value = initializer
        for element in it:
            try:
                value = func(value, element)
            except ZeroDivisionError:
                print('division Zero')
                return 0
        return value
