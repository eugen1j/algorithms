def verify_value(A, block_limit, value):
    current_sum = 0
    block_number = 0
    for a in A:
        if a > value:
            return False

        if a + current_sum > value:
            block_number += 1
            current_sum = a
            if block_number >= block_limit:
                return False
        else:
            current_sum += a

    return True


def bin_search(A, block_limit, left, right):
    if right == left:
        return right

    mid = (left + right) // 2
    if verify_value(A, block_limit, mid):
        return bin_search(A, block_limit, left, mid)
    else:
        return bin_search(A, block_limit, mid + 1, right)


def solution(K, M, A):
    return bin_search(A, K, 0, sum(A))


print(solution(9, 5, [100000] * 100000))