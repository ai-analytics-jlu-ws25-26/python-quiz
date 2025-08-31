# When training a ML model, it's often necessary to normalize input features.
# Normalize a list of numerical values to the range [0, 1].


def normalize(list_of_numbers):
    """
    Normalize a list of numerical values to the range [0, 1].

    >>> normalize([10, 20, 30, 40, 50])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    >>> normalize([5, 5, 5])
    [0.0, 0.0, 0.0]
    >>> normalize([-10, 0, 10])
    [0.0, 0.5, 1.0]
    """
