class RecommendationScorer:

    def __init__(self):
        self.scorers = []

    def add_scorer(self, name, function, weight):
        self.scorers.append((name, function, weight))

    def calculate_score(self, user_id, item_id, context):
        total = 0
        total_weight = 0
        explanation = {}

        for name, func, weight in self.scorers:
            score = max(0, min(1, func(user_id, item_id, context)))  # clamp 0–1
            explanation[name] = score

            total += score * weight
            total_weight += weight

        final = total / total_weight if total_weight else 0
        return final, explanation

    def rank_candidates(self, user_id, candidates, context, limit=10):
        scored = []

        for item in candidates:
            score, explanation = self.calculate_score(user_id, item, context)
            scored.append((item, score, explanation))

        scored.sort(key=lambda x: x[1], reverse=True)

        return scored[:limit]