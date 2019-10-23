def lucas_lehmer(p):
    """
    Returns a list of Lucas-Lehmer series values up to when
    Mersenne = M^p.
    """

    ll = []
    ll.append(4)
    i = 1
    mers = 2**p - 1
    for i in range(1, p-1):
        llvl = (ll[i-1]**2 - 2) % mers
        ll.append(llvl)
    return ll

# print(lucas_lehmer(5))
