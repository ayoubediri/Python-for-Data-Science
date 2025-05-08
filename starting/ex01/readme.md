# Mastering Time in Python: A Comprehensive Guide to Built-in Modules

## 📄 Description

This guide provides a comprehensive overview of how to work with dates and times in Python using its powerful built-in `time` and `datetime` modules. No external libraries are required. Understanding these modules is crucial for a wide range of applications, from logging and data analysis to scheduling tasks and handling timestamps.

**Why this guide is useful:**

* **Fundamental Skill:** Time manipulation is a common task in programming.
* **No External Dependencies:** Learn to leverage what Python offers out-of-the-box.
* **Consolidated Knowledge:** A one-stop reference for common time-related operations in Python.
* **Clear Examples:** Practical code snippets to illustrate concepts.

## 📚 Table of Contents

* [📄 Description](#-description)
* [📚 Table of Contents](#-table-of-contents)
* [🚀 Introduction: Python's Time Toolkit](#-introduction-pythons-time-toolkit)

  * [The `time` Module (Overview)](#the-time-module-overview)
  * [The `datetime` Module (Overview)](#the-datetime-module-overview)
* [✅ No Installation Required](#-no-installation-required)
* [⚙️ The `time` Module in Detail](#⚙️-the-time-module-in-detail)

  * [Epoch and Timestamps: `time.time()`](#epoch-and-timestamps-timetime)
  * [Time Structures: `struct_time`](#time-structures-struct_time)
  * [Getting Local and UTC Time Structures: `localtime()` and `gmtime()`](#getting-local-and-utc-time-structures-localtime-and-gmtime)
  * [Converting `struct_time` to Timestamp: `mktime()`](#converting-struct_time-to-timestamp-mktime)
  * [Formatting Time: `time.strftime()`](#formatting-time-timestrftime)
  * [Pausing Execution: `time.sleep()`](#pausing-execution-timesleep)
  * [Measuring Performance: `perf_counter()` and `process_time()`](#measuring-performance-perfcounter-and-processtime)
* [📅 The `datetime` Module in Detail](#📅-the-datetime-module-in-detail)

  * [Core Objects: `date`, `time`, `datetime`, `timedelta`, `tzinfo`](#core-objects-date-time-datetime-timedelta-tzinfo)
  * [Creating `datetime` Objects](#creating-datetime-objects)

    * [`datetime.now()` and `datetime.utcnow()`](#datetimenow-and-datetimeutcnow)
    * [`datetime.today()`](#datetimetoday)
    * [Specific Date and Time](#specific-date-and-time)
    * [From Timestamp: `fromtimestamp()`](#from-timestamp-fromtimestamp)
  * [Creating `date` and `time` Objects](#creating-date-and-time-objects)
  * [Formatting and Parsing with `strftime()` and `strptime()`](#formatting-and-parsing-with-strftime-and-strptime)

    * [Common Format Codes](#common-format-codes)
  * [Time Arithmetic with `timedelta`](#time-arithmetic-with-timedelta)
* [🌍 Handling Timezones](#-handling-timezones)

  * [Naive vs. Aware Datetime Objects](#naive-vs-aware-datetime-objects)
  * [The `datetime.timezone` Class (Python 3.2+)](#the-datetimetimezone-class-python-32)
  * [The `zoneinfo` Module (Python 3.9+)](#the-zoneinfo-module-python-39)
  * [Converting Between Timezones](#converting-between-timezones)
* [⏱️ Practical Examples](#⏱️-practical-examples)

  * [Get Current Date and Time in Various Formats](#get-current-date-and-time-in-various-formats)
  * [Calculate Time Difference](#calculate-time-difference)
  * [Add/Subtract Time](#addsubtract-time)
* [💡 Best Practices and Common Pitfalls](#-best-practices-and-common-pitfalls)
* [🤝 Contributing to This Guide](#-contributing-to-this-guide)
* [📜 License](#-license)
* [🙏 Acknowledgements](#-acknowledgements)
* [🔗 Further Resources](#-further-resources)

## 🚀 Introduction: Python's Time Toolkit

Python provides two primary built-in modules for handling dates and times: `time` and `datetime`.

### The `time` Module (Overview)

The `time` module provides functions for working with time. It often deals with "Unix time" or "epoch seconds" (seconds since 00:00:00 UTC on January 1, 1970). It's generally lower-level and can be more platform-dependent for things like resolution.

### The `datetime` Module (Overview)

The `datetime` module supplies classes for manipulating dates and times in a more object-oriented way. It offers data types like `date`, `time`, `datetime`, and `timedelta`, making complex operations more intuitive. This is usually the preferred module for most date and time logic.

## ✅ No Installation Required

The `time` and `datetime` modules are part of Python's standard library. You do not need to install anything extra to use them. Simply import them into your Python scripts:

```python
import time
import datetime
```

---

## ⚙️ The `time` Module in Detail

### Epoch and Timestamps: `time.time()`

This function returns the current time as a floating-point number representing seconds since the epoch (January 1, 1970, 00:00:00 UTC).

```python
import time

current_timestamp = time.time()
print(f"Seconds since epoch: {current_timestamp}")
```

### Time Structures: `struct_time`

Several functions in the `time` module return or operate on a `time.struct_time` object. This is a tuple-like object with named attributes:

* `tm_year`: Year (e.g., 2023)
* `tm_mon`: Month (1-12)
* `tm_mday`: Day of month (1-31)
* `tm_hour`: Hour (0-23)
* `tm_min`: Minute (0-59)
* `tm_sec`: Second (0-61; 60/61 for leap seconds)
* `tm_wday`: Day of week (0-6, Monday is 0)
* `tm_yday`: Day of year (1-366)
* `tm_isdst`: Daylight Saving Time flag (-1, 0, or 1)

### Getting Local and UTC Time Structures: `localtime()` and `gmtime()`

```python
import time

local_time_struct = time.localtime()
utc_time_struct = time.gmtime()

print(f"Local time struct: {local_time_struct}")
print(f"UTC time struct:   {utc_time_struct}")
```

### Converting `struct_time` to Timestamp: `mktime()`

```python
import time

local_time_struct = time.localtime()
timestamp_from_struct = time.mktime(local_time_struct)
print(f"Timestamp from struct: {timestamp_from_struct}")
```

### Formatting Time: `time.strftime()`

```python
import time

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"Formatted local time: {formatted_time}")
```

### Pausing Execution: `time.sleep()`

```python
import time

print("Start")
time.sleep(2.5)
print("End (after 2.5 seconds)")
```

### Measuring Performance: `perf_counter()` and `process_time()`

```python
import time

start_perf = time.perf_counter()
start_proc = time.process_time()

# Simulate work
for _ in range(1000000): pass
time.sleep(0.1)

end_perf = time.perf_counter()
end_proc = time.process_time()

print(f"Wall time (perf_counter): {end_perf - start_perf:.4f} seconds")
print(f"CPU time (process_time): {end_proc - start_proc:.4f} seconds")
```

---

## 📅 The `datetime` Module in Detail

### Core Objects: `date`, `time`, `datetime`, `timedelta`, `tzinfo`

* `date`: Calendar date (year, month, day).
* `time`: Time independent of date (hour, minute, second, microsecond, tzinfo).
* `datetime`: Combination of date and time.
* `timedelta`: Duration expressing the difference between two dates/times.
* `tzinfo`: Abstract base class for timezone information.

### Creating `datetime` Objects

#### `datetime.now()` and `datetime.utcnow()`

```python
from datetime import datetime, timezone

now_local_naive = datetime.now()
now_utc_aware = datetime.now(timezone.utc)
now_utc_naive = datetime.utcnow()

print(now_local_naive)
print(now_utc_aware)
print(now_utc_naive)
```

#### `datetime.today()`

```python
from datetime import datetime

today = datetime.today()
print(today)
```

#### Specific Date and Time

```python
from datetime import datetime

specific_dt = datetime(2024, 7, 26, 10, 30, 15)
print(specific_dt)
```

#### From Timestamp: `fromtimestamp()`

```python
import time
from datetime import datetime, timezone

ts = time.time()

dt_local = datetime.fromtimestamp(ts)
dt_utc = datetime.fromtimestamp(ts, timezone.utc)

print(dt_local)
print(dt_utc)
```

### Creating `date` and `time` Objects

```python
from datetime import date, time

today_date = date.today()
specific_date = date(2025, 1, 1)
specific_time = time(15, 45, 30)

print(today_date)
print(specific_date)
print(specific_time)
```

### Formatting and Parsing with `strftime()` and `strptime()`

```python
from datetime import datetime

now = datetime.now()
formatted = now.strftime("%A, %B %d, %Y %I:%M:%S %p")
parsed = datetime.strptime("2023-10-26 14:35:00", "%Y-%m-%d %H:%M:%S")

print(formatted)
print(parsed)
```

#### Common Format Codes

| Code | Meaning                             | Example |
| ---- | ----------------------------------- | ------- |
| %Y   | Year with century                   | 2023    |
| %m   | Month as zero-padded decimal        | 03      |
| %d   | Day of the month as zero-padded     | 05      |
| %H   | Hour (24-hour clock) as zero-padded | 14      |
| %M   | Minute as zero-padded               | 30      |
| %S   | Second as zero-padded               | 59      |
| %A   | Weekday full name                   | Monday  |
| %B   | Month full name                     | March   |

### Time Arithmetic with `timedelta`

```python
from datetime import datetime, timedelta

now = datetime.now()
tomorrow = now + timedelta(days=1)

print(now)
print(tomorrow)
```

---

## 🌍 Handling Timezones

### Naive vs. Aware Datetimes

* **Naive:** No timezone info.
* **Aware:** Contains `tzinfo`.

### The `datetime.timezone` Class (Python 3.2+)

```python
from datetime import datetime, timezone, timedelta

utc_tz = timezone.utc
est = timezone(timedelta(hours=-5), name="EST")
now_utc = datetime.now(utc_tz)
now_est = now_utc.astimezone(est)

print(now_utc)
print(now_est)
```

### The `zoneinfo` Module (Python 3.9+)

```python
from datetime import datetime
from zoneinfo import ZoneInfo

now_ny = datetime.now(ZoneInfo("America/New_York"))
now_tokyo = datetime.now(ZoneInfo("Asia/Tokyo"))

print(now_ny)
print(now_tokyo)
```

### Converting Between Timezones

```python
from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime.now(ZoneInfo("UTC"))
ny_time = utc_time.astimezone(ZoneInfo("America/New_York"))
print(utc_time)
print(ny_time)
```

---

## ⏱️ Practical Examples

### Get Current Date and Time in Various Formats

```python
from datetime import datetime

now = datetime.now()
print(now.isoformat())
print(now.strftime("%Y/%m/%d %H:%M"))
```

### Calculate Time Difference

```python
from datetime import datetime

e1 = datetime(2024, 1, 1, 9, 0)
e2 = datetime(2024, 1, 1, 17, 30)
diff = e2 - e1
print(diff)
print(diff.total_seconds() / 3600)
```

### Add/Subtract Time

```python
from datetime import datetime, timedelta

dt = datetime(2024, 5, 10, 14, 0)
reminder = dt - timedelta(days=3, hours=12)
print(dt)
print(reminder)
```

---

## 💡 Best Practices and Common Pitfalls

* Prefer `datetime` for most applications.
* Store and calculate in UTC; convert to local for display.
* Understand naive vs. aware objects.
* Use `datetime.now(timezone.utc)` for aware UTC datetimes.
* Rely on `zoneinfo` (Python 3.9+) for full timezone support.

## 🤝 Contributing to This Guide

Contributions are welcome! Please submit issues or pull requests on the repository hosting this guide.

## 📜 License

This guide is provided under the MIT License. The Python time and datetime modules are under the PSF License.

## 🙏 Acknowledgements

* Python official documentation for `time` and `datetime` modules.

## 🔗 Further Resources

* [time module documentation](https://docs.python.org/3/library/time.html)
* [datetime module documentation](https://docs.python.org/3/library/datetime.html)
* [zoneinfo module documentation](https://docs.python.org/3/library/zoneinfo.html)
