import math

class RecommendationEvaluator:

    @staticmethod
    def precision_at_k(recommendations, relevant_items, k):
        if not recommendations:
            return 0.0
        
        recommended_k = recommendations[:k]
        relevant = set(relevant_items)

        hits = sum(1 for item in recommended_k if item in relevant)
        return hits / k

    @staticmethod
    def recall_at_k(recommendations, relevant_items, k):
        if not relevant_items:
            return 0.0
        
        recommended_k = recommendations[:k]
        relevant = set(relevant_items)

        hits = sum(1 for item in recommended_k if item in relevant)
        return hits / len(relevant)

    @staticmethod
    def ndcg_at_k(recommendations, relevant_items, k):
        dcg = 0
        for i, item in enumerate(recommendations[:k]):
            if item in relevant_items:
                dcg += 1 / math.log2(i + 2)

        ideal_dcg = sum(1 / math.log2(i + 2) for i in range(min(len(relevant_items), k)))

        return dcg / ideal_dcg if ideal_dcg > 0 else 0

    def evaluate_all(self, recommendations_dict, ground_truth_dict, k=5):
        precision_list = []
        recall_list = []
        ndcg_list = []

        for user, recs in recommendations_dict.items():
            if user not in ground_truth_dict:
                continue

            relevant = ground_truth_dict[user]

            precision_list.append(self.precision_at_k(recs, relevant, k))
            recall_list.append(self.recall_at_k(recs, relevant, k))
            ndcg_list.append(self.ndcg_at_k(recs, relevant, k))

        return {
            "precision": sum(precision_list) / len(precision_list) if precision_list else 0,
            "recall": sum(recall_list) / len(recall_list) if recall_list else 0,
            "ndcg": sum(ndcg_list) / len(ndcg_list) if ndcg_list else 0
        }
        