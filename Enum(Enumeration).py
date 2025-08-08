from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# print(Color.RED)  # Output: Color.RED
# print(Color(1))  # Output: Color.RED
# print(Color['RED'])  # Output: Color.RED
# print(Color.RED.value)  # Output: 1


def create_car(color: Color):
    if color == Color.RED:
        return "You chose Red!"
    elif color == Color.GREEN:
        return "You chose Green!"
    elif color == Color.BLUE:
        return "You chose Blue!"
    else:
        return "Unknown color!"


print(create_car(Color.RED))  # Output: You chose Red!
