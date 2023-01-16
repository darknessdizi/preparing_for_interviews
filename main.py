class Stack:

    def __init__(self, string):

        self.string = string[::-1]

    def is_empty(self) -> bool:

        '''Проверка стека на пустоту. Метод возвращает True или False.'''

        if self.string:
            return True
        else:
            return False

    def push(self) -> None:

        '''Добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''

        pass

    def _element_search(self):
        pass

    def pop(self) -> str:

        '''Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека.'''

        print(self.string[::-1])
        print('Объект класса: ', self.string)
        for index, element in enumerate(self.string):
            if index == 0:
                continue
            element_stack = element + self.string[index-1]

            if element_stack in ['{}', '[]', '()']:
                end = index - 1
                begin = index + 1
                self.string = self.string[:end] + self.string[begin:]
                print('В классе удаление: ', self.string)
                return element_stack

    def peek(self) -> str:
        
        '''Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''

        for index, element in enumerate(self.string):
            if index == len(self.string) - 1:
                break
            if index == 0:
                continue
            element_stack = element + self.string[index-1]

            if element_stack in ['{}', '[]', '()']:
                return element_stack
            
    def size(self) -> int:
        
        '''Возвращает количество элементов в стеке.'''

        count_tuple = self.string.count('(') + self.string.count(')')
        count_list = self.string.count('[') + self.string.count(']')
        count_dict = self.string.count('{') + self.string.count('}')
        if count_tuple % 2 == 0 and count_list % 2 == 0 and count_dict % 2 == 0:
            count = int((count_tuple + count_list + count_dict) / 2)
            return count


list_of_strings = [
    '',
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


if __name__ == '__main__':
    a = Stack(list_of_strings[0])
    b = Stack(list_of_strings[0])
    c = Stack(list_of_strings[4])
    d = Stack(list_of_strings[2])
    #print(a.is_empty(), b.is_empty())

    '''print(b.peek())
    print(c.peek())
    print(d.peek())

    print(c.pop())
    print(c.pop())
    print(c.pop())'''
    print(c.size())
    print(c.pop())
    print(c.pop())
    print(c.pop())
    print(c.pop())
    print(c.pop())
    print(c.pop())
    print(c.size())