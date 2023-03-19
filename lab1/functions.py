def basic_calculations(num1, num2, operation):
    operation = operation.lower()
    match operation:
        case "add":
            return num1+num2
        case "sub":
            return num1-num2
        case "mul":
            return num1*num2
        case "div":
            if num2==0:
                return "infinity"
            return num1/num2
        case _:
            return "Check your input! Try again."

def even_numbers_list(list_of_nums):
    return [num for num in list_of_nums if num %2==0]



