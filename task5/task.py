import json
import numpy as np

def task(rankings_str_1: str, rankings_str_2: str) -> str:
    rankings_1 = json.loads(rankings_str_1)
    rankings_2 = json.loads(rankings_str_2)

    matrix_a = generate_matrix(rankings_1)
    matrix_a_transposed = matrix_a.transpose()

    matrix_b = generate_matrix(rankings_2)
    matrix_b_transposed = matrix_b.transpose()

    multiplied_matrix_ab = np.multiply(matrix_a, matrix_b)
    multiplied_matrix_ab_transposed = np.multiply(matrix_a_transposed, matrix_b_transposed)

    conflicts = []

    for i in range(multiplied_matrix_ab.shape[0]):
        for j in range(multiplied_matrix_ab[i].shape[1]):
            if int(multiplied_matrix_ab[i, j]) == 0 and int(multiplied_matrix_ab_transposed[i, j]) == 0:
                if (str(j + 1), str(i + 1)) not in conflicts:
                    conflicts.append((str(i + 1), str(j + 1)))

    return json.dumps(conflicts)


def generate_matrix(rank_):
    ranks = dict()
    rank_length = calculate_length(rank_)
    for i, rank in enumerate(rank_):
        if type(rank) is str:
            ranks[int(rank)] = i
        else:
            for r in rank:
                ranks[int(r)] = i

    return np.matrix([[1 if ranks[i + 1] <= ranks[j + 1] else 0 for j in range(rank_length)] for i in range(rank_length)])


def calculate_length(rank_):
    length = 0
    for i in rank_:
        if type(i) is str:
            length += 1
        else:
            length += len(i)
    return length
