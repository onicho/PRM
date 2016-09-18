#REFERENCE
# the execution of the Error classes was adopted from a python tutorial
# which can be accessed here https://docs.python.org/3/tutorial/errors.html


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

