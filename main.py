class Stack:

    def __init__(self, string):

        self.string = string[::-1]
        self.list = '[]'
        self.dict = '{}'
        self.tuple = '()'

    def is_empty(self) -> bool:

        '''Проверка стека на пустоту. Метод возвращает True или False.'''

        if self.string:
            return True
        else:
            return False

    def push(self) -> None:

        '''Добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''

        pass

    def pop(self) -> str:

        '''Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека.'''

        print(self.string[::-1])
        print('В классе: ', self.string)
        for index, element in enumerate(self.string):
            if index == len(self.string) - 1:
                break
            if index == 0:
                continue
            element_stack = element + self.string[index-1]

            if (element_stack == self.list or
            element_stack == self.dict or
            element_stack == self.tuple):
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

            if (element_stack == self.list or
            element_stack == self.dict or
            element_stack == self.tuple):
                return element_stack
            
             

    def size(self) -> int:
        
        '''Возвращает количество элементов в стеке.'''

        pass


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
    c = Stack(list_of_strings[1])
    d = Stack(list_of_strings[2])
    print(a.is_empty(), b.is_empty())

    print(b.peek())
    print(c.peek())
    print(d.peek())

    print(c.pop())
    print(c.pop())