
def merge(arr, l, m, r):
    inversion_count = 0
    merged = []

    idx_l = l
    idx_r = m

    while idx_l < m and idx_r < r:
        if arr[idx_l] <= arr[idx_r]:
            merged.append(arr[idx_l])
            idx_l += 1
        else:
            merged.append(arr[idx_r])
            idx_r += 1

            inversion_count += m - idx_l

    while idx_l < m:
        merged.append(arr[idx_l])
        idx_l += 1

    while idx_r < r:
        merged.append(arr[idx_r])
        idx_r += 1

    for idx, val in enumerate(merged):
        arr[l + idx] = val

    return inversion_count

def merge_sort(arr, l, r):
    inversion_count = 0

    if l + 1 < r:
        m = (l + r) // 2

        inversion_count += merge_sort(arr, l, m)
        inversion_count += merge_sort(arr, m, r)
        inversion_count += merge(arr, l, m, r)

    return inversion_count


def solution(A):
    reversion_count = merge_sort(A, 0, len(A))

    if reversion_count > 1_000_000_000:
        return -1

    return reversion_count

