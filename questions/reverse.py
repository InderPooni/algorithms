def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if 0 <= x <= 9:
        return x

    negative = x < 10

    s = str(x)

    if negative:
        s = s[1:]

    if s[-1] == "0":
        s = s[:-1]
    
    s = s[::-1]

    print(s)

    res = int(s)

    if negative:
        res *= -1

    if -1 * (2**31) <= res <= (2**31) - 1:
        return res

    else:
        return 0

print(reverse(1))