class FourCal:
    def setdata(self, first, second):
        self.first =  first
        self.second =second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal()
b = FourCal()

a.setdata(4,2)

print(a.first, a.second)




class FourCal2:
    def __init__(self, first, second):
        self.first =  first
        self.second =second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result