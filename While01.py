def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    while s != "":
        if s[0].isdigit():
            count += 1
        s = s[1:]