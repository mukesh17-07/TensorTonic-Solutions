import numpy as np

def dot_product(x: list, y: list) -> float:
    
    data1 = np.asarray(x, dtype=float)
    data2 = np.asarray(y, dtype=float)

    return float(np.dot(x,y))
    