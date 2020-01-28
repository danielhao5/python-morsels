import datetime
import calendar


def meetup_date(year: int, month: int, nth: int=4, weekday: int=3) -> datetime.date:
    """Determine which day of the month the San Diego Python meetup should be

    The meetup is on the fourth Thrusday of the month
    """
    date_first_week = datetime.date(year, month, 1)

    day_delta = (weekday + 1) - date_first_week.isocalendar()[2] # weekday is datetime.date.weekday format not isocalendar, so +1 to be in range 1..7
    if nth > 0:
        week_delta = nth - 1 if day_delta >= 0 else nth
    else:
        nth_from_end = len(calendar.monthcalendar(year, month)) + nth
        week_delta = nth_from_end - 1 if day_delta >= 0 else nth_from_end

    three_week_delta = datetime.timedelta(days=day_delta, weeks=week_delta)

    date_fourth_week = date_first_week + three_week_delta

    return date_fourth_week


if __name__ == "__main__":
    print(meetup_date(2016, 2, nth=4, weekday=3))

