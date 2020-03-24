def angleClock(hour: int, minutes: int) -> float:
    if hour == 12:
        hour = 0
    hourAngle = 0.5 * (hour * 60 + minutes)
    minutesAngle = minutes * 6

    angle = abs(hourAngle - minutesAngle)
    angle = min(angle, 360 - angle)

    return angle


print(angleClock(12, 30))
print(angleClock(3, 30))
print(angleClock(3, 15))
print(angleClock(4, 50))
print(angleClock(12, 0))

# Input: hour = 12, minutes = 30
# Output: 165
#
# Input: hour = 3, minutes = 30
# Output: 75
#
# Input: hour = 3, minutes = 15
# Output: 7.5
#
# Input: hour = 4, minutes = 50
# Output: 155
#
# Input: hour = 12, minutes = 0
# Output: 0
