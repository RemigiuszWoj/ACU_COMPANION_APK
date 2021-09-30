import math

class mathStatisticks():
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
    
    def variance(self, numbers:list) -> float:
        try:
            return sum([(float(i) - self.expected_value(numbers)) ** 2 for i in numbers]) / len(numbers)
        except ValueError:
            return "List must consist of numbers."
        except ZeroDivisionError:
            return "Division by 0."

    def unloaded_estimator(self, numbers:list) -> float:
        try:
            return sum([(float(i) - self.expected_value(numbers)) ** 2 for i in numbers]) / len(numbers) - 1
        except ValueError:
            return "List must consist of numbers."
        except ZeroDivisionError:
            return "Division by 0."

    def standard_deviation(self, numbers:list) -> float:
        try:
            return math.sqrt(self.variance(numbers))
        except ValueError: 
            return "List must consist of numbers."
        except ZeroDivisionError:
            return "Division by 0."
    
    def three_sigmas(self,numbers:list) -> float:
        try:
            return (3 * self.standard_deviation(numbers)) + self.expected_value(numbers)
        except ValueError: 
            return "List must consist of numbers."

    def three_sigmas_limits(self, numbers:list) -> list:
        try:
            return [float(i) for i in numbers if float(i) < self.three_sigmas(numbers) and float(i) > - self.three_sigmas(numbers)]
        except ValueError: 
            return "List must consist of numbers."




List = [['1', '4', '7'], ['4', '-3', '2'], ['3', '6', '9']]

mat = mathStatisticks()
# print(mat.sum_list(List[1]))
# print(mat.expected_value(List[1]))
# print(mat.Variance(List[1]))
# print(mat.unloaded_estimator(List[1]))
# print(mat.standard_deviation(List[1]))
print(mat.three_sigmas(List[1]))
print(*mat.three_sigmas_limits(List[1]))
mat