def solve(*lines):
    n, k = [int(i) for i in lines[0].split()]
    count = 0
    while n > 1:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        count += 1
    return count


assert solve("25 5") == 2
