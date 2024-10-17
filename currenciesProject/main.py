from shekel import Shekel
from dollar import Dollar
from euro import Euro


def add(currency1, currency2):
    """
       Add two currency objects together.

       Args:
           currency1: The first currency object.
           currency2: The second currency object.

       Returns:
           The result of adding currency1 and currency2.
    """
    return currency1 + currency2


def sub(currency1, currency2):
    """
        Subtract one currency object from another.

        Args:
            currency1: The currency object to subtract from.
            currency2: The currency object to subtract.

        Returns:
            The result of subtracting currency2 from currency1.
    """
    return currency1 - currency2


# Ex_B ###################################################


def apply(act, currency1, currency2):
    """
        Apply a specified action to two currency objects.

        Args:
            act: The action to perform ('add' or 'sub').
            currency1: The first currency object.
            currency2: The second currency object.

        Returns:
            The result of applying the action to currency1 and currency2.
    """
    if act == 'add':
        if type(currency1) is Shekel:
            return Shekel(currency1 + currency2)
        elif type(currency1) is Dollar:
            return Dollar((currency1 + currency2) * rates[('nis', 'dollar')])
        elif type(currency1) is Euro:
            return Euro((currency1 + currency2) * rates[('nis', 'euro')])
    elif act == 'sub':
        if type(currency1) is Shekel:
            return Shekel(currency1 - currency2)
        elif type(currency1) is Dollar:
            return Dollar((currency1 - currency2) * rates[('nis', 'dollar')])
        elif type(currency1) is Euro:
            return Euro((currency1 - currency2) * rates[('nis', 'euro')])


# Ex_C ###################################################


def type_tag(currency):
    """
        Get the currency tag based on its type.

        Args:
            currency: The currency object.

        Returns:
            The currency tag.
    """
    return type_tag.tags[type(currency)]


type_tag.tags = {Shekel: 'nis', Dollar: 'dollar', Euro: 'euro'}


def dollar_to_nis(currency):
    """
        Convert Dollar to Shekel.

        Args:
            currency: The Dollar object.

        Returns:
            The equivalent value in Shekel.
    """
    return Shekel(currency.amount())


def euro_to_nis(currency):
    """
       Convert Euro to Shekel.

       Args:
           currency: The Euro object.

       Returns:
           The equivalent value in Shekel.
    """
    return Shekel(currency.amount())


def dollar_to_euro(currency):
    """
       Convert Dollar to Euro.

       Args:
           currency: The Dollar object.

       Returns:
           The equivalent value in Euro.
    """
    return Euro(currency.get_original_sum() * rates[('dollar', 'euro')])


coercions = {('dollar', 'nis'): dollar_to_nis,
             ('euro', 'nis'): euro_to_nis,
             ('dollar', 'euro'): dollar_to_euro}


def coerce_apply(act, currency1, currency2):
    """
       Apply an action to two currency objects, coercing if necessary.

       Args:
           act: The action to perform ('add' or 'sub').
           currency1: The first currency object.
           currency2: The second currency object.

       Returns:
           The result of applying the action to currency1 and currency2.
    """
    t_currency1, t_currency2 = type_tag(currency1), type_tag(currency2)
    if t_currency1 != t_currency2:
        if (t_currency1, t_currency2) in coercions:
            t_currency1, currency1 = t_currency2, coercions[(t_currency1, t_currency2)](currency1)
        elif (t_currency2, t_currency1) in coercions:
            t_currency2, currency2 = t_currency1, coercions[(t_currency2, t_currency1)](currency2)
        else:
            return "No coercion possible."
    return Shekel(coerce_apply.implementations[(act, t_currency1)](currency1, currency2))


coerce_apply.implementations = {('add', 'nis'): add, ('add', 'dollar'): add, ('add', 'euro'): add,
                                ('sub', 'nis'): sub, ('sub', 'dollar'): sub, ('sub', 'euro'): sub }


# rates dict #############################################

rates = {('dollar', 'nis'): 3.82, ('euro', 'nis'): 4.07}
rates[('nis', 'dollar')] = 1/rates[('dollar', 'nis')]
rates[('nis', 'euro')] = 1/rates[('euro', 'nis')]
rates[('dollar', 'euro')] = rates[('dollar', 'nis')]/rates[('euro', 'nis')]
rates[('euro', 'dollar')] = rates[('euro', 'nis')]/rates[('dollar', 'nis')]

# main ###################################################

if __name__ == '__main__':
    # Examples of running:
    shekel = Shekel(50)
    dollar = Dollar(50)
    euro = Euro(50)
    print(coerce_apply('add', shekel, dollar))
    print(coerce_apply('add', shekel, euro))
    print(coerce_apply('add', dollar, shekel))
    print(coerce_apply('sub', dollar, euro))
    print(coerce_apply('sub', euro, shekel))
    print(coerce_apply('sub', euro, dollar))

    s = Shekel(50)
    d = Dollar(50)
    e = Euro(50)
    print(d.amount())

    print(e.amount())
    print(d + s)
    print(add(e, d))
    z = eval(repr(d))
    print(z)
    print(s)
    print(e)
    print(apply('add', Shekel(50), Dollar(20)))
    print(apply('add', Dollar(50), Euro(20)))
    print(apply('sub', Dollar(50), Euro(20)))

    print(coercions[('dollar', 'nis')](Dollar(50)))
    print(coerce_apply('add', Shekel(50), Dollar(20)))
    print(coerce_apply('add', Dollar(50), Euro(20)))
    print(coerce_apply('sub', Dollar(50), Euro(20)))



