# Alexandra Lesan
# 2433764

# PART 1 for previous functions
'''
Write a function called toCelsius that takes a temperature in
Fahrenheit and returns the corresponding temperature in Celsius rounded to 2 decimal places.
Here is the formula that you can use: C = (F - 32)*(5/9).
For example:
If the temperature in Fahrenheit is 77, then your function returns 25.0. 
'''
def toCelsius(F):
    return round((F - 32)*(5/9), 2)

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
    except KeyError:
        print("This year has not been found in the dictionary")

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
    while len(l) != 3:
        for avg in s:
            if avg == max(s):
                mx = avg
                l.append(avg)
        s.remove(mx)
    return l

"""
Write a function called avgTempMonth that takes a dictionary (of
same format as you read from the data.txt file) and a month (as a string of 3 characters) and
returns the average temperature for the given month across all years rounded to 2 decimal places.
Note that you may create a dictionary in your function to help you go back and forth between
string and integer representation of months.
For example: month_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, etc.}
"""

def avgTempMonth(d, month):
    months_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,\
                    'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    month_i = months_dict[month]
    total = 0
    count = 0
    for year in d:
        total += d[year][month_i-1]
        count += 1
    return round(total/count, 2)



# PART 2
"""
Write a function belowFreezing that takes a dictionary (of same format as you read from the
data.txt file) and returns all months that have had a temperature value below freezing in
some year. On the given data, the output should be the months of January, February, March and
December. 
"""
def belowFreezing(d, year):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for i in range(12): # could also be range(len(d[year])), but that's 12
        if d[year][i] < 0:
            print(months[i])

"""
In your main program you are to write to a file called data_celsius.txt. Create this file
for writing using Python (don't manually create the file in the folder).
- In data_celsius.txt the first 4 lines are the same as the 4 lines in data.txt. Do not
copy and paste these 4 lines. Write Python code that automates this process for you.
- The next 12 lines are the 12 key-value pairs from your temp_dict. When you write this
data to your file, make sure the display format and spacing in data_celsius.txt is the
same as that of data.txt. 
"""

output_file = open('data_celsius.txt', 'w')
input_file = open('data.txt', 'r')
input_file.seek(0)
for i in range(4):
    output_file.write(input_file.readline())
input_file.close()
for year in temp_dict:
    output_file.write(f'{year:>4}')
    for temp in temp_dict[year]:
        output_file.write(f'{temp:>8.2f}')
    output_file.write('\n')
output_file.close()
