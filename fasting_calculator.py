import datetime
import math

tday = datetime.datetime.now()

def get_julian_datetime(date):
    """
    Convert a datetime object into julian float.
    Args:
        date: datetime-object of date in question

    Returns: float - Julian calculated datetime.
    Raises: 
        TypeError : Incorrect parameter type
        ValueError: Date out of range of equation
    """

    # Ensure correct format
    if not isinstance(date, datetime.datetime):
        raise TypeError('Invalid type for parameter "date" - expecting datetime')
    elif date.year < 1801 or date.year > 2099:
        raise ValueError('Datetime must be between year 1801 and 2099')

    # Perform the calculation
    julian_datetime = 367 * date.year - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0) + int(
        (275 * date.month) / 9.0) + date.day + 1721013.5 + (
                          date.hour + date.minute / 60.0 + date.second / math.pow(60,
                                                                                  2)) / 24.0 - 0.5 * math.copysign(
        1, 100 * date.year + date.month - 190002.5) + 0.5

    return julian_datetime
def new_moon(julian_datetime):
	#we have considered the new moon on 6th January 2000 at 23:43 in Kolhapur
	day_buffer = julian_datetime - 2451550.34
	new_moons = day_buffer / 29.53
	frac = new_moons %1
	lnm = frac * 29.53
	dtg = 29.53 - lnm
	return dtg
	
print("The Next New Moon is in: ",new_moon(get_julian_datetime(tday)),"days.")


	
