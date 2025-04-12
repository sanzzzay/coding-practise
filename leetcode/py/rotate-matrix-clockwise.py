class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        column = len(matrix[0])
        # print(row, column)
        extra_array = []
        total_count = row * column //4
        print(total_count)
        count = 0
        # faced two challenges 
        # 1. noting the pattern that four numbers will be swapped once
        # 2. getting the i and j iteration over matrix, since it was going into circles.
        # need to adjust the inner circle.
        for i in range(row//2):
            for j in range(i, column - i -1):
                temp1 = matrix[j][column-1-i]
                temp2 = matrix[row-1-i][column-1-j]
                temp3 = matrix[row-1-j][i]
                temp4 = matrix[i][j]   

                matrix[j][column-1-i] = temp4
                matrix[row-1-i][column-1-j] = temp1
                matrix[row-1-j][i] = temp2
                matrix[i][j] = temp3
                count += 1
