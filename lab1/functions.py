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

