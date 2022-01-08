import pandas
'''
Zalozenia:
 - funkcja dostaje daty w formacie 2019-06-16T24:00:00.000
  - intervals: przedzialy czasowe w formie array np [0,2,3]
            0 - godziny 6-12 rano
            1 - godziny 12-18 popoludnie
            2 - godziny 18-24 wieczor
            3 - godziny 24-6 noc
    
  - daytype: 0-swieto
            1 - dzien roboczy
Output: pandas Dataframe
'''
def interval_to_hours(interval):
    if interval == 0:
        start_time = '06:00:00'
        end_time = '12:00:00'
    elif interval == 1:
        start_time = '12:00:00'
        end_time = '18:00:00'
    elif interval == 2:
        start_time = '18:00:00'
        end_time = '23:59:59'
    elif interval == 3:
        start_time = '23:59:59'
        end_time = '6:00:00'
    return start_time, end_time


def filter_data(day_type, start_day, end_day, intervals):
    data = pandas.read_csv('../../data/dataZosia.csv') #toDo change path to our data!!!
    days = filter_days(data, start_day, end_day)
    weekdays = filter_weekdays(days, day_type)
    no_of_intervals = len(intervals)
    hours = pandas.DataFrame(columns=data.columns)
    for i in range(no_of_intervals):
        start_time, end_time = interval_to_hours(intervals[i])
        part_hours = filter_hours(weekdays, start_time, end_time)
        hours = hours.append(part_hours)
    return hours

def filter_days(data, start_day, end_day):
    zero_time = '00:00:00.000'
    start_date = start_day[0:11] + zero_time

    max_time = '23:59:59.000'
    end_date = end_day[0:11] + max_time
    days = data[(data['start_time'] >= start_date) & (data['start_time'] < end_date)]
    return days

def filter_weekdays(days, day_type):
    days['start_time'] = pandas.to_datetime(days['start_time'])

    if (day_type == 0):  # swieto
        weekdays = days[
            (days['start_time'].dt.weekday == 5) | (days['start_time'].dt.weekday == 6)]  # 5=Saturday, 6=Sunday
    else:
        weekdays = days[(days['start_time'].dt.weekday != 5) & (days['start_time'].dt.weekday != 6)]
    return weekdays

def filter_hours(data,start_time, end_time):
    hours = (data.set_index('start_time')
             .between_time(start_time, end_time)
             .reset_index()
             .reindex(columns=data.columns))
    return hours


#print(days['weekday'])
day_type = 1 #dni robocze
start_day = '2019-06-12T06:00:00.000'
end_day = '2019-06-19T05:00:00.000'
start_time = '05:00:00'
end_time = '11:00:00'
intervals = [1]
filtered = filter_data(day_type, start_day,end_day, intervals)
print("Filtered data:")
print(filtered['start_time'])

