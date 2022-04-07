def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    while s != "":
        if int(s[0]) % 2 != 0:
            count += int(s[0])
        s = s[1:]
    return count