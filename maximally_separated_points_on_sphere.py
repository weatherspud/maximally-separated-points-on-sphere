#!/usr/bin/env python3
from math import sqrt, sin, cos, pi
import random
import sys
from typing import Any, List


class PointOnUnitSphere:
    def __init__(self, theta: float, phi: float) -> None:
        self.theta = theta
        self.phi = phi

    def x(self) -> float:
        return sin(self.phi) * sin(self.theta)

    def y(self) -> float:
        return sin(self.phi) * cos(self.theta)

    def z(self) -> float:
        return cos(self.phi)

    def distance(self, other: Any) -> float:
        return sqrt((self.x() - other.x()) ** 2 +
                    (self.y() - other.y()) ** 2 +
                    (self.z() - other.z()) ** 2)

    def derivative_theta(self, other: Any) -> float:
        # pylint: disable=bad-continuation
        return ((-2 * (-cos(other.theta) * sin(other.phi) +
                 cos(self.theta) * sin(self.phi)) * sin(self.phi) * sin(self.theta) +
                 2 * cos(self.theta) * (-sin(other.phi) * sin(other.theta) +
                 sin(self.phi) * sin(self.theta)) * sin(self.phi)) /
                (2 * sqrt((cos(self.phi) -
                          cos(other.phi)) ** 2 +
                          (-cos(other.theta) * sin(other.phi) +
                          cos(self.theta) * sin(self.phi)) ** 2 +
                          (-sin(other.phi) * sin(other.theta) +
                          sin(self.phi) * sin(self.theta)) ** 2)))

    def derivative_phi(self, other: Any) -> float:
        # pylint: disable=bad-continuation
        return ((-2 * (cos(self.phi) -
                 cos(other.phi)) * sin(self.phi) +
                 2 * cos(self.phi) * cos(self.theta) * (-cos(other.theta) * sin(other.phi) +
                 cos(self.theta) * sin(self.phi)) +
                 2 * cos(self.phi) * (-sin(other.phi) * sin(other.theta) +
                 sin(self.phi) * sin(self.theta)) * sin(self.theta)) /
                (2 * sqrt((cos(self.phi) -
                 cos(other.phi)) ** 2 +
                 (-cos(other.theta) * sin(other.phi) +
                  cos(self.theta) * sin(self.phi)) ** 2 +
                 (-sin(other.phi) * sin(other.theta) +
                  sin(self.phi) * sin(self.theta)) ** 2)))

    def __str__(self) -> str:
        return '({:.3}, {:.3}, {:.3})'.format(self.x(), self.y(), self.z())


def random_point() -> PointOnUnitSphere:
    return PointOnUnitSphere(random.random() * 2 * pi,
                             random.random() * pi)


def distance(points: List[PointOnUnitSphere]) -> float:
    distance = 0.0
    for i, p1 in enumerate(points):
        for p2 in points[i + 1:]:
            distance += p1.distance(p2)

    return distance


def step(points: List[PointOnUnitSphere], gamma: float) -> List[PointOnUnitSphere]:
    new_points = []
    for i, p1 in enumerate(points):
        dtheta = 0.0
        dphi = 0.0
        for j, p2 in enumerate(points):
            if i == j:
                continue
            dtheta += p1.derivative_theta(p2)
            dphi += p1.derivative_phi(p2)
        new_points.append(PointOnUnitSphere(p1.theta + gamma * dtheta,
                                            p1.phi + gamma * dphi))

    return new_points


def find_equidistant_points_on_sphere(number_of_points: int) -> List[PointOnUnitSphere]:
    points = [random_point() for _ in range(number_of_points)]
    gamma = 0.1
    for _ in range(1000):
        print('{:.6}'.format(distance(points)))
        points = step(points, gamma)
    gamma = 0.01
    for _ in range(1000):
        print('{:.8}'.format(distance(points)))
        points = step(points, gamma)


    return points

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('USAGE: equidistance_points_on_sphere.py NUM')
    points = find_equidistant_points_on_sphere(int(sys.argv[1]))
    for point in points:
        print(point)
    print('{:.8}'.format(distance(points)))
