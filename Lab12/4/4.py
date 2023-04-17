import datetime

# Read in the file containing dates
f = open("Lab12/4/dates.txt", "r")
dates = f.readlines()

# Convert each date string into a datetime object
dates = [datetime.datetime.strptime(date.strip(), "%Y-%m-%d") for date in dates]

# Calculate the number of days between each date and today
now = datetime.datetime.now()
delta_days = [(now - date).days for date in dates]

# Sort the delta days list in ascending order
delta_days.sort()

# Print out the sorted delta days list
print(delta_days)
