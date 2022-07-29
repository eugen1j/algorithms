# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from bisect import bisect_right

def solution(A):
    # write your code in Python 3.6
    intersections = 0

    # Turn disks into segments
    segments = sorted([
        (center - radius, center + radius)
        for center, radius in enumerate(A)
    ])
    # Two segments intersect if and only if s1 <= e2 and s2 <= e1

    starts_2 = [s[0] for s in segments]

    for idx, segment_1 in enumerate(segments):
        # Here s1 <= e2 automatically because s1 <= s2 (due to ordering of segments) and s2 <= e2
        end_1 = segment_1[1]

        # So, let's count segments with s2 <= e1
        intersections_1 = bisect_right(starts_2, end_1)

        # remove all elements that have been counted on prev steps and the current element
        # Note: intersections_1 contains all prev elements and the current, because:
        # it contains all element with s2 <= e1;
        # so, it contains all element with s2 <= s1 (s1 <= e1);
        # so, it contains all element with s2 <= s1_prev (s1_prev <= s1).
        intersections_1 -= idx + 1

        intersections += intersections_1
        if intersections > 10_000_000:
            return -1
    return intersections

