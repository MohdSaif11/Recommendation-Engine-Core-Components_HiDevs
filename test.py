from similarity import SimilarityCalculator
from candidate_gen import CandidateGenerator
from scorer import RecommendationScorer
from evaluator import RecommendationEvaluator

# Data
user_data = {
    "u1": ["i1", "i2"],
    "u2": ["i2", "i3"],
    "u3": ["i3", "i4"]
}

item_data = {
    "i1": ["u1"],
    "i2": ["u1", "u2"],
    "i3": ["u2", "u3"],
    "i4": ["u3"]
}

# -------- Similarity --------
print("Cosine:", SimilarityCalculator.cosine_similarity([1,1], [1,1]))
print("Jaccard:", SimilarityCalculator.jaccard_similarity({1,2}, {2,3}))

# -------- Candidate Generation --------
cg = CandidateGenerator(user_data, item_data)
candidates = cg.hybrid_candidates("u1")
print("Candidates:", candidates)

# -------- Scoring --------
def relevance(user, item, context):
    return 1.0 if item in context["relevant"] else 0.0

def popularity(user, item, context):
    return len(context["item_data"].get(item, [])) / 3

scorer = RecommendationScorer()
scorer.add_scorer("relevance", relevance, 0.8)
scorer.add_scorer("popularity", popularity, 0.2)

context = {
    "relevant": ["i3", "i4"],
    "item_data": item_data
}

ranked = scorer.rank_candidates("u1", candidates, context, limit=5)
print("Ranked:", ranked)

# -------- Evaluation (FINAL FIX HERE) --------
evaluator = RecommendationEvaluator()

recommendations = {
    "u1": [item for item, _, _ in ranked]
}

ground_truth = {
    "u1": ["i3", "i4"]
}

k = len(recommendations["u1"])

metrics = evaluator.evaluate_all(recommendations, ground_truth, k=k)
print("Metrics:", metrics)
