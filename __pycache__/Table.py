class Table:
    def __init__(self, number):
        self.number = number
        self.amount_of_people = 0
     
    def getNumber(self):
        return self.number

    def setNumber(self, newNumber):
        self.number = newNumber