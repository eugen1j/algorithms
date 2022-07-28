import math


class Point:
    def __init__(self, x, y, index=0):
        self.x = x
        self.y = y
        self.index = index

    def __repr__(self):
        return f"({self.x}, {self.y})"


def angle(p1: Point, p2: Point):
    x = p2.x - p1.x
    y = p2.y - p1.y
    return math.atan2(y, x)


def is_cw(p1: Point, p2: Point, p3: Point):
    return (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y) > 0


def solution(A):
    points = [Point(a[0], a[1], idx) for idx, a in enumerate(A)]

    starting_point = min(points, key=lambda p: (p.y, p.x))

    points.remove(starting_point)
    sorted_points = sorted(points, key=lambda p: angle(starting_point, p))
    points_stack = [starting_point]

    for point in sorted_points:
        if len(points_stack) > 1 and is_cw(points_stack[-2], points_stack[-1], point):
            return points_stack[-1].index
        points_stack.append(point)

    return -1


print(solution([[-1, 3], [1, 2], [3, 1], [0, -1], [-2, 1]]))
