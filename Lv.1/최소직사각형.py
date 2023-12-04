def solution(sizes):
    max_width = max_height = 0
    for size in sizes:
        width, height = size
        max_width = max(max_width, width, height)
        max_height = max(max_height, min(width, height))

    return max_width * max_height


print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))