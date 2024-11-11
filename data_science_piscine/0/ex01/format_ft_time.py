# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$

import datetime as dt
import time as time
from datetime import timezone

current_time = time.time() # Seconds since January 1, 1970, 00:00:00 (UTC)
posix_date = dt.date.fromtimestamp(42)

print("Seconds since {} {}, {}:".format(posix_date.strftime("%B"), posix_date.day, posix_date.year),
      current_time, "or {:.2e} in scientific notation".format(current_time))
print(dt.date.today().strftime("%b %d %Y"))

# for i in range(0, 20):
#     print(time.time())
#     i = i+1