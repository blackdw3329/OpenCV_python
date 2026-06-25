import numpy as np

A = np.array(
    [
        [1,2,3],
        [10,-1,-5],
        [6,7,5]
    ]
)

np_eye = np.identity(3)

array_cal = A@A@A - 5*A@A - 4*A - 98*np_eye

print(array_cal)
