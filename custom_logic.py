class DType():

    def __init__(self,value):
        self.value =value
    
    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self,other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value
    
a = DType(10)
b = DType(20)

c = a+b
print(c)