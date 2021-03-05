# roam-weekly-plan
Alfred workflow that generates a Roam weekly plan template

This workflow allows you to use a snippet trigger with [Alfred](https://www.alfredapp.com/) to generate
a weekly plan template for the next week as described by [Nat Eliason](https://www.nateliason.com) in his
excellent [Effortless Output with Roam](https://learn.nateliason.com/courses/764250) course. 

## Installation
To install, all you need to do is download the Roam Weekly Plan.alfredworkflow file from this repo and
open it with Alfred. Define the snippet trigger you want to use (I like `\\xrwp`) and use it whenever you
want to generate a new weekly plan. The script that generates the template is also available to look
at in this repo.

### Customization
The example script that is used by the workflow can be found in the `src/` directory. Edit this script in
your favorite editor to include your daily habits and pages to reference. This requires no coding experience:
just open the file and find the area that looks like the output below (starting on line 26), then edit that.
Once done, run `make` in your terminal and it will deposit a fresh RoamWeeklyPlan.alfredworkflow file in the
`dist/` directory. Import that into Alfred, and you'll be all set.

## Output
An example output looks like this: 
```
Week:: [[October 5th, 2020]]
Weekly Review:: [[Weekly Review October 5th, 2020]]
## Pages to Reference
    Go through these to find priorities for upcoming week.
    [[TODO]]
    [[Goals]]
    [[📝 Projects]]
    [[📓 Article Ideas]]
    [[🧠 Research]]
## Top Priorities
## Daily Goals
    Monday: [[October 5th, 2020]]
    Tuesday: [[October 6th, 2020]]
    Wednesday: [[October 7th, 2020]]
    Thursday: [[October 8th, 2020]]
    Friday: [[October 9th, 2020]]
    Saturday: [[October 10th, 2020]]
    Sunday: [[October 11th, 2020]]
## [[Daily Habits]]
    If these have a daily notes attribute, add what you did to those.
    Habit 1
        {{[[TODO]]}} [[October 5th, 2020]]
        {[[TODO]]} [[October 6th, 2020]]
        {[[TODO]]} [[October 7th, 2020]]
        {[[TODO]]} [[October 8th, 2020]]
        {[[TODO]]} [[October 9th, 2020]]
        {[[TODO]]} [[October 10th, 2020]]
        {[[TODO]]} [[October 11th, 2020]]
    [More habits here...]
```	

Enjoyed this workflow? [Buy me a beer!](https://www.buymeacoffee.com/kylestratis)
