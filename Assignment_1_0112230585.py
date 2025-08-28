Array1 = [[[[[20, 32], [18, 13], [56, 89], [45, 69]]]]]
Array2 = [[[[[32, 9], [20, 12], [45, 8], [69, 14]]]]]

common_values = []

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

print("Common values:", common_values)
