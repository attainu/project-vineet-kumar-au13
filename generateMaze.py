import numpy as np
# generate random maze Of N * M
n = int(input("Enter the value for N ") or "4")
m = int(input("Enter the value for M ") or "4")
A = np.random.randint(2, size=(n, m))
print(A)

np.savetxt("input.txt", np.array(A), fmt="%s")
