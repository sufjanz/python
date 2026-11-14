def add (x, y):
    return x + y

def concatenate(x , y):
    return str(x) + str(y)

def operate(operation, x ,y):
    """

    :param operation: the operation function to be performed (param1)
    :param x: The first operand(param2)
    :param y: The second operand(param3)
    :return:
    """

    return operation (x, y)


result_sum = operate(add, 3, 5)
result_concatenate = operate(concatenate, "Hello", "World")
