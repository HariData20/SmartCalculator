

def startswith_capital_counter(names):
    return sum(1 if name.istitle() else 0 for name in names)
