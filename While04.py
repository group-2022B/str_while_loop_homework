from string import ascii_uppercase
def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    while s != "":
        if s[0] in ascii_uppercase:
            count += 1
        s = s[1:]
    return count