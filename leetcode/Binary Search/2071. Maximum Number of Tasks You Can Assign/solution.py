class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # return the maximum number of tasks that can be completed.
        # <=> use the most strength workers on the tasks that require the least strength
        # <=> check() to check whether we can complete the number of tasks
        # <=> binary search on the number of tasks that can be complete
        # check(mid)  mid - number of tasks that can be complete
        # iterate the tasks from mid - 1 to 0:
        #     add the most strength workers that + strength >= tasks[i] to a deque([])
        #     if q[-1] >= tasks[i]:
        #         q.pop() # assign the worker to the tasks[i]
        #     else:
        #         pills -= 1 # use the pills worker + strength >= tasks[i]
        #         q.popleft() 
        tasks_num, worker_num = len(tasks), len(workers)
        res = 0
        tasks.sort(), workers.sort()

        def check(mid):
            # mid number of tasks that are assigned to the mid number of workers
            worker_ind = worker_num - 1
            que = deque([]) # to save the workers
            p = pills
            for i in range(mid - 1, -1, -1):
                while worker_ind >= worker_num - mid and workers[worker_ind] + strength >= tasks[i]:
                    que.appendleft(workers[worker_ind]) # the most strength worker is at the last of the que
                    worker_ind -= 1
                if not que:
                    return False
                if que[-1] >= tasks[i]:
                    que.pop() # assign the most strength worker to the tasks[i]
                else:
                    if p <= 0:
                        return False
                    if que[0] + strength < tasks[i]:
                        return False
                    que.popleft()
                    p -= 1
            return True

        l, r = 0, min(tasks_num, worker_num)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if check(mid):
                res = max(res, mid)
                l = mid
            else:
                r = mid
        if check(r):
            return r
        if check(l):
            return l
        return 0
