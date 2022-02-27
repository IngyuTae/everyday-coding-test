STEP_TO_OFFSET = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D": [1, 0]}


def solve(*lines):
    n = int(lines[0])
    steps = lines[1].split()
    x, y = 1, 1
    for step in steps:
        offset_x, offset_y = STEP_TO_OFFSET[step]
        if not (0 < x + offset_x < n and 0 < y + offset_y < n):
            continue
        x += offset_x
        y += offset_y
    return f"{x} {y}"


assert solve("5", "R R R U D D") == "3 4"
