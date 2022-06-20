def leap_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


month_length = {"January": 0,
                "February": 0,
                "March": 0,
                "April": 0,
                "May": 0,
                "June": 0,
                "July": 0,
                "August": 0,
                "September": 0,
                "October": 0,
                "November": 0,
                "December": 0}
sentence = "30 days in September, April, June and November"

year = 2020

for i in month_length:
    if i in sentence:
        month_length[i] = 30
    elif i == "February" and leap_year(year) == True:
        month_length[i] = 29
    elif i == "February":
        month_length[i] = 28
    elif i not in sentence:
        month_length[i] = 31

print(month_length)


month_length = {"January": 0,
                "February": 0,
                "March": 0,
                "April": 0,
                "May": 0,
                "June": 0,
                "July": 0,
                "August": 0,
                "September": 0,
                "October": 0,
                "November": 0,
                "December": 0}
sentence = "30 days in September, April, June and November"
for i in month_length:
    if i in sentence:
        month_length[i] = 30
    elif i == "February":
        month_length[i] = 28
    elif i not in sentence:
        month_length[i] = 31

print(month_length)
