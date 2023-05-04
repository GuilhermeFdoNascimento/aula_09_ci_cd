import methods

def test_soma():
    # given two numbers
    num1 = 2
    num2 = 3

    # when we calculate the sum
    output = methods.soma(num1, num2)

    # then the sum should be 5
    assert output == 5

def test_subtracao():
    # given two numbers
    num1 = 2
    num2 = 3

    # when we calculate the subtraction
    output = methods.subtracao(num1, num2)

    # then the subtraction should be -1
    assert output == -1

def test_multiplicacao():
    # given two numbers
    num1 = 2
    num2 = 3

    # when we calculate the multiplication
    output = methods.multiplicacao(num1, num2)

    # then the multiplication should be 6
    assert output == 6

def test_divisao():
    # given two numbers
    num1 = 2
    num2 = 3

    # when we calculate the division
    output = methods.divisao(num1, num2)

    # then the division should be 0.6666666666666666
    assert output == 0.6666666666666666
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14