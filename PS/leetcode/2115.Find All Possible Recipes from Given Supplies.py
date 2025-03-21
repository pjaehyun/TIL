class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        rec = {r: ing for r, ing in zip(recipes, ingredients)}
        sup, memo, visited = set(supplies), {}, set()

        def dfs(s):
            if s not in rec: return True
            if s in memo: return memo[s]
            if s in visited: return False
            visited.add(s)
            memo[s] = all(dfs(p) if p in rec else p in sup for p in rec[s])
            visited.remove(s)
            return memo[s]

        return [r for r in recipes if dfs(r)]