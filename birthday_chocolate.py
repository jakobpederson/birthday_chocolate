
class BirthdayChocolate():

    def solve(self, n, s, d, m):
        if self.check_constraints(n, s, d, m):
            total = 0
            count = 0
            for ind, value in enumerate(s):
                total = sum(s[ind: ind + m])
                if total == d:
                    count += 1
            return count
        return 'Error: Input outside of established constraints'

    def check_constraints(self, n, s, d, m):
        for value in s:
            if value < 1 or value > 5:
                return False
        if n < 1 or n > 100:
            return False
        if d < 1 or d > 31:
            return False
        if m < 1 or m > 12:
            return False
        return True
