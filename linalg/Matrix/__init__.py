import copy


class Matrix:
    """

    Matrix

    """

    def __init__(self, row, column, fill=0.0):
        self.shape = (row, column)
        self.row = row
        self.column = column
        self._matrix = [[fill] * column for i in range(row)]

    def __getitem__(self, index):
        if isinstance(index, int):
            return self._matrix[index - 1]
        elif isinstance(index, tuple):
            return self._matrix[index[0] - 1][index[1] - 1]

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self._matrix[index - 1] = copy.deepcopy(value)
        elif isinstance(index, tuple):
            self._matrix[index[0] - 1][index[1] - 1] = value

    def __eq__(self, N):
        # A == B
        assert isinstance(N, Matrix), "Not in Same Dimension"
        return N.shape == self.shape

    def __add__(self, N):
        # A + B
        assert N.shape == self.shape, "Not in Same Dimension"
        M = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                M[r, c] = self[r, c] + N[r, c]
        return M

    def __sub__(self, N):
        # A - B
        assert N.shape == self.shape, "Not in Same Dimension"
        M = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                M[r, c] = self[r, c] - N[r, c]
        return M

    def __mul__(self, N):
        # A * B or A * constant
        if isinstance(N, int) or isinstance(N, float):
            M = Matrix(self.row, self.column)
            for r in range(self.row):
                for c in range(self.column):
                    M[r, c] = self[r, c] * N
        else:
            assert N.row == self.column, "Not in Same Dimension"
            M = Matrix(self.row, N.column)
            for r in range(self.row):
                for c in range(N.column):
                    sum = 0
                    for k in range(self.column):
                        sum += self[r, k] * N[k, r]
                    M[r, c] = sum
        return M

    def __div__(self, N):
        # A / B
        pass

    def __pow__(self, k):
        # A**k
        assert self.row == self.column, "Not Square Matrix"
        M = copy.deepcopy(self)
        for i in range(k):
            M = M * self
        return M

    def invert(self):
        """inverse matrix"""
        assert self.row == self.column, "Not Square Matrix"
        M = Matrix(self.row, self.column * 2)
        I = self.identity()  # Unit Matrix
        I.show()  #############################

        # augment
        for r in range(1, M.row + 1):
            temp = self[r]
            temp.extend(I[r])
            M[r] = copy.deepcopy(temp)
        M.show()  #############################

        # row exchange
        for r in range(1, M.row + 1):

            if M[r, r] == 0:
                for rr in range(r + 1, M.row + 1):
                    if M[rr, r] != 0:
                        M[r], M[rr] = M[rr], M[r]  # switch two lines
                    break

            assert M[r, r] != 0, 'Matrix not invertible'

            temp = M[r, r]  # Cache
            for c in range(r, M.column + 1):
                M[r, c] /= temp
                print("M[{0}, {1}] /=  {2}".format(r, c, temp))
            M.show()

            for rr in range(1, M.row + 1):
                temp = M[rr, r]  # Cache
                for c in range(r, M.column + 1):
                    if rr == r:
                        continue
                    M[rr, c] -= temp * M[r, c]
                    print("M[{0}, {1}] -= {2} * M[{3}, {1}]".format(rr, c, temp, r))
                M.show()

        # inverse matrix
        N = Matrix(self.row, self.column)
        for r in range(1, self.row + 1):
            N[r] = M[r][self.row:]
        return N

    def transpose(self):
        '''Transpose'''
        M = Matrix(self.column, self.row)
        for r in range(self.column):
            for c in range(self.row):
                M[r, c] = self[c, r]
        return M

    def cofactor(self, row, column):
        '''Algebraic cofactor'''
        assert self.row == self.column, "Not Square Matrix"
        assert self.row >= 3, "At Least 3*3 Matrix"
        assert row <= self.row and column <= self.column, "Out of Range"
        M = Matrix(self.column - 1, self.row - 1)
        for r in range(self.row):
            if r == row:
                continue
            for c in range(self.column):
                if c == column:
                    continue
                rr = r - 1 if r > row else r
                cc = c - 1 if c > column else c
                M[rr, cc] = self[r, c]
        return M

    def det(self):
        '''Determinant'''
        assert self.row == self.column, "Not Determinant"
        if self.shape == (2, 2):
            return self[1, 1] * self[2, 2] - self[1, 2] * self[2, 1]
        else:
            sum = 0.0
            for c in range(self.column + 1):
                sum += (-1) ** (c + 1) * self[1, c] * self.cofactor(1, c).det()
            return sum

    def zeros(self):
        '''Zero Matrix'''
        M = Matrix(self.column, self.row, fill=0.0)
        return M

    def ones(self):
        '''1 Matrix'''
        M = Matrix(self.column, self.row, fill=1.0)
        return M

    def identity(self):
        '''Unit Matrix'''
        assert self.row == self.column, "Not NxN Matrix"
        M = Matrix(self.column, self.row)
        for r in range(self.row):
            for c in range(self.column):
                M[r, c] = 1.0 if r == c else 0.0
        return M

    def show(self):
        '''Print Matrix'''
        for r in range(self.row):
            for c in range(self.column):
                print(self[r + 1, c + 1], end=' ')
            print()
