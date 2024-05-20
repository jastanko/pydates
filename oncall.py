#!/usr/bin/env python3

from datetime import date, datetime

days_done = date.today().isoweekday()
days_left = 7 - days_done
hours_done = days_done * 12

hours_left = 20 - datetime.now().hour
if hours_left <= 0:
    print(f"You are done for the day!")
else:
    if hours_left > 8:
        hours_left = 8
    hours_done -= hours_left
    print(f"You have {hours_left} hours left today.")
   
hours_total = 7 * 12
pct_complete = hours_done/hours_total * 100

print(f"Hours left: {hours_total-hours_done}")
print(f"You are {pct_complete:.1f}% done.")
