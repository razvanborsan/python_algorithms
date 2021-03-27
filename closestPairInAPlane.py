import copy
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def brute_force(points):
    min_distance = float('inf')
    first = 0
    second = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = dist(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                first = i
                second = j
    return points[first], points[second]


def closest_split(x_sorted, y_sorted, delta):
    mid = len(x_sorted) // 2
    mid_point = x_sorted[mid]
    s_y = [point for point in y_sorted if mid_point.x - delta < point.x < mid_point.x + delta]
    best = delta
    best_pair = None
    for i in range(len(s_y)):
        for j in range(min(7, len(s_y) - i - 1)):
            if dist(y_sorted[i], y_sorted[i + j + 1]) < best:
                best = dist(y_sorted[i], y_sorted[i + j + 1])
                best_pair = (y_sorted[i], y_sorted[i + j + 1])
    return best_pair


def closest_points(p_array, q_array):
    if len(p_array) <= 3:
        return brute_force(p_array)

    mid = len(p_array) // 2

    left_x = p_array[:mid]
    right_x = p_array[mid:]
    left_y, right_y = [], []
    for elem in q_array:
        if elem.x < p_array[mid].x:
            left_y.append(elem)
        else:
            right_y.append(elem)

    left_pair = closest_points(left_x, left_y)
    right_pair = closest_points(right_x, right_y)

    right_dist = dist(right_pair[0], right_pair[1])
    left_dist = dist(left_pair[0], left_pair[1])

    delta = min(left_dist, right_dist)
    split_pair = closest_split(p_array, q_array, delta)

    if split_pair is not None:
        dist_split = dist(split_pair[0], split_pair[1])
        min_dist = min(dist_split, right_dist, left_dist)
    else:
        min_dist = delta

    if min_dist == right_dist:
        return right_pair
    if min_dist == left_dist:
        return left_pair
    return split_pair


def closest(p_array):
    x_sorted = copy.deepcopy(p_array)
    y_sorted = copy.deepcopy(p_array)

    x_sorted.sort(key=lambda point: point.x)
    x_sorted.sort(key=lambda point: point.y)

    points = closest_points(x_sorted, y_sorted)
    print(f'The closest poinst are ({points[0].x}, {points[0].y}), ({points[1].x}, {points[1].y}), '
          f'with the distance {dist(points[0], points[1])}')
