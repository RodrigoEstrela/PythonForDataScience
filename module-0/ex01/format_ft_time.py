from datetime import datetime, date

now_seconds = datetime.now().timestamp()
# Date today since Jan 1 1970 displayed in seconds and scientific notation
print("Seconds since January 1, 1970: {:,.4f} or {:.2e} in scientifc notation".format(now_seconds, now_seconds))
# Today normal display
print(date.today().strftime("%b %d %Y"))

