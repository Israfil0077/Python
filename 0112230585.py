# Declare 5D arrays
Array1 = [[[[[2, 3], [18, 12], [9, 10], [2, 14]]]]]
Array2 = [[[[[18, 9], [3, 12], [6, 8], [9, 14]]]]]


# Store common elements
common_values = []

# Compare each element in both arrays
for i in range(len(Array1)):
    for j in range(len(Array1[i])):
        for k in range(len(Array1[i][j])):
            for l in range(len(Array1[i][j][k])):
                for m in range(len(Array1[i][j][k][l])):
                    val1 = Array1[i][j][k][l][m]
                    for i2 in range(len(Array2)):
                        for j2 in range(len(Array2[i2])):
                            for k2 in range(len(Array2[i2][j2])):
                                for l2 in range(len(Array2[i2][j2][k2])):
                                    for m2 in range(len(Array2[i2][j2][k2][l2])):
                                        val2 = Array2[i2][j2][k2][l2][m2]
                                        if val1 == val2 and val1 not in common_values:
                                            common_values.append(val1)

# Print common elements
print("Common values:", common_values)
