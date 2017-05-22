
class BirthdayChocolate():

    def solve_problem(self, n, s, d, m):
        total = 0
        check = 0
        for ind, value in enumerate(s):
            if len(s) == 1:
                if s[0] == d:
                    return 1
                else:
                    return 0
            for x in range(1, m):
                try:
                    total = value + s[ind + x]
                except:
                    return check
            if total == d:
                check += 1
            total = 0
        return check

    def solve(self, n, s, d, m):
        total = 0
        check = s[0]
        count = 0
        for ind, value in enumerate(s):
            while len(s) - d > 0:
                for x in range(1, m):
                    total = check + s[ind + x]
                if total == m:
                    count += 1
            return check
