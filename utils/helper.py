import time


def delay(speed):

    if speed <= 0:
        return

    seconds = 0.05 / speed

    time.sleep(seconds)


def format_algorithm_name(name):

    if name == "A*":
        return "A-Star"

    return name