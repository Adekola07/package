class CustomError(Exception):
    """Custom exception class for specific errors."""
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
def critical_function(value):
    if value < 0:
        raise CustomError("The value cannot be negative.", 1001)
try:
    critical_function(-1)
except CustomError as e:
    print(f"Captured error: {e} with code {e.code}")