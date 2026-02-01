import numpy as np

def dynamic_retrieve(similarities):

    max_score = np.max(similarities)

    if max_score < 0.1:
        return []

    if max_score > 0.5:
        threshold = max_score * 0.8
    else:
        threshold = max_score * 0.6

    indices = [
        i for i, score in enumerate(similarities)
        if score >= threshold
    ]

    return indices
