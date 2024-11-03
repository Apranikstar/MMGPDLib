import numpy as np

def genSkewedData(initial, final, num_points, scatteringRate):

    # Ensure initial is less than final
    if initial >= final:
        raise ValueError("Initial value must be less than final value")

    # Generate values in the range [0, 1]
    uniform_random_values = np.random.uniform(0, 1, num_points)
    
    # Apply the transformation to skew values towards initial
    skewed_values = np.power(uniform_random_values,scatteringRate)
    # Transform values back to the range [initial, final], If you're confused the second part is calculated first.
    scaled_values = initial + (final - initial) * skewed_values
    # Remove zero values
    non_zero_values = scaled_values[scaled_values != initial]

    # Sort the values in ascending order
    sorted_values = np.sort(non_zero_values)
    return sorted_values

