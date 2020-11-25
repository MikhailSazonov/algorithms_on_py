import copy


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class GaussError(Exception):
    def __init__(self, matrix):
        self.matrix = matrix


class Matrix:
    def __init__(self, mat):
        self.mat = copy.deepcopy(mat)

    def __str__(self):
        return "\n".join("\t".join(str(x) for x in r) for r in self.mat)

    def size(self):
        return len(self.mat), len(self.mat[0])

    def __add__(self, plus):
        if len(self.mat) == len(plus.mat) and len(self.mat[0]) == len(
                plus.mat[0]):
            rot = []
            for i in range(len(self.mat)):
                rot.append([])
                for j in range(len(self.mat[i])):
                    rot[i].append(self.mat[i][j] + plus.mat[i][j])
            return Matrix(rot)
        else:
            matrix1 = Matrix(self.mat)
            matrix2 = Matrix(plus.mat)
            raise MatrixError(matrix1, matrix2)

    def __mul__(self, multiply):
        if type(multiply) == int or type(multiply) == float:
            rot = []
            for i in range(len(self.mat)):
                rot.append([])
                for j in range(len(self.mat[i])):
                    rot[i].append(self.mat[i][j] * multiply)
            return Matrix(rot)
        if type(multiply.mat) == list and \
                len(self.mat[0]) == len(multiply.mat):
            rot = []
            for i in range(len(self.mat)):
                rot.append([])
                for j in range(len(multiply.mat[0])):
                    rot[i].append(0)
                    for k in range(len(self.mat[0])):
                        rot[i][j] += self.mat[i][k] * multiply.mat[k][j]
            return Matrix(rot)
        else:
            matrix1 = Matrix(self.mat)
            matrix2 = Matrix(multiply.mat)
            raise MatrixError(matrix1, matrix2)

    def __rmul__(self, multiply):
        rot = []
        for i in range(len(self.mat)):
            rot.append([])
            for j in range(len(self.mat[i])):
                rot[i].append(self.mat[i][j] * multiply)
        return Matrix(rot)

    def transpose(self):
        rot = [[0 for j in range(len(self.mat))] for i in
               range(len(self.mat[0]))]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                rot[j][i] = self.mat[i][j]
        self.mat = rot
        return Matrix(self.mat)

    @staticmethod
    def transposed(self):
        rot = [[0 for j in range(len(self.mat))] for i in
               range(len(self.mat[0]))]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                rot[j][i] = self.mat[i][j]
        return Matrix(rot)

    def solve(self, args):
        t = 0
        p = len(args)
        bb = copy.deepcopy(self.mat)
        if len(args) != len(bb):
            raise GaussError(Matrix(self.mat))
        while t < len(bb) and t < len(bb[0]):
            for i in range(t, len(bb)):
                for j in range(i + 1, len(bb)):
                    if bb[j][t] != 0:
                        mult_i = bb[j][t] // gcd(
                            bb[i][t], bb[j][t])
                        mult_j = bb[i][t] // gcd(
                            bb[i][t], bb[j][t])
                        for k in range(len(bb[0])):
                            bb[j][k] *= mult_j
                            bb[j][k] -= bb[i][k] * mult_i
                        args[j] *= mult_j
                        args[j] -= args[i] * mult_i
                t += 1
        t -= 1
        while bb[t][-1] == 0:
            for z in range(t, len(args)):
                if args[z] != 0:
                    matrix = Matrix(self.mat)
                    raise GaussError(matrix)
                else:
                    t -= 1
                    p -= 1
        if t < len(bb[0]) - 1:
            matrix = Matrix(self.mat)
            raise GaussError(matrix)
        while t > 0:
            for i in range(t, -1, -1):
                for j in range(i - 1, -1, -1):
                    if bb[j][t] != 0:
                        mult_i = bb[j][t] // gcd(
                            bb[i][t], bb[j][t])
                        mult_j = bb[i][t] // gcd(
                            bb[i][t], bb[j][t])
                        for f in range(len(bb[0])):
                            bb[j][f] *= mult_j
                        bb[j][t] = 0
                        args[j] *= mult_j
                        args[j] -= args[i] * mult_i
                t -= 1
        ans = []
        for s in range(p):
            ans.append(args[s] / bb[s][s])
        return ans


class SquareMatrix(Matrix):
    def __pow__(self, elevate):
        if elevate == 0:
            ans = []
            for i in range(len(self.mat)):
                ans.append([])
                for j in range(len(self.mat[0])):
                    if i == j:
                        ans[i].append(1)
                    else:
                        ans[i].append(0)
            return Matrix(ans)
        if elevate == 1:
            return SquareMatrix(self.mat)
        if elevate % 2 == 0:
            result = pow(SquareMatrix(self.mat), elevate // 2)
            return result * result
        return pow(SquareMatrix(self.mat), elevate - 1) * \
            SquareMatrix(self.mat)


print()
