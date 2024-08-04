from functools import reduce

def check_if_all_rows_equal(acc, curr):
    if type(curr) is not list:
        return 0
    if acc == 0:
        return len(curr) 
    if acc != len(curr):
        return 0
    return len(curr)


class Matrix:
    def __init__(self, mat: list[list[int]]):
        self.mat = mat
        self.col_len = len(mat)
        self.row_len = reduce(check_if_all_rows_equal, mat, 0)

    def operation(self, other, cb):
        if self.col_len != self.row_len:
            raise ValueError("can not add matrix with different lenghts")
        result = [[0] * self.row_len for _ in range(self.col_len)]
        for i in range(self.col_len):
            for j in range(self.row_len):
                result[i][j] = cb(self.mat[i][j], other.mat[i][j])
        return result

    def __add__(self, other):
        result = self.operation(other, lambda a, b: a+b)
        return Matrix(result)

    def __sub__(self, other):
        result = self.operation(other, lambda a, b: a-b)
        return Matrix(result)

    def __mul__(self, other):
        result = self.operation(other, lambda a, b: a*b)
        return Matrix(result)

    def __floordiv__(self, other):
        result = self.operation(other, lambda a, b: a//b)
        return Matrix(result)

    def __truediv__(self, other):
        result = self.operation(other, lambda a, b: a/b)
        return Matrix(result)

if __name__ == "__main__":
    mat1 = Matrix([[1,2], [1,3]])
    mat2 = Matrix([[4,4], [4,6]])
    
    res  = mat1 + mat2 
    print(res.mat, mat1.mat, mat2.mat)
    res  = mat1 - mat2 
    print(res.mat, mat1.mat, mat2.mat)
    res  = mat1 * mat2 
    print(res.mat, mat1.mat, mat2.mat)
    res  = mat1 / mat2 
    print(res.mat, mat1.mat, mat2.mat)
    res  = mat1 // mat2 
    print(res.mat, mat1.mat, mat2.mat)
