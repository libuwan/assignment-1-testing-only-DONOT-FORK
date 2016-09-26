"""
Write a function getTimeName(hours, minutes) that returns the English name for
a point in time, such as "ten minutes past two", "half past three", "a quarter
to four", or "five o'clock". Assume that hours is between 1 and 12.
"""


def getTimeName(hours, minutes):
    """
    Convert hours and minutes to its English name.
    hours: the hours portion of the time
    minutes: the minutes portion of the time
    return a string containing the English name of the time
    """
    pass


hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
print(getTimeName(hours, minutes))
