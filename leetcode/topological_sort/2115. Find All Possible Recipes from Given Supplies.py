class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # {sandwich: {bread, meat}, 'bread': {yeast, flour}, burger: {sandwich, meat, bread}}
        # set({yeast, flour, bread})
        # yeast->
        #           bread   ->  sandwich
        # flour->      meat ->
        graph = collections.defaultdict(list)
        indgree = collections.defaultdict(int)
        for ingre in supplies:
            indgree[ingre] = 0
        n = len(recipes)
        for i in range(n):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
            indgree[recipes[i]] += len(ingredients[i])
        
        supplies_set = set(supplies)
        recipes_set = set(recipes)

        q = collections.deque([])
        for k, v in indgree.items():
            if v == 0 and k in supplies_set:
                q.append(k)
        
        res = []
        while q:
            for _ in range(len(q)):
                tmpval = q.popleft()
                if tmpval in recipes_set:
                    res.append(tmpval)
                for nex in graph[tmpval]:
                    indgree[nex] -= 1
                    if indgree[nex] == 0:
                        q.append(nex)

        return res    

