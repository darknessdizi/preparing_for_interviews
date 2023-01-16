class Stack:

    def __init__(self, text):
        
        self.string = text

    def is_empty(self) -> bool:

        if self.string:
            return True
        else:
            return False

    def push(self) -> None:
        pass

    def pop(self) -> str:
        pass

    def peek(self) -> str:
        pass

    def size(self) -> int:
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
    b = Stack(list_of_strings[1])
    print(a.is_empty(), b.is_empty())