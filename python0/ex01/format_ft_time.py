from datetime import datetime

now = datetime.now()

first_date = datetime(1970, 1, 1)

time_since = now - first_date

seconds = int(time_since.total_seconds())

print("Seconds since january 1, 1970:",seconds,"or","%.2e"%float(seconds),"in scientific notation")

month = ["0","Jan","Fab","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
print(month[now.month],now.day,now.year)
