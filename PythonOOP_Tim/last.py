# Static method

class Math:
    # They don't change anything
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

print(Math.add10(5))