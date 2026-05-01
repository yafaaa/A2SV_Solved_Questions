from collections import deque, defaultdict
class Solution:
    def findOrder(self, words):
        n = len(words)
        graph = defaultdict(list)
        incoming = defaultdict(int)
        node_set = set([ch for word in words for ch in word])
        
        def fun(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                
                if word1[i] != word2[i]:
                    graph[word1[i]].append(word2[i])
                    incoming[word2[i]] += 1
                    return                 
                
                i += 1
            if i == len(word2) and i < len(word1):
                return True
            
            
        for i in range(n-1):
            if fun(words[i], words[i+1]):
                return ""
        dq = deque([ch for ch in node_set if not incoming[ch]])
        ans = []
        while dq:
            node = dq.popleft()
            ans.append(node)
            
            for child in graph[node]:
                incoming[child] -= 1
                
                if not incoming[child]:
                    dq.append(child)
        
        return "".join(ans) if len(ans) == len(node_set) else ""
                
            
            
            
        
            
