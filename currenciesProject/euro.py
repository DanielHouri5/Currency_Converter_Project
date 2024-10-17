
class Euro(object):
    """
        A class representing money in Euros.

        Attributes:
            __original_sum (float): The original amount of money in Euros.
    """
    def __init__(self, original_sum):
        """
            Initialize a Euro object with the original sum.

            Args:
                original_sum (float): The original amount of money in Euros.
        """
        self.__original_sum = original_sum

    def __str__(self):
        """
            Return a string representation of the Euro object.

            Returns:
                str: The string representation of the Euro object.
        """
        return str(self.get_original_sum()) + "€"

    def __repr__(self):
        """
           Return a string representation of the Euro object for debugging purposes.

           Returns:
               str: The string representation of the Euro object.
        """
        return f"Euro({self.get_original_sum()})"

    def __add__(self, other):
        """
            Add two Euro objects together.

            Args:
                other (Euro): The Euro object to be added.

            Returns:
                float: The sum of the amounts in Euros.
        """
        return self.amount() + other.amount()

    def __sub__(self, other):
        """
            Subtract one Euro object from another.

            Args:
                other (Euro): The Euro object to be subtracted.

            Returns:
                float: The difference between the amounts in Euros.
        """
        return self.amount() - other.amount()

    def get_original_sum(self):
        """
           Get the original sum of money in Euros.

           Returns:
               float: The original sum of money in Euros.
        """
        return self.__original_sum

    def amount(self):
        """
            Get the equivalent amount of money in Euros converted to Shekels.

            Returns:
                float: The equivalent amount of money in Euros.
        """
        from main import rates
        return self.get_original_sum() * rates[('euro', 'nis')]
