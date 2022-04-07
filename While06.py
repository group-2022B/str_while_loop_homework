def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    count = 0
    while s != "":
        if s[0].isalpha() and s[0].lower() not in "aeiou":
            count += 1
        s = s[1:]
    return count