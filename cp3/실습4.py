import numpy as np

A = np.array(
    [
        [1,1,1,1],
        [2,-1,2,-1],
        [3,2,-1,2],
        [1,3,2,-1]
    ]
)

B = np.array(
    [
        [10],
        [3],
        [11],
        [9]
    ]
)


result = np.linalg.inv(A) @ B

for i in result:
    print(i)
