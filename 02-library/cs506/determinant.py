def determinant(A):

    n = len(A)
    AM = copy_matrix(A)

    for fd in range(n):  
        if AM[fd][fd] == 0:
            AM[fd][fd] = 1.0e-18 
        for i in range(fd+1, n): 
            crScaler = AM[i][fd] / AM[fd][fd]  
            for j in range(n):  # cr - crScaler * fdRow, one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    product = 1.0
    for i in range(n):
        product *= AM[i][i]  

    return product
