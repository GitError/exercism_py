"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module provides functions to calculate the preparation time, 
baking time, and total elapsed time for making lasagna.
"""

# Constants
EXPECTED_BAKE_TIME: int = 40  # Total expected bake time in minutes
LAYER_BAKE_TIME: int = 2      # Time to prepare each layer in minutes

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - Baking time already elapsed.
    :return: int - Remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    This function takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate preparation time in minutes.

    :param number_of_layers: int - The number of layers in the lasagna.
    :return: int - Preparation time in minutes.

    This function calculates the total preparation time required for the given
    number of lasagna layers, assuming each layer takes `LAYER_BAKE_TIME` minutes.
    """
    return LAYER_BAKE_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers: int = 1, elapsed_bake_time: int = 0) -> int:
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - The number of layers in the lasagna.
    :param elapsed_bake_time: int - Time already spent baking.
    :return: int - Total time elapsed (in minutes) preparing and cooking.

    This function calculates the total elapsed time spent on preparing and
    baking the lasagna, combining the preparation time for the layers and
    the time already spent baking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time