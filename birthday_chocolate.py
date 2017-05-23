
class BirthdayChocolate():

    def solve(self, n, s, d, m):
        total = 0
        count = 0
        for ind, value in enumerate(s):
            total = sum(s[ind: ind + m])
            if total == d:
                count += 1
        return count
