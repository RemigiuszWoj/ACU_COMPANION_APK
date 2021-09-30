import math_operation

def test_sum_list():
    mat = math_operation.mathStatisticks()
    numbers = ['4', '-3', '2']
    lethers = ['4', 'a', '2']
    #empty = []
    
    assert mat.sum_list(numbers) == 3
    assert mat.sum_list(lethers) == "List must consist of numbers."
    #assert mat.sum_list(empty) == "List must consist of numbers."

def test_expected_value():
    mat = math_operation.mathStatisticks()
    numbers = ['4', '-3', '2']
    lethers = ['4', 'a', '2']
    empty = []
    
    assert mat.expected_value(numbers) == 1.0
    assert mat.expected_value(lethers) == "unsupported operand type(s) for /: 'str' and 'int'"
    assert mat.expected_value(empty) == "Division by 0."

def test_variance():
    mat = math_operation.mathStatisticks()
    numbers = ['4', '-3', '2']
    lethers = ['4', 'a', '2']
    empty = []
    
    assert mat.variance(numbers) == 8.666666666666666
    assert mat.variance(lethers) == "unsupported operand type(s) for /: 'str' and 'int'"
    assert mat.variance(empty) == "Division by 0."

def test_unloaded_estimator():
    mat = math_operation.mathStatisticks()
    numbers = ['4', '-3', '2']
    lethers = ['4', 'a', '2']
    empty = []
    
    assert mat.unloaded_estimator(numbers) == 7.666666666666666
    assert mat.unloaded_estimator(lethers) == "unsupported operand type(s) for /: 'str' and 'int'"
    assert mat.unloaded_estimator(empty) == "Division by 0."

def test_standard_deviation():
    mat = math_operation.mathStatisticks()
    numbers = ['4', '-3', '2']
    lethers = ['4', 'a', '2']
   
    assert mat.standard_deviation(numbers) == 2.943920288775949
    assert mat.standard_deviation(lethers) == "unsupported operand type(s) for /: 'str' and 'int'"
   
def test_three_sigmas():
    mat = math_operation.mathStatisticks()
    numbers = ['4', '-3', '2']
    lethers = ['4', 'a', '2']
    empty = []
    print(mat.three_sigmas(lethers))
    assert mat.three_sigmas(numbers) == 9.831760866327846
    assert mat.three_sigmas(lethers) == "unsupported operand type(s) for /: 'str' and 'int'unsupported operand type(s) for /: 'str' and 'int'unsupported operand type(s) for /: 'str' and 'int'unsupported operand type(s) for /: 'str' and 'int'"
    assert mat.three_sigmas(empty) == "unsupported operand type(s) for /: 'str' and 'int'unsupported operand type(s) for /: 'str' and 'int'unsupported operand type(s) for /: 'str' and 'int'Division by 0."

def test_three_sigmas_limits():
    mat = math_operation.mathStatisticks()
    numbers = ['4', '-3', '2']
    lethers = ['4', 'a', '2']
   # empty = []
   
    assert mat.three_sigmas_limits(numbers) == [4.0, -3.0, 2.0]
    assert mat.three_sigmas_limits(lethers) == "unsupported operand type(s) for /: 'str' and 'int'"
   # assert mat.three_sigmas_limits(empty) == []









