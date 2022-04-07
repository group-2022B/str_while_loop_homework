def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    while s != "":
        count += int(s[0])
        s = s[1:]
    return count