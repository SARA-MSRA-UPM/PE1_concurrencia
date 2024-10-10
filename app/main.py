# external imports
import threading
from time import sleep

from src.base.lector import Lector
# internal imports
from src.actors.points.circular_point import CircularPoint
from src.actors.points.eight_point import EightPoint
from src.actors.radar import Radar
from src.base.monitor import Monitor


if __name__ == '__main__':
    # Constants
    AREA=200

    # Create monitor
    monitor = Monitor()
    # Create lector
    lector = Lector(monitor=monitor)

    # Create points
    points = [
        CircularPoint(75, 75, 10),
        CircularPoint(150, 150, 20),
        EightPoint(100, 125)
    ]

    # Create radar
    radar = Radar(name="radar0",
                  position=(AREA/2, AREA/2),
                  detection_range=(AREA/2)*0.6,
                  orientation=0,
                  points=points,
                  monitor=monitor)

    # Start radar and point threads
    radar_thread = threading.Thread(target=radar.run)
    radar_thread.start()

    for point in points:
        point.start()

    lector.start()

    print("Executing during 5 seconds")
    sleep(5)
    print("Start STOP action")

    lector.stop()
    lector.join()
    print("Lector stopped")

    # Stop all threads
    radar.stop()
    radar_thread.join()
    print("Radar stopped")

    for point in points:
        point.stop()
        point.join()
    print("Points stopped")

    exit(0)
