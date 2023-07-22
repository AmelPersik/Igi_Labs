class MyContextManager():
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        if (exc_type == ZeroDivisionError):
            return True

with MyContextManager():
    1/0

