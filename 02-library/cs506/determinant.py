#recursive implementation of deteminants
def determinant(matrix):
    """Takes care of the base case scenario where it is a 2x2 matrix"""
    if len(matrix) == 2:
        return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    else:
        """recursive case:iterates through the first row"""
        result = 0
        for i in range(len(matrix[0])):
            """creates the multiplier for each sub matrix, and alternate sign
            according to the index"""
            a = matrix[0][i]
            idx = i
            multiplier = (-1)**i
            a = a*multiplier
            new_matrix = []
            for j in range(1,len(matrix)):
                """creates a sub-matrix without the column the multiplier occupies"""
                new_row = []
                for k in range(len(matrix[0])):
                    if k != i:
                        new_row.append(matrix[j][k])
                new_matrix.append(new_row)
                """find the determinant of the sub-matrix and multiply by the multiplier
                and add all the results together to get the final number"""
            result = result + determinant(new_matrix)*a
        
        return result
