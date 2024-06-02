class IntegerSet:
    def __init__(self, integers=None):
        if integers is None:
            self.integers = set()
        else:
            self.integers = set(integers)

    def add(self, value):
        self.integers.add(value)

    def sum(self):
        return sum(self.integers)

    def mean(self):
        if not self.integers:
            return 0
        return sum(self.integers) / len(self.integers)

    def max(self):
        if not self.integers:
            return None
        return max(self.integers)

    def min(self):
        if not self.integers:
            return None
        return min(self.integers)