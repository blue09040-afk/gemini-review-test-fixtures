def rank(entries):
    return sorted(entries, key=lambda item: (item[1], item[0]), reverse=True)
