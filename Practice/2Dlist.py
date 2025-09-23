matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
for i in range(len(matrix)):
    print(matrix[i][i])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]==5:
            print("found at:", i,j)