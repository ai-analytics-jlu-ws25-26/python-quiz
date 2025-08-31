# The quality of a ML model is typically evaluated by comparing the model's predictions to the true values.
# Calculate the Mean Squared Error (MSE) between the true and predicted values.


def mean_squared_error(y_true, y_pred):
    """
    Calculate the Mean Squared Error (MSE) between two lists of numbers.

    >>> mean_squared_error([1, 2, 3], [1, 2, 3])
    0.0
    >>> mean_squared_error([1, 2, 3], [2, 2, 2])
    0.6666666666666666
    >>> mean_squared_error([0, 0, 0], [1, 1, 1])
    1.0
    """
