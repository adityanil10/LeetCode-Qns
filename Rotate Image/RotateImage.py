class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix[0]) #The transpose of a matrix is the mirror image of the matrix we get after a 90 degree clockwise rotation
        for i in range(n): #transpose the matrix
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            
        for i in range(n): #reverse the matrix by row
            for j in range(int(n/2)):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]
