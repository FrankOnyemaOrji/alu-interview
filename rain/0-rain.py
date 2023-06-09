#!/usr/bin/python3
"""Create an algorithm for claculating the
amount of rain trapped in a 2D array"""


def rain(walls):
    """Calculate how much water will be retained after it rains"""
    if not walls or len(walls) < 3:
        return 0
    water = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])
        water = water + (min(left, right) - walls[i])
    return water
