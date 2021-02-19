"""A vaccination calculator."""

__author__ = "730368084"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
today: datetime = datetime.today()
one_day: timedelta = timedelta(1)
tomorrow: datetime = today + one_day
fortnight: timedelta = timedelta(7 + 7)

population = int(input('Population: '))
doses = int(input('Doses administered: '))
doses_day = int(input('Doses per day: '))
target = int(input('Target percent vaccinated: '))

pop_vaccinated = (doses / 2)
percentage_vaccinated = (pop_vaccinated / population)
percentage_to_target = ((target / 100) - percentage_vaccinated)
ppl_left_until_target = (percentage_to_target * population)
days_left_until_target = round(ppl_left_until_target / (doses_day / 2))
date_of_target = today + timedelta(days_left_until_target)

print(pop_vaccinated)
print(percentage_vaccinated)
print(percentage_to_target)
print(ppl_left_until_target)
print(days_left_until_target)
print(date_of_target)

print("We will reach " + str(target) + "% vaccination in " + str(days_left_until_target) + " days, which falls on " + date_of_target.strftime("%B %d, %Y") + ".")