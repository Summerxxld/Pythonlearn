def make_mutiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_mutiplier(3)