class T(object):
    x = 0
    l = None
    r = None


def dfs(T, depth=1):
    if T.l:
        depth_left = dfs(T.l, depth + 1)
    else:
        depth_left = depth

    if T.r:
        depth_right = dfs(T.r, depth + 1)
    else:
        depth_right = depth

    return max(depth_right, depth_left)


def solution(T):
    return dfs(T)
