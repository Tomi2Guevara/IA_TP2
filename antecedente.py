

class Antecedent():
    def __init__(self, name, val, type = None):
        self.name = name
        self.val = val
        self.type = type

    def __str__(self):
        return self.name + " is " + str(self.value)