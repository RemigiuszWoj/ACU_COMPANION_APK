import math

class matchStatisticks():
    def sum_list(self, numbers:list) -> float:
        try:
            return sum([float(i) for i in numbers]) 
        except ValueError:
            return "List must consist of numbers."

    def expected_value(self, number:list) -> float:
        try:
            return self.sum_list(number) / len(number)
        except ZeroDivisionError:
            return "Division by 0."
    
    def Variance(self, numbers:list) -> float:
        try:
            return sum([(float(i) - self.expected_value(numbers)) ** 2 for i in numbers]) / len(numbers)
        except ValueError:
            return "List must consist of numbers."
        except ZeroDivisionError:
            return "Division by 0."
    
    def standard_deviation(self, numbers:list) -> float:
        try:
            return math.sqrt(self.Variance(numbers))
        except ValueError: 
            return "List must consist of numbers."
        except ZeroDivisionError:
            return "Division by 0."


List = [['1', '4', '7'], ['4', '-3', '2'], ['3', '6', '9']]

mat = matchStatisticks()
print(mat.sum_list(List[1]))
print(mat.expected_value(List[1]))
print(mat.Variance(List[1]))
print(mat.standard_deviation(List[1]))