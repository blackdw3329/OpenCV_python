import numpy as np

A = [
    [1,2,3],
     [-1,3,-10]
]
B = [
    [2,-1],
     [3,1],
     [0,5]
]

A_np = np.array([
    [1,2,3],
     [-1,3,-10]
])

B_np = np.array([
    [2,-1],
     [3,1],
     [0,5]
])

AB = [[0,0],[0,0]]

for dot in range(len(AB)): # 0 1
    for i in range(len(AB)): # 0 1
        for x in range(len(A[0])):  # 0 1 2
            AB[dot][i] += A[dot][x]*B[x][i]

np_total = np.dot(A_np,B_np)

print(np_total)
print(AB)
