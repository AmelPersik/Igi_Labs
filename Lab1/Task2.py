import const
def basic_calculations(num1, num2,
                      operation):
    operation = operation.lower()
    match operation:
        case const.add_func:
            return num1 + num2
        case const.sub_func:
            return num1 - num2
        case const.mul_func:
            return num1 * num2
        case const.div_func:
            if num2 == 0:
                return "Infinity"
            return num1 / num2
        case _:
            return "Check your input!" \
                   " Something is incorrect!" \
                   " Try Again!"
