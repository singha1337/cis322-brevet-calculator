"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

SPEEDS = {600: [28, 11.428], 400: [30, 15], 200: [32, 15], 0: [34, 15]}
MAX_TIME_LIMIT = {1000: [75, 00], 600: [40, 00], 400: [27, 00], 300: [20, 00], 200: [13, 30]}


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    time = arrow.get(brevet_start_time).replace(tzinfo='US/Pacific')

    if type(control_dist_km) is str:
        return "Invalid input!"
    elif type(control_dist_km) is chr:
        return "Invalid input!"
    elif int(control_dist_km) < 0 or int(control_dist_km) > (1.20 * int(brevet_dist_km)):
        return "Invalid input!"

    if control_dist_km == 0:
        return time.isoformat()
    if control_dist_km > brevet_dist_km:
        control_dist_km = brevet_dist_km

    remaining_distance = control_dist_km
    total_time = 0.0
    for distance in SPEEDS:
        if remaining_distance >= distance:
            total_time += ((remaining_distance - distance) / SPEEDS[distance][0])
            remaining_distance = distance
    hours = int(total_time)
    minutes = round((total_time - hours) * 60)
    time = time.shift(hours=+ hours, minutes=+ minutes)

    return time.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    time = arrow.get(brevet_start_time, tzinfo='US/Pacific')

    if type(control_dist_km) is str:
        return "Invalid input!"
    elif type(control_dist_km) is chr:
        return "Invalid input!"
    elif int(control_dist_km) < 0 or int(control_dist_km) > (1.20 * int(brevet_dist_km)):
        return "Invalid input!"

    if control_dist_km == 0:
        time = time.shift(hours=+ 1)

    elif control_dist_km <= 60:
        total_time = control_dist_km / 20
        hours = int(total_time)
        minutes = int((total_time - hours)*60)
        time = time.shift(hours=+ hours + 1, minutes=+ minutes)

    elif control_dist_km > brevet_dist_km:
        hours = MAX_TIME_LIMIT[brevet_dist_km][0]
        minutes = MAX_TIME_LIMIT[brevet_dist_km][1]
        time = time.shift(hours=+ hours, minutes=+ minutes)

    else:
        remaining_distance = control_dist_km
        total_time = 0.0
        for distance in SPEEDS:
            if remaining_distance > distance:
                total_time += ((remaining_distance - distance) / SPEEDS[distance][1])
                remaining_distance = distance
        hours = int(total_time)
        minutes = round((total_time - hours)*60)
        time = time.shift(hours=+ hours, minutes=+ minutes)

    return time.isoformat()
