import numpy as np

# 1. Create a vector with values ranging from 10 to 49.
a = np.arange(10, 50)
print(a)

# 2. Create a 3x3 matrix with values ranging from 0 to 8.
eight = np.arange(0, 9).reshape(3,3)
print(eight)

# 3. Create a 3x3 identity matrix.
identity = np.eye(3, 3)
print(identity)

# 4. Create a 3x3x3 array with random values.
randomm = np.random.random((3, 3))
print(randomm)

# 5. Create a 10x10 array with random values and find the minimum and maximum values.
randomm = np.random.random((10, 10))
max_val = randomm.max()
min_val = randomm.min()
print(randomm)
print(max_val)
print(min_val)

# 6. Create a random vector of size 30 and find the mean value.
vect = np.random.random(30)
mean1 = vect.mean()
print(mean1)

# 7. Normalize a 5x5 random matrix.

norma = np.random.random((5, 5))
norm = (norma - norma.min())/(norma.max() - norma.min())
print(norm)

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).

mat1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 7, 9],
    [5, 6, 6],
    [9, 6, 7]
])
mat2 = np.array([
    [2, 9],
    [4, 6],
    [8, 2]
])

mult = mat1 @ mat2
print(mult)

# 9. Create two 3x3 matrices and compute their dot product.  
A = np.array([
    [1, 2, 1],
    [0, 1, 0],
    [2, 3, 4]
])

B = np.array([
    [2, 5, 1],
    [6, 7, 1],
    [1, 8, 1]
])
dot_pro = np.dot(A, B)
print(dot_pro)

# 10. Given a 4x4 matrix, find its transpose.  
real_mat = np.random.randint(1, 10, size = (4, 4))
print(f"real matrix:\n {real_mat}")

#tranponerlash
tr_mat = real_mat.T
print(f"transposed matrix:\n {tr_mat}")

# 11. Create a 3x3 matrix and calculate its determinant.  
mat = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
det = np.linalg.det(mat)
print(det)

# 12. Create two matrices \( A \) (3x4) and \( B \) (4x3), and compute the matrix product \( A \cdot B \).  
A = np.random.randint(1, 10, size=(3, 4))
B = np.random.randint(1, 10, size=(4, 3))

cdot = A @ B
print(cdot)

# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.  
A = np.random.randint(1, 10, size=(3, 3))
B = np.random.randint(1, 10, size=(3,))

product = A @ B

print(product)

# 14. Solve the linear system \( Ax = b \) where \( A \) is a 3x3 matrix, and \( b \) is a 3x1 column vector.  
A = np.array([
    [1, 2, 3],
    [4, 10, 6],
    [7, 8, 5]
])

b = np.array([10, 20, 30])

x = np.linalg.solve(A, b)
print(x)

# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.
A = np.random.randint(1, 10, size=(3, 3))

column_wise = A.sum(axis=0)
row_wise = A.sum(axis=1)
print(f"row wised sum:\n {row_wise}")
print(f"column wised sum:\n {column_wise}")