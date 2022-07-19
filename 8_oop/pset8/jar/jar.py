class Jar:
    def __init__(self, capacity=12):
        # if capacity is not int raise ValueError
        self.size = 0
        self.capacity = capacity
        if type(capacity) != int:
            raise ValueError
        elif capacity < 0:
            raise ValueError

    def __str__(self):
        # return str with num of 🍪 in jar
        cookies = ""
        for _ in range(self.size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        # add n cookies to jar
        # if exceed its capacity, raise ValueError
        if (self.size + n) <= self.capacity:
            self.size += n
        else:
            raise ValueError

    def withdraw(self, n):
        # remove n cookies form jar
        # if not enough cookies in jar, raise ValueError
        if (self.size - n) >= 0:
            self.size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        # return jar's capacity
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        # return num of cookies in jar
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
