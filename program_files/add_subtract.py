import numpy as np

def add(array1, array2):

    """
    TBD !
    """

    
    assert isinstance(array1, np.ndarray)
    assert isinstance(array2, np.ndarray)
    assert len(array1) > 0
    assert len(array2) > 0
    assert len(array1) == len(array2)
    

    return array1 + array2
