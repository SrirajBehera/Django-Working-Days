from django.shortcuts import render
import calendar

def index(request):
    return render(request, 'index.html')

def calculate(request):
    year = 2022
    month = int(request.GET.get('monthselected'))

    calendar.setfirstweekday(calendar.MONDAY)

    holidaycsv = request.GET.get('holiday_csv')
    customHoliday = list(map(int, holidaycsv.split(',')))

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    workingDates = []
    for day in range(1, 32):
        try:
            weekday = calendar.weekday(year, month, day)
        except ValueError: # for handling invalid dates
            continue
        if weekday < calendar.SATURDAY:
            workingDates.append(day)

    refinedWorkingDates = []
    for date in workingDates:
        if date not in customHoliday:
            refinedWorkingDates.append(date)
    
    params = {'month':months[month-1], 'customHoliday': customHoliday, 'refinedWorkingDates': refinedWorkingDates}
    return render(request, 'result.html', params)
