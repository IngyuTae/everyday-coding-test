def solve(*lines):
    n, m = [int(i) for i in lines[0].split()]
    n_lists = [list(map(int, i.split()[:m])) for i in lines[1 : n + 1]]
    result = max([min(n_list) for n_list in n_lists])
    return result


assert solve("3 3", "3 1 2", "4 1 4", "2 2 2") == 2
