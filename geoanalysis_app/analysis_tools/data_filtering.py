import pandas
pandas.options.mode.chained_assignment = None

# Zalozenia:
#  - funkcja dostaje daty w formacie 2019-06-16T24:00:00.000
#   - intervals: przedzialy czasowe w formie array np  ["RANO", "POŁUDNIE", "WIECZÓR", "NOC"]
#             "RANO" - godziny 6-12 rano
#             "POŁUDNIE" - godziny 12-18 popoludnie
#             "WIECZÓR" - godziny 18-24 wieczor
#             "NOC" - godziny 24-6 noc
#
#   - daytype: ["NORMALNY", "ŚWIĄTECZNY"]
# Output: pandas Dataframe

def interval_to_hours(interval):
    if interval == "RANO":
        start_time = '06:00:00'
        end_time = '12:00:00'
    elif interval == "POŁUDNIE":
        start_time = '12:00:00'
        end_time = '18:00:00'
    elif interval == "WIECZÓR":
        start_time = '18:00:00'
        end_time = '23:59:59'
    elif interval == "NOC":
        start_time = '23:59:59'
        end_time = '6:00:00'
    return start_time, end_time


def filter_data(data, day_type, start_day, end_day, intervals):
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
    zero_time = 'T00:00:00.000'
    start_date = start_day + zero_time

    max_time = 'T23:59:59.000'
    end_date = end_day + max_time
    days = data[(data['Start Time'] >= start_date) & (data['Start Time'] < end_date)]
    return days


def filter_weekdays(days, day_type):
    if (day_type == "ŚWIĄTECZNY"):  # swieto
        weekdays = days[
            (pandas.to_datetime(days['Start Time']).dt.weekday == 5) | (pandas.to_datetime(days['Start Time']).dt.weekday == 6)]  # 5=Saturday, 6=Sunday
    else:
        weekdays = days[(pandas.to_datetime(days['Start Time']).dt.weekday != 5) & (pandas.to_datetime(days['Start Time']).dt.weekday != 6)]
    return weekdays


def filter_hours(data,start_time, end_time):
    data['Start Time'] = pandas.to_datetime(data['Start Time'])
    hours = (data.set_index('Start Time')
             .between_time(start_time, end_time)
             .reset_index()
             .reindex(columns=data.columns))
    hours['Start Time'] = hours['Start Time'].dt.strftime("%Y-%m-%dT%H:%M:%S.000")
    return hours


# data = pandas.read_csv('../../data/data.csv')
# day_type = ["NORMALNY"] #dni robocze
# start_day = '2019-06-12'
# end_day = '2019-06-19'
# start_time = '05:00:00'
# end_time = '11:00:00'
# intervals = ["WIECZÓR"]
# filtered = filter_data(data, day_type, start_day,end_day, intervals)
# print("Filtered data:")
# print(filtered['Start Time'])