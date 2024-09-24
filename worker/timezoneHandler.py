import datetime
import pytz


def get_isttime():
    # Get the current time in UTC
    utc_now = datetime.datetime.now(pytz.utc)

    # Convert UTC time to IST
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_now = utc_now.astimezone(ist_timezone)

    # Format the time as YYYYMMDDHHMMSS
    formatted_time = ist_now.strftime("%Y%m%d%H%M%S")
    print(formatted_time)
    return formatted_time
