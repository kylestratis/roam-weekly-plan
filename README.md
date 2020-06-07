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

## Output
An example output looks like this: 
```
Week:: [[June 8th, 2020]]
## Top Weekly Goals
## [[Weekly Habits]]
    -
## Daily Goals
  - Monday: [[monday]]
  - Tuesday: [[tuesday]]
  - Wednesday: [[wednesday]]
  - Thursday: [[thursday]]
  - Friday: [[friday]]
  - Saturday: [[saturday]]
  - Sunday: [[sunday]]
```	
  
