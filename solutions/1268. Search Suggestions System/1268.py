class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, prefix = [], ""
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix)
            res.append([p for p in products[i:i+3] if p.startswith(prefix)])
        return res
