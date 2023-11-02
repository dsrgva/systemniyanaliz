import math
import numpy

def calculate_entropy_a(probabilities):
    entropy = 0
    for row in probabilities:
        for probability in row:
            if probability != 0:
                entropy -= probability * math.log2(probability)
    return entropy


def calculate_entropy_b(matrix, n):
    transposed_matrix = numpy.transpose(matrix)
    normalized_probabilities = []
    entropy = 0

    for row in transposed_matrix:
        normalized_row = [x / (n * n) for x in row]
        normalized_probabilities.append(normalized_row)

    for row in normalized_probabilities:
        if sum(row) != 0:
            entropy -= sum(row) * math.log2(sum(row))

    return entropy

def task():
    n = 6
    mat, pr, pr1, h_norm = [], [], [], []
    for j in range(n * 2 + 1):
        row = []
        for i in range(n * n + 1):
            row.append(0)
        mat.append(row)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            mat[i + j][i * j] += 1

    pr = []
    for row in mat:
        normalized_row = []
        for x in row:
            normalized_row.append(x / (n * n))
        pr.append(normalized_row)

    H_AB = calculate_entropy_a(pr)

    pr1 = []
    for row in mat:
        normalized_row = []
        for mij in row:
            if sum(row) == 0:
                normalized_row.append(0)
            else:
                normalized_row.append(mij / sum(row))
        pr1.append(normalized_row)

    h_norm = []
    for row in pr1:
        h_row = []
        for pij in row:
            if pij == 0:
                h_row.append(0)
            else:
                h_row.append(-pij * math.log2(pij))
        h_norm.append(h_row)

    HaB = 0.0
    for i in range(len(pr1)):
        HaB += sum(h_norm[i]) * sum(pr[i])

    Ha = H_AB - HaB
    Hb = calculate_entropy_b(mat, n)

    I_ab = Hb - HaB
    return [round(x, 2) for x in [H_AB, Ha, Hb, HaB,  I_ab]]
                                            

print(task())
