def solve(lines):
    n = int(lines[0])
    count = 0
    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                if "3" in f"{h:02d} {m:02d} {s:02d}":
                    count += 1
    return count


assert solve("5") == 11475
