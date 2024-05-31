def union(*args) -> set:
    sets = [set(arg) for arg in args]
    if sets:
        return set.union(*sets)
    return set()
print(union(('S', 'A'), ('P', 'C'), ('G', 'H')))


def intersect(*args):
    sets = [set(arg) for arg in args]
    if sets:
        return set.intersection(*sets)
    return set()
print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S')))
