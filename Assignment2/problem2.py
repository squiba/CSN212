'''
https://community.topcoder.com/stat?c=problem_statement&pm=1889
'''

def banned_roads(banned_strings):
    banned_paths = {}
    for banned_string in banned_strings:
        banned_coords = [int(item) for item in banned_string.split()]
        banned_coords = [tuple(banned_coords[:2]), tuple(banned_coords[2:])]
        banned_coords.sort()  # we always move towards larger coords
        src, dst = banned_coords
        banned_srcs = banned_paths.setdefault(dst, [])
        banned_srcs.append(src)
    return banned_paths

def avoid_roads(rows, cols, banned_paths):
    rows += 1
    cols += 1
    prev_row = [1] + [0] * (cols - 1)
    for row in range(rows):
        this_row = []
        before = 0
        for col, above in enumerate(prev_row):
            banned_srcs = banned_paths.get((row, col), [])
            if (row, col - 1) in banned_srcs:
                before = 0
            if (row - 1, col) not in banned_srcs:
                before += above
            this_row.append(before)
        prev_row = this_row
    return prev_row[-1]


print avoid_roads(6, 6, banned_roads(['0 0 0 1', '6 6 5 6']))
print avoid_roads(1, 1, {})
print avoid_roads(35, 31, {})
