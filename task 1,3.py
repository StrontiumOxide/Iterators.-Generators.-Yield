# Доработать класс FlatIterator в коде ниже. 
# Должен получиться итератор, который принимает список списков 
# и возвращает их плоское представление, т. е. последовательность, 
# состоящую из вложенных элементов. Функция test в коде ниже также 
# должна отработать без ошибок.


class FlatIterator:

    def __init__(self, list_of_list: list[list]) -> None:
        self.lists = self.extracting(list_of_list)
        self.lenth = len(self.lists)

    def __iter__(self):
        self.order = 0
        return self

    def __next__(self):

        if self.order >= self.lenth:
            raise StopIteration
        
        item = self.lists[self.order]
        self.order += 1

        return item
    
    def extracting(self, lists: list[any]) -> list:
        result = []
        for item in lists:
            if isinstance(item, list):
                result.extend(self.extracting(item))
            else:
                result.append(item)
        return result


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()