"""
Time Conversion
This method takes a time in 12 hour format time and prints a 24 hour time

Example:
    input: 12:00:00AM
    output: 00:00:00
    input: 07:05:45PM
    output: 19:05:45
    input: 12:00:00PM
    output: 12:00:00
"""


def convert_to_24_hour(input_time):
    hours = int(input_time[:2])
    minutes = input_time[3:5]
    seconds = input_time[6:8]
    ampm = input_time[8:10]
    if ampm == 'PM' and hours != 12:
        hours += 12
    if ampm == 'AM' and hours == 12:
        hours = 0
    return '{0}:{1}:{2}'.format(str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2))


time = raw_input().strip()
print convert_to_24_hour(time)
