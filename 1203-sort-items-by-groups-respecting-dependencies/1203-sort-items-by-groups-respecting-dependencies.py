class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        idx_group = m
        for i, num in enumerate(group):
            if num == -1:
                group[i] = idx_group
                idx_group += 1
        
        def topo_sort(graph, incoming, nodes):

            dq = deque([ i for i in range(nodes) if not incoming[i] ])
            res = []
            while dq:
                parent = dq.popleft()
                res.append(parent)
                
                for child in graph[parent]:
                    incoming[child] -= 1

                    if not incoming[child]:
                        dq.append(child)
            return res if len(res) == len(graph) else []

        item_graph = [[] for _ in range(n)]
        incoming_item = [0] * n

        grup_graph = defaultdict(set)
        incoming_grup = defaultdict(int)
        # graph building for both group and item
        for child, lst in enumerate(beforeItems):
            for parent in lst:
                item_graph[parent].append(child)
                incoming_item[child] += 1

                if group[child] != group[parent] and group[child] not in grup_graph[group[parent]]:
                    grup_graph[group[parent]].add(group[child])
                    incoming_grup[group[child]] += 1

        srted_item = topo_sort(item_graph, incoming_item, n)
        if not srted_item:
            return []
        
        srted_grup = topo_sort(grup_graph, incoming_grup, idx_group)
        if not srted_grup:
            return []
        
        group_bucket = [[] for _ in range(len(srted_grup))]

        for item in srted_item:
            group_bucket[group[item]].append(item)
        ans = []
        for idx in srted_grup:
            ans.extend(group_bucket[idx])
        return ans
        
        
        

        


