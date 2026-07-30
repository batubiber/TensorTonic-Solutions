import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Girdiyi NumPy array'e çeviriyoruz (liste veya tuple verilme ihtimaline karşı)
    A = np.asarray(A)
    
    # NumPy'ın yerleşik transpoz özelliğini kullanıyoruz
    return A.T