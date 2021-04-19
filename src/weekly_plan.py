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
## Overview
    There are two ways to do your planning:
        1. Upfront. Once a week, go through your priority projects and pull blockrefs to their TODOs to the day you want to accomplish them, nested under a blockref to the project.
        2. One Big Thing. Pick one major item to work on (or individual TODOs that would represent one big thing to accomplish) as a project selection, and also set aside habit time.
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
        {{{{[[TODO]]}}}} Project selection
        {{{{[[TODO]]}}}} Habit time
    Tuesday: [[{tuesday}]]
        {{{{[[TODO]]}}}} Project selection
        {{{{[[TODO]]}}}} Habit time
    Wednesday: [[{wednesday}]]
        {{{{[[TODO]]}}}} Project selection
        {{{{[[TODO]]}}}} Habit time
    Thursday: [[{thursday}]]
        {{{{[[TODO]]}}}} Project selection
        {{{{[[TODO]]}}}} Habit time
    Friday: [[{friday}]]
        {{{{[[TODO]]}}}} Habit time
    Saturday: [[{saturday}]]
        {{{{[[TODO]]}}}} Project selection
        {{{{[[TODO]]}}}} Habit time
    Sunday: [[{sunday}]]
        {{{{[[TODO]]}}}} Project selection
        {{{{[[TODO]]}}}} Habit time
## [[Daily Habits]]
    If these have a daily notes attribute, add what you did to those.
    Process "Things to Process" and Writing Inbox
        {{{{[[TODO]]}}}} [[{monday}]]
        {{{{[[TODO]]}}}} [[{wednesday}]]
        {{{{[[TODO]]}}}} [[{thursday}]]
        {{{{[[TODO]]}}}} [[{sunday}]]
    Process Reading Inboxes
        {{{{[[TODO]]}}}} [[{monday}]]
        {{{{[[TODO]]}}}} [[{tuesday}]]
        {{{{[[TODO]]}}}} [[{wednesday}]]
        {{{{[[TODO]]}}}} [[{thursday}]]
        {{{{[[TODO]]}}}} [[{friday}]]
        {{{{[[TODO]]}}}} [[{saturday}]]
        {{{{[[TODO]]}}}} [[{sunday}]]
    Research One Research Topic
        {{{{[[TODO]]}}}} [[{tuesday}]]
        {{{{[[TODO]]}}}} [[{saturday}]]
    [[Practice Elixir]]
        {{{{[[TODO]]}}}} [[{monday}]]
        {{{{[[TODO]]}}}} [[{tuesday}]]
        {{{{[[TODO]]}}}} [[{wednesday}]]
        {{{{[[TODO]]}}}} [[{thursday}]]
        {{{{[[TODO]]}}}} [[{friday}]]
        {{{{[[TODO]]}}}} [[{saturday}]]
        {{{{[[TODO]]}}}} [[{sunday}]]
    [[Exercise]]
        {{{{[[TODO]]}}}} [[{monday}]]
        {{{{[[TODO]]}}}} [[{tuesday}]]
        {{{{[[TODO]]}}}} [[{wednesday}]]
        {{{{[[TODO]]}}}} [[{thursday}]]
        {{{{[[TODO]]}}}} [[{friday}]]
        {{{{[[TODO]]}}}} [[{saturday}]]
        {{{{[[TODO]]}}}} [[{sunday}]]
    [[Read]]
        {{{{[[TODO]]}}}} [[{monday}]]
        {{{{[[TODO]]}}}} [[{tuesday}]]
        {{{{[[TODO]]}}}} [[{wednesday}]]
        {{{{[[TODO]]}}}} [[{thursday}]]
        {{{{[[TODO]]}}}} [[{friday}]]
        {{{{[[TODO]]}}}} [[{saturday}]]
        {{{{[[TODO]]}}}} [[{sunday}]]
    [[Greek]]
        {{{{[[TODO]]}}}} [[{monday}]]
        {{{{[[TODO]]}}}} [[{tuesday}]]
        {{{{[[TODO]]}}}} [[{wednesday}]]
        {{{{[[TODO]]}}}} [[{thursday}]]
        {{{{[[TODO]]}}}} [[{friday}]]
        {{{{[[TODO]]}}}} [[{saturday}]]
        {{{{[[TODO]]}}}} [[{sunday}]]
    [[Bass]]
        {{{{[[TODO]]}}}} [[{monday}]]
        {{{{[[TODO]]}}}} [[{tuesday}]]
        {{{{[[TODO]]}}}} [[{wednesday}]]
        {{{{[[TODO]]}}}} [[{thursday}]]
        {{{{[[TODO]]}}}} [[{friday}]]
        {{{{[[TODO]]}}}} [[{saturday}]]
        {{{{[[TODO]]}}}} [[{sunday}]]
    Add to [[Brag Document 2021]]
        {{{{[[TODO]]}}}} [[{saturday}]]
    Work on newsletter
        {{{{[[TODO]]}}}} [[{friday}]]
    Update public mind garden
        {{{{[[TODO]]}}}} [[{saturday}]]
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
