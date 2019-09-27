"""
Write a program that prints the day of the week given a number of days and weeks.
Example:​ 30 days and 6 weeks from Monday is Wednesday.

> A couple notes:
> * The day calculation by date could be accomplished **lot** easier and in a **much** more robust way by importing `datetime` and just adding days to the date. But, this way works and it is more fun :)
> * I borrowed the `from_date` formula from this page: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
> * I didn't use the `weeks` input because it does not change the outcome.

"""
import math
from datetime import datetime
from datetime import timedelta  

class DayOfWeekCalculator:
    def __init__(self,start,days,weeks):
        self.start = start
        self.days = days
        self.weeks = weeks
        self.week_days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
        self.new_month = ""

    def get_weekday(self):
        if self.is_date():
            self.get_new_month()
            self.from_date()
        else:
            self.get_start_index()
        self.from_weekday()
        return self.weekday_string()

    def is_date(self):
        return "/" in self.start

    def get_start_index(self):
        self.start_index = self.week_days.index(self.start.lower())

    def from_weekday(self):
        remainder = (self.days % 7)
        diff = (self.start_index + remainder)
        if diff >= 7: diff -= 7
        self.day_diff = diff

    def from_date(self):
        month, day, year = map(int, self.start.split("/"))
        if month > 2: 
            month -= 2 
        else: 
            month += 10
            day -= 1
        yr = (abs(year) % 100)
        ce = int(str(year)[:2])
        self.start_index = ((day 
                            + math.floor((2.6*month) - .2)
                            - (2*ce) 
                            + yr 
                            + math.floor(yr/4) 
                            + math.floor(ce/4) \
                            ) % 7)

    def get_new_month(self):
        parsed_date = datetime.strptime(self.start, '%m/%d/%Y')
        self.new_month = (parsed_date + timedelta(days=self.days)).strftime("%B")
        
    def weekday_string(self):
        new_day = self.week_days[self.day_diff].capitalize()
        print(f'Today is { self.start.capitalize() }. in {self.days} day(s) and {self.weeks} week(s), it will be {new_day}.')
        if self.new_month != "": print(f'The month will be {self.new_month}.')
        return new_day


# 4a. ​Today is Sunday - What day of the week will it be in 100 days?
DayOfWeekCalculator("Sunday",100,0).get_weekday()
# 4b.​ Today is Tuesday - What day of the week will it be in 4 weeks and 2 days? 
DayOfWeekCalculator("Tuesday",2,4).get_weekday()
# 4c.​ Today is Friday - What day of the week will it be in 294 days?
DayOfWeekCalculator("Friday",294,0).get_weekday()
# 4d.​ Bonus: What month and day is it 73 days after October 31st 2018?
DayOfWeekCalculator("10/31/2018",73,0).get_weekday()

# user input accepted as well:
def user_input():
    print("________________________________________________")
    print("You can enter your own values!")
    print("What is the start day or date? (ex: 'Monday' or '1/14/2010' [date is 'm/d/yyyy' format]):")
    usr_start = input("Start day or date: ")
    print("How many days would you like to add?")
    usr_days = input("Number of days: ")
    print("How many weeks would you like to add?")
    usr_weeks = input("Weeks: ")
    return [str(usr_start),int(usr_days),int(usr_weeks)]

user_inputs = user_input()

DayOfWeekCalculator(user_inputs[0],user_inputs[1],user_inputs[2]).get_weekday()