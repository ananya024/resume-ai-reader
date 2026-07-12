# similarity_service.py

from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarities(em1, em2):
    similarities = cosine_similarity(em1,em2)
    return similarities