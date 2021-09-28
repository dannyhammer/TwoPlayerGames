"""
Sample Class

This file contains an example of a class file to showcase naming conventions and
documentation style.
"""

class SampleClass:
    """
    A sample class to be used as a reference for documentation and style

    Attributes
    ----------
    attr : type
        desc
    name : str
        The name of this SampleClass instance. Uniquely identifies this instance.

    Method
    ------
    mthd(params):
        desc
    add(x: int, y: int):
        Adds two parameters together and returns their sum.
    """

    def __init__(self, name: str):
        """
        Constructs a new SampleClass instance for a given game.

        Parameters
        ----------
            name : str
                Name of this SampleClass instance. Uniquely identifies this instance.
        """
        self.name = name

    def add(self, x: int, y: int) -> int:
        """
        Adds the two provided parameters together and returns their sum.

        Must be supplied only two integers as parameters.

        Parameters
        ----------
            x : int
                The first parameter to add.
            y : int
                The second parameter to add.

        Raises
        ------
            TypeError
                If either supplied parameters is not an integer.

        Returns
        -------
            the_sum : int
                The sum of the two parameters.
        """
        if type(x) is not type(y) and type(x) is not int:
            raise ValueError("Non-integer argument supplied")

        the_sum = x + y

        return the_sum
