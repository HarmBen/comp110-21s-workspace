"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

today: datetime = datetime.today()

__author__ = "730368084"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days_2_target: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    future_2_target: str = future_date(days_2_target)
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "% vaccination in " + str(days_2_target) + " days, which falls on " + str(future_date(days_2_target)) + ".")


# TODO 1: Define days_to_target function
def days_to_target(population, doses, doses_per_day, target) -> int:
    pop_vaccinated = (doses / 2)
    percentage_vaccinated = (pop_vaccinated / population)
    percentage_to_target = ((target / 100) - percentage_vaccinated)
    ppl_left_until_target = (percentage_to_target * population)
    return round(ppl_left_until_target / (doses_per_day / 2))

# TODO 3: Define future_date function
def future_date(days_2_target: int) -> str:
    fut_date: datetime = today + timedelta(days_2_target)
    return fut_date.strftime("%B %d, %Y")



if __name__ == "__main__":
    main()
