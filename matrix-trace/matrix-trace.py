import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Girdiyi güvenli bir şekilde NumPy array'e çeviriyoruz
    A = np.asarray(A)
    
    # NumPy'ın yerleşik iz (trace) fonksiyonunu kullanıyoruz
    return np.trace(A)