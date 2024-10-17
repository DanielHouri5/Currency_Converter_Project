
class Dollar(object):
    """
        A class representing money in US Dollars.

        Attributes:
            __original_sum (float): The original amount of money in US Dollars.
    """
    def __init__(self, original_sum):
        """
            Initialize a Dollar object with the original sum.

            Args:
                original_sum (float): The original amount of money in US Dollars.
        """
        self.__original_sum = original_sum

    def __str__(self):
        """
            Return a string representation of the Dollar object.

            Returns:
                str: The string representation of the Dollar object.
        """
        return str(self.get_original_sum()) + "$"

    def __repr__(self):
        """
            Return a string representation of the Dollar object for debugging purposes.

            Returns:
                str: The string representation of the Dollar object.
        """
        return f"Dollar({self.get_original_sum()})"

    def __add__(self, other):
        """
            Add two Dollar objects together.

            Args:
                other (Dollar): The Dollar object to be added.

            Returns:
                float: The sum of the amounts in Dollars.
        """
        return self.amount() + other.amount()

    def __sub__(self, other):
        """
            Subtract one Dollar object from another.

            Args:
                other (Dollar): The Dollar object to be subtracted.

            Returns:
                float: The difference between the amounts in Dollars.
        """
        return self.amount() - other.amount()

    def get_original_sum(self):
        """
            Get the original sum of money in US Dollars.

            Returns:
                float: The original sum of money in US Dollars.
        """
        return self.__original_sum

    def amount(self):
        """
            Get the equivalent amount of money in US Dollars converted to Shekels.

            Returns:
                float: The equivalent amount of money in US Dollars.
        """
        from main import rates
        return self.get_original_sum() * rates[('dollar', 'nis')]
