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
        except TypeError:
            return "unsupported operand type(s) for /: 'str' and 'int'"

    
    def variance(self, numbers:list) -> float:
        try:
            return sum([(float(i) - self.expected_value(numbers)) ** 2 for i in numbers]) / len(numbers)
        except TypeError:
            return "unsupported operand type(s) for /: 'str' and 'int'"
        except ZeroDivisionError:
            return "Division by 0."

    def unloaded_estimator(self, numbers:list) -> float:
        try:
            return sum([(float(i) - self.expected_value(numbers)) ** 2 for i in numbers]) / len(numbers) - 1
        except TypeError:
            return "unsupported operand type(s) for /: 'str' and 'int'"
        except ZeroDivisionError:
            return "Division by 0."

    def standard_deviation(self, numbers:list) -> float:
        try:
            return math.sqrt(self.variance(numbers))
        except TypeError:
            return "unsupported operand type(s) for /: 'str' and 'int'"
 
    def three_sigmas(self,numbers:list) -> float:
        try:
            return (3 * self.standard_deviation(numbers)) + self.expected_value(numbers)
        except TypeError:
            return "unsupported operand type(s) for /: 'str' and 'int'"

    def three_sigmas_limits(self, numbers:list) -> list:
        try:
            return [float(i) for i in numbers if float(i) < self.three_sigmas(numbers) and float(i) > - self.three_sigmas(numbers)]
        except TypeError:
            return "unsupported operand type(s) for /: 'str' and 'int'"

