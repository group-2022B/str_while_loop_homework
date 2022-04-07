def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    while s != "":
        if int(s[0]) % 2 != 0:
            count += 1
        s = s[1:]
    return count