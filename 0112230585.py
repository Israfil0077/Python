arr1 = [[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]]]
arr2 = [[[[[1, 9], [3, 0]], [[5, 6], [0, 8]]]]]
common_values = []
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        for k in range(len(arr1[i][j])):
            for l in range(len(arr1[i][j][k])):
                for m in range(len(arr1[i][j][k][l])):
                    if arr1[i][j][k][l][m] == arr2[i][j][k][l][m]:
                        common_values.append(arr1[i][j][k][l][m])
print("Common values:", common_values)
