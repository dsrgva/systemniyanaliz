import json
import numpy as np


def task(*reviews):
    num_experts = len(reviews)
    review_template = {}
    num_reviews = 0

    for review in json.loads(reviews[0]):
        if isinstance(review, list):
            for item in review:
                review_template[item] = num_reviews
                num_reviews += 1
        else:
            review_template[review] = num_reviews
            num_reviews += 1

    matrix = [convert_reviews_to_list(review, review_template) for review in reviews]

    matrix_sum = np.sum(matrix, axis=0)

    variance = np.var(matrix_sum) * num_reviews / (num_reviews - 1)
    max_variance = (num_experts ** 2) * ((num_reviews ** 3 - num_reviews) / 12 / (num_reviews - 1))

    return format(variance / max_variance, ".2f")

def convert_reviews_to_list(reviews_json, template):
    reviews = json.loads(reviews_json)
    reviews_list = [0 for _ in range(len(template))]

    for i, review in enumerate(reviews):
        if isinstance(review, list):
            for item in review:
                reviews_list[template[item]] = i + 1
        else:
            reviews_list[template[review]] = i + 1

    return reviews_list
