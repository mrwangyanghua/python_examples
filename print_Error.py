#!/usr/bin/python
# -*- coding:utf-8 -*-
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occured
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that't not 
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempting new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


if __name__ == "__main__":
    print("Test the customized exception classes")
    try:
        raise InputError("expression", "The error message")
    except InputError as inst:
        print("Catch the InputError", inst.args)
    finally:
        print("Clean up Actions")
