class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        group_no = [i for i in range(n)]
        group_count = n
        logs.sort(key=lambda x: x[0])

        def find_group(person):
            nonlocal group_no
            p = person
            while group_no[p] != p:
                p = group_no[group_no[p]]
            return p

        def union(person1, person2):
            nonlocal group_count, group_no
            group1, group2 = find_group(person1), find_group(person2)
            if group1 == group2:
                return
            group_no[group2] = group1
            group_count -= 1
        
        for timestamp, person1, person2 in logs:
            union(person1, person2)
            if group_count == 1:
                return timestamp
        
        return -1
        
        
