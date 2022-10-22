class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())

class List:
    def __init__(self, collection=None):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value,
                                               self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            return False
        if i < len(self) / 2:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
            return curr_pointer.get_value()

        curr_pointer = self._finish_pointer
        for j in range(len(self) - i - 1):
            curr_pointer = curr_pointer.get_prev()

        return curr_pointer.get_value()

    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    def pop(self, i):
        mas = List()
        mas2 = self[i]
        for j in range(len(self) - 1):
            if j < i:
                mas.append(self[j])
            else:
                mas.append(self[j + 1])
        self = mas
        return mas2

    def __add__(self, b):
        if isinstance(b, list):
            for i in range(len(b)):
                self.append(b[i])
            return self

    def __radd__(self, b):
        if isinstance(b, list):
            for i in range(len(self)):
                b.append(self[i])
            return b



A = [9, 78, 97, 7, 5, 2, 786, 9]
B= [8 ,0 ,6, 790, 97, 2, 35, 53, 8, 78, 536, 56, 235]
A.pop(4)
B.append(12)
print(A)
print(B)
print(A+B)



