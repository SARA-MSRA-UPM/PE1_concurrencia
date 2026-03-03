# external imports
import math
from threading import Thread, Event
from time import sleep
# internal imports
from src.actors.points.point import Point
from src.monitors.detections_monitor import DetectionsMonitor
from src.models.radar_detection import RadarDetection

# Radar constants
INCREMENT = 15
REVOLUTIONS = 1


class Radar(Thread):
    def __init__(
            self,
            name: str,
            position: tuple[float, float],
            detection_range: float,
            orientation: float,
            points: list[Point],
            monitor: DetectionsMonitor,
        ):
        super().__init__()
        # Radar properties
        self.name = name
        self.x, self.y = position
        self.detection_range = detection_range
        self.orientation = orientation
        self.facing = 0
        self.detections = set()
        self.points = points
        self.monitor = monitor

        # Threads properties
        self._stop_event = Event()

    # Thread methods
    def run(self):
        while not self._stop_event.is_set():
            self.update()
            self.detect(self.points)
            sleep(INCREMENT/(360*REVOLUTIONS))

    def stop(self):
        self._stop_event.set()

    # Private Radar methods
    def _in_sector(self, point: Point, sector: float) -> bool:
        angle = self._angle(point)
        return abs(sector - angle) < INCREMENT/2

    def _angle(self, point: Point):
        return (math.degrees(
            math.atan2(point.y - self.y, point.x - self.x)) + 360) % 360

    def _distance(self, point: Point) -> float:
        return math.hypot(point.x - self.x, point.y - self.y)

    # Radar methods
    def update(self):
        self.facing = (self.facing + INCREMENT) % 360
        self.detection = self.detection_range

    def detect(self, points: list[Point]):
        # determine sector
        sector = (self.orientation + self.facing) % 360
        distances_detected = set()
        for point in points:
            if self._in_sector(point, sector):
                distance = self._distance(point)
                if self.detection_range >= distance:
                    distances_detected.add(distance)

        for distance in distances_detected:
            coordinates = self.get_cartesian_coords(distance, self.facing)
            radar_detection = RadarDetection(
                radar=self,
                distance=distance,
                facing=self.facing,
                x=coordinates[0],
                y=coordinates[1],
            )
            self.detections.add(radar_detection)
            self.monitor.update(detection=radar_detection)
            print(f"Detección: {radar_detection}")

    # PG1 methods
    def get_cartesian_coords(self, distance: float, angle: float) -> tuple[float, float]:
        x_relative: float = distance * math.cos(math.radians(angle + self.orientation))
        y_relative: float = distance * math.sin(math.radians(angle + self.orientation))
        return self.x + x_relative, self.y + y_relative
