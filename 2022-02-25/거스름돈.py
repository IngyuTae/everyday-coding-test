def solve(change, coins, count=0, result=0):
    if change == 0:
        return result
    return solve(
        change % coins[count], coins, count + 1, result + int(change / coins[count])
    )


assert solve(1260, [500, 100, 50, 10]) == 6
