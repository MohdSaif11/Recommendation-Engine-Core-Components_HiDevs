import math

class SimilarityCalculator:

    @staticmethod
    def cosine_similarity(vec1, vec2):
        if not vec1 or not vec2:
            return 0.0
        
        dot = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = math.sqrt(sum(a * a for a in vec1))
        norm2 = math.sqrt(sum(b * b for b in vec2))

        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot / (norm1 * norm2)

    @staticmethod
    def jaccard_similarity(set1, set2):
        if not set1 and not set2:
            return 1.0
        
        intersection = len(set1 & set2)
        union = len(set1 | set2)

        if union == 0:
            return 0.0
        
        return intersection / union

    @staticmethod
    def pearson_correlation(ratings1, ratings2):
        common = set(ratings1.keys()) & set(ratings2.keys())

        if not common:
            return 0.0
        
        n = len(common)

        sum1 = sum(ratings1[i] for i in common)
        sum2 = sum(ratings2[i] for i in common)

        sum1_sq = sum(ratings1[i]**2 for i in common)
        sum2_sq = sum(ratings2[i]**2 for i in common)

        product_sum = sum(ratings1[i] * ratings2[i] for i in common)

        num = product_sum - (sum1 * sum2 / n)
        den = math.sqrt((sum1_sq - sum1**2 / n) * (sum2_sq - sum2**2 / n))

        if den == 0:
            return 0.0
        
        return num / den