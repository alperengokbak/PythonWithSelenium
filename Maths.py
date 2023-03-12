class Math():
    def __init__(self, number1, number2) -> None: # Constructor(init block)
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        return self.number1 + self.number2 
    
    def subtraction(self):
        return self.number1 - self.number2
    
    def divison(self):
        return self.number1 / self.number2 
    
    def multiplication(self):
        return self.number1 * self.number2

# Inheritence 
class Statistics(Math): # It's similiar to "extends" keywords in Java. We can use the variable, functions etc. inside of defined class.
    def __init__(self, number1, number2) -> None:
        super().__init__(number1, number2)
    
    def calculate_variance(self):
        return self.number1 * self.number2


math = Math(25, 15)
result = math.addition()
result= math.divison()

print(f"Result: {result}") # print("Result: {result}".format(result = result)) --> Both way are correct.