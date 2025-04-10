# Alexandra Lesan
# 2433764

'''
Write a function called toCelsius that takes a temperature in
Fahrenheit and returns the corresponding temperature in Celsius rounded to 2 decimal places.
Here is the formula that you can use: C = (F - 32)*(5/9).
For example:
If the temperature in Fahrenheit is 77, then your function returns 25.0. 
'''
def toCelsius(F):
    return round((F - 32)*(5/9), 2)

# print(toCelsius(77))

'''
Download the file data.txt from Moodle. In your main
program, open the file data.txt for reading only. From this file you are to read all the lines
from the year 1964 to 1975 into a dictionary temp_dict. That is, all the lines in your file
before 1964 should not appear in temp_dict dictionary. In temp_dict the keys are the
years (as an integer), and the values are the list of temperatures from JAN to DEC (as floats and
changed to Celsius).
HINT: the map function may be useful to do fast change of floats from strings and from
Fahrenheit to Celsius. 
'''
file = open('data.txt', 'r')
file.seek(0)
temp_dict = {}
for i in range(4):
    file.readline()
for line in file:
    lst = line.rstrip().split()
    year = int(lst[0])
    lst = lst[1:]
    temp_dict[year] = []
    for temp in lst:
        temp_dict[year].append(toCelsius(float(temp)))
file.close()
# print(temp_dict)

'''
Write a function called avgTempYear that takes two arguments: a
dictionary (of same format as you read from the data.txt file) and year. The function returns
the average temperature for the given year in the dictionary rounded to 2 decimal places. If the
provided year is not in the dictionary, your code should use exceptions to handle it as we have
done in class by using the try-except-else block as needed. In the case of invalid year,
you should print a friendly message and your function in such a case should return nothing
'''
def avgTempYear(d, year):
    try:
        avg = round(sum(d[year])/len(d[year]), 2)
        return avg
    except:
        print("This year has not been found in the dictionary")

# print(avgTempYear(temp_dict, 1965))

'''
Write a function topThreeYears that takes a dictionary (of
same format as you read from the data.txt file) and returns a list of the three largest averages
in descending order among all the years. Pay attention to what data structures you may use for
efficiency. 
'''

def topThreeYears(d):
    l = []
    s = set()
    for year in d:
        s.add(avgTempYear(d, year))
    print(s)
    while len(l) != 3:
        for avg in s:
            if avg == max(s):
                mx = avg
                l.append(avg)
        s.remove(mx)
    return l

# print(topThreeYears(temp_dict))

"""
Write a function called avgTempMonth that takes a dictionary (of
same format as you read from the data.txt file) and a month (as a string of 3 characters) and
returns the average temperature for the given month across all years rounded to 2 decimal places.
Note that you may create a dictionary in your function to help you go back and forth between
string and integer representation of months.
For example: month_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, etc.}
"""

def avgTempMonth(d, month):
    month_dict = {}
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    for i in range(len(months)):
        temps_month = []
        for year in d:
            temps_month.append(d[year][i])
        month_dict[months[i]] = round(sum(temps_month)/len(temps_month), 2)
    print(month_dict)
    return month_dict[month]

# print(avgTempMonth(temp_dict, 'DEC'))