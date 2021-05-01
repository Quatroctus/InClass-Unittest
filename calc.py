

def addition(x: int, y: int) -> int:
    return x + y


def subtraction(x: int, y: int) -> int:
    return x - y


def division(x: int, y: int) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        return None


def multiplication(x: int, y: int) -> int:
    return x * y
