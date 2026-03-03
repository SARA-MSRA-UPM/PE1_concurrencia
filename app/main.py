# external imports
import threading
from time import sleep
# internal imports
from src.actors.points.circular_point import CircularPoint
from src.actors.points.eight_point import EightPoint
from src.actors.points.point import Point
from src.actors.radar import Radar
from src.actors.detections_consumer import DetectionsConsumer
from src.actors.common_detections_searcher import CommonDetectionsSearcher
from src.monitors.detections_monitor import DetectionsMonitor
from src.monitors.system_detection_data import SystemDetectionsData

if __name__ == '__main__':
    # Constants
    AREA=200

    # Initialize monitors
    monitor = DetectionsMonitor()

    # Create points
    points = [
        CircularPoint(75, 75, 10),
        CircularPoint(150, 150, 20),
        EightPoint(100, 125),
    ]

    # Create radars
    radars = [
        Radar(
            name="radar0",
            position=(AREA/2, AREA/2),
            detection_range=(AREA/2)*0.6,
            orientation=0,
            points=points,
            monitor=monitor
        )
    ]

    # Start radar and point threads
    for radar in radars:
        radar.start()

    for point in points:
        point.start()

    # Create and start consumer
    consumers = [
        DetectionsConsumer(
            monitor=monitor
        )
    ]
    for consumer in consumers:
        consumer.start()

    # Wait 10 seconds of execution
    sleep(15)

    # Stop all threads
    for consumer in consumers:
        consumer.stop()
        consumer.join()

    for radar in radars:
        radar.stop()
        radar.join()

    for point in points:
        point.stop()
        point.join()

    exit(0)
