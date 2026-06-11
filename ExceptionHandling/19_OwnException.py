class MyZeroDivisionError(ZeroDivisionError):
    pass

def division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")
    
# division(False)
division(True)