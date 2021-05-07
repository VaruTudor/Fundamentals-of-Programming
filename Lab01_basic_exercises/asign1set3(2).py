day=input('day of birth:')
month=input('month of birth:')
year=int(input('year of birth:'))
day2=input('current day:')
month2=input('current month:')
year2=int(input('current year:'))

yeardays=[31,28,31,30,31,30,31,31,30,31,30,31]
month=int(month)
month2=int(month2)
days=0 #total number of days
#determines whther a year is leap or not and returns the answer
def leap(y):
    if y%4==0:
        return True
    else: return False
#determines how many leap years are between two given years
def TotalLeaps(y1,y2):
    s=0
    for i in range(y1,y2):
        if leap(year):
            s+=1
    return s
month-=1
month2-=1
for i in range(month,11):
    days+=yeardays[i]
for i in range(month2,0,-1):
    days+=yeardays[i]
if leap(year):
    days+=1
if leap(year2):
    days+=1
year+=1
year2-=1
days=366*(year2-year)-TotalLeaps(year,year2)
print('number of days is:',days)
