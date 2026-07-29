import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Girdiyi NumPy array'e çeviriyoruz
    x = np.asarray(x)
    
    return 1 / (1 + np.exp(-x))