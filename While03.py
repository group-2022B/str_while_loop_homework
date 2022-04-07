def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    while s != "":
        if s[0].isalpha() == False and s[0].isdigit() == False:
            count += 1
        s = s[1:]
    return count