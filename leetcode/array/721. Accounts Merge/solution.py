class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        l = len(accounts)
        groups_reps = [i for i in range(l)] # length of the accounts
        # tree, root node rep to leaf node rep

        def find(x):
            # find the root node rep of x
            if groups_reps[x] != groups_reps[groups_reps[x]]:
                groups_reps[x] = find(groups_reps[x])
            return groups_reps[x]
        
        def merge(x, y):
            x_rep, y_rep = find(x), find(y)
            if x_rep != y_rep:
                groups_reps[y_rep] = x_rep
            return x_rep
        
        email_group_ind = {}
        for ind, group in enumerate(accounts):
            for i, val in enumerate(group):
                if i == 0: continue
                if val not in email_group_ind:
                    email_group_ind[val] = ind
                else:
                    merge(email_group_ind[val], ind)
        
        group_rep_emails = collections.defaultdict(list)
        for email, group_ind in email_group_ind.items():
            group_rep_emails[find(group_ind)].append(email)
        
        res = []
        for group_rep, emails in group_rep_emails.items():
            emails.sort()
            tmp = [accounts[group_rep][0]]
            tmp += emails
            res.append(tmp)
        
        return res

        

