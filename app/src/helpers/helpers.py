# external imports
from math import cos, sin, radians
# internal imports
from ..actors.points.point import Point
from ..actors.radar import Radar


def radar_detection_to_point(
        detection: tuple[Radar, float, float]) -> Point:
    radar, distance, facing = detection
    point_angle = radians(radar.orientation + facing)
    return Point(
        x=radar.x + distance * cos(point_angle),
        y=radar.y + distance * sin(point_angle),
    )