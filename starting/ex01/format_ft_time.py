import datetime
import time

# First I need to get seconds from 1 1 1970. and formatted to be like this 1,000,000 
# that why I use time.time to get it the time and formatted to be like what we want, 
# the method 'format' is the key to that

time_in_seconds = "{:,}".format(time.time())

# I do the same thing to convert the seconds to the scientific format

time_in_scientific = "{:.2e}".format(time.time())

# and now I get the current time
now = datetime.datetime.now()

# and formatted to be like { month shortcut, day in number, years}
tody_date = now.strftime("%b %d %Y")
print(f"Seconds since January 1, 1970: {time_in_seconds} or {time_in_scientific} in scientific notation")
print(tody_date)