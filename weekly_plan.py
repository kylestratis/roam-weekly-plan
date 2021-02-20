# -*- coding: utf-8 -*-
import sys
import datetime


def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def custom_strftime(fmt, t):
    return t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))


def next_week():
    today = datetime.date.today()
    next_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
    return [
        custom_strftime("%B {S}, %Y", next_monday + datetime.timedelta(days=i))
        for i in range(0, 7)
    ]


def generate_template():
    week = next_week()
    template = """
Week:: [[{monday}]]
Weekly Review:: [[Weekly Review {monday}]]
## Pages to Reference
    Go through these to find priorities for upcoming week.
    [[TODO]]
    [[Goals]]
    [[📝 Projects]]
    [[🎥 Video Ideas]]
    [[📓 Article Ideas]]
    [[🧠 Research]]
## Top Priorities
	1 article or video, 1 project, 1-2 books and/or courses from above. Individual tasks filter to daily goals.
## Daily Goals
    Monday: [[{monday}]]
    Tuesday: [[{tuesday}]]
    Wednesday: [[{wednesday}]]
    Thursday: [[{thursday}]]
    Friday: [[{friday}]]
    Saturday: [[{saturday}]]
    Sunday: [[{sunday}]]
## [[Daily Habits]]
    If these have a daily notes attribute, add what you did to those.
    Habit 1 - Daily example
        {{{{[[TODO]]}}}} [[{monday}]]
        {{{{[[TODO]]}}}} [[{tuesday}]]
        {{{{[[TODO]]}}}} [[{wednesday}]]
        {{{{[[TODO]]}}}} [[{thursday}]]
        {{{{[[TODO]]}}}} [[{friday}]]
        {{{{[[TODO]]}}}} [[{saturday}]]
        {{{{[[TODO]]}}}} [[{sunday}]]
    Habit 2 - Weekend example
        {{{{[[TODO]]}}}} [[{saturay}]]
        {{{{[[TODO]]}}}} [[{sunday}]]
    Habit 3 - Once a week example
        {{{{[[TODO]]}}}} [[{wednesday}]]
    """.format(
        monday=week[0],
        tuesday=week[1],
        wednesday=week[2],
        thursday=week[3],
        friday=week[4],
        saturday=week[5],
        sunday=week[6],
    )
    return template


s = generate_template()
sys.stdout.write(s)
