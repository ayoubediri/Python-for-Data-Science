import datetime
import time

time_in_seconds = "{:,}".format(time.time())
time_in_scientific = "{:.2e}".format(time.time())
now = datetime.datetime.now()
tody_date = now.strftime("%b %d %Y")
print(f"Seconds since January 1, 1970: {time_in_seconds} or {time_in_scientific} in scientific notation")
print(tody_date)