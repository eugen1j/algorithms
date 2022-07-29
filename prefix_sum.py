# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def prefix_count_letter(s: str, letter: str):
    count = 0
    prefix_count = [count]
    for ltr in s:
        if ltr == letter:
            count += 1
        prefix_count.append(count)
    return prefix_count


def solution(S, P, Q):
    # write your code in Python 3.6
    pass

    # A, C, G, T

    prefix_count_a = prefix_count_letter(S, 'A')
    prefix_count_c = prefix_count_letter(S, 'C')
    prefix_count_g = prefix_count_letter(S, 'G')
    prefix_count_t = prefix_count_letter(S, 'T')

    result = []

    for idx_from, idx_to in zip(P, Q):
        if prefix_count_a[idx_from] != prefix_count_a[idx_to + 1]:
            result.append(1)
        elif prefix_count_c[idx_from] != prefix_count_c[idx_to + 1]:
            result.append(2)
        elif prefix_count_g[idx_from] != prefix_count_g[idx_to + 1]:
            result.append(3)
        else:
            result.append(4)

    return result


