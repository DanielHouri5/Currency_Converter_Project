
class Shekel(object):
    """
      A class representing money in Shekels.

      Attributes:
          __original_sum (float): The original amount of money in Shekels.
    """
    def __init__(self, original_sum):
        """
            Initialize a Shekel object with the original sum.

            Args:
                original_sum (float): The original amount of money in Shekels.
        """
        self.__original_sum = original_sum

    def __str__(self):
        """
           Return a string representation of the Shekel object.

           Returns:
               str: The string representation of the Shekel object.
        """
        return str(self.get_original_sum()) + "nis"

    def __repr__(self):
        """
           Return a string representation of the Shekel object for debugging purposes.

           Returns:
               str: The string representation of the Shekel object.
        """
        return f"Shekel({str(self.get_original_sum())})"

    def __add__(self, other):
        """
           Add two Shekel objects together.

           Args:
               other (Shekel): The Shekel object to be added.

           Returns:
               float: The sum of the original sums of the two Shekel objects.
        """
        return self.get_original_sum() + other.amount()

    def __sub__(self, other):
        """
           Subtract one Shekel object from another.

           Args:
               other (Shekel): The Shekel object to be subtracted.

           Returns:
               float: The difference between the original sums of the two Shekel objects.
        """
        return self.get_original_sum() - other.amount()

    def get_original_sum(self):
        """
            Get the original sum of money in Shekels.

            Returns:
                float: The original sum of money in Shekels.
        """
        return self.__original_sum

    def amount(self):
        """
            Get the original sum of money in Shekels.

            Returns:
                float: The original sum of money in Shekels.
        """
        return self.get_original_sum()
