def solve(m, k, data, count=0, result=0):
    if result == 0:
        data.sort()
    [*_, second, first] = data
    if m == 0:
        return result
    if count >= k:
        return solve(m - 1, k, data, 0, result + second)
    return solve(m - 1, k, data, count + 1, result + first)


def solve2(m, k, data):
    [*_, second, first] = sorted(data)
    count = int(m / (k + 1)) * k + m % (k + 1)
    return count * first + (m - count) * second


def main(solve, *lines):
    import time

    start_time = time.process_time()
    n, m, k = [int(i) for i in lines[0].split()]
    data = [int(v) for i, v in enumerate(lines[1].split()) if i < n]
    end_time = time.process_time()
    print(f"{solve.__name__}() takes {(end_time - start_time) * 1000}ms")
    return solve(m, k, data)


assert main(solve, "5 8 3", "2 4 5 4 6") == 46

assert main(solve2, "5 8 3", "2 4 5 4 6") == 46
