def mcd(a, b):
    (a, b)=(max(a, b), min(a, b))
    for num in range(a):
        if a%num in range(a) and b%num in range(b):
            return num
