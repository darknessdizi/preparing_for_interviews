class Stack:

    def __init__(self, string):

        self.string = string[::-1]

    def is_empty(self) -> bool:

        '''Проверка стека на пустоту. Метод возвращает True или False.'''

        if self.string:
            return True
        else:
            return False

    def push(self, new_element) -> None:

        '''Добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''

        for index, element in enumerate(self.string):
            if index == 0:
                continue
            element_stack = element + self.string[index-1]

            if element_stack in ['{}', '[]', '()']:
                self.string = self.string[:index] + new_element[::-1] + self.string[index:]
                break

    def pop(self) -> str:

        '''Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека.'''

        for index, element in enumerate(self.string):
            if index == 0:
                continue
            element_stack = element + self.string[index-1]

            if element_stack in ['{}', '[]', '()']:
                first_index = index - 1
                second_index = index + 1
                self.string = self.string[:first_index] + self.string[second_index:]
                return element_stack

    def peek(self) -> str:
        
        '''Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''

        for index, element in enumerate(self.string):
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
    c = Stack(list_of_strings[1])

    print(c.string[::-1])
    print(c.is_empty())
    print(c.peek())
    print(c.size())
    print('*' * 40)

    for i in range(c.size()):
        print(c.string[::-1])
        print('Удалён ', c.pop())
        print('Следующий ', c.peek())
        print('-' * 40)

    print('Наша строка', c.string[::-1])