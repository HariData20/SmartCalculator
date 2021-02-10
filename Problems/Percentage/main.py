from math import floor, ceil


def get_percentage(number, ndigits=None):
    return f'The output is "{round(number * 100, ndigits)}%"'
    """
    if ndigits is None:
        if abs(number - 1) < 0.5:
            return str(int(floor(number))) + '%'
        else:
            return str(int(ceil(number))) + '%'
    elif ndigits == 0:
        if abs(number - 1) < 0.5:
            return str(float(floor(number))) + '%'
        else:
            return str(float(ceil(number))) + '%'
    else:
        number = round(number, ndigits)
        if abs(number - 1) < 0.5:
            return str(number) + '%'
        else:
"""



