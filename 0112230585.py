# Comparison between two 5D arrays' elements  for common data

Arrary1 = [[[[[8, 9], [3, 4]], [[9, 10], [2, 14]]]]]
Arrary2 = [[[[[18, 9], [3, 12]], [[9, 8], [9, 14]]]]]
common_values = []
for i in range(len(Arrary1)):
    for j in range(len(Arrary1[i])):
        for k in range(len(Arrary1[i][j])):
            for l in range(len(Arrary1[i][j][k])):
                for m in range(len(Arrary1[i][j][k][l])):
                    if Arrary1[i][j][k][l][m] == Arrary2[i][j][k][l][m]:
                        common_values.append(Arrary1[i][j][k][l][m])
print("Common values:", common_values)
