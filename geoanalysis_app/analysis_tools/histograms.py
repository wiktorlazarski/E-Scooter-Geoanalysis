import datetime
import math

import numpy as np
import pandas as pd
from geoanalysis_app import constants as C
from matplotlib import pyplot as plt


def histogram_trip_length(data_df, bins_width):
    fig = plt.figure()

    max_distance = data_df["Trip Distance"].max()
    max_distance = math.ceil(max_distance)

    bins_list = np.arange(0, max_distance, bins_width).tolist()

    plt.hist(data_df["Trip Distance"], density=False, bins=bins_list)
    plt.xlim([0, max_distance])

    x_axis_interval = 1000 * (round(max_distance / 15000))
    plt.xticks(np.arange(0, max_distance, x_axis_interval), rotation=-30)

    # Add title and axis names
    # plt.title('Histogram długości przejechanych tras jednego przejazdu')
    plt.xlabel("długość przejazdów [m]")
    plt.ylabel("liczba przejazdów")

    # plt.show()

    return fig


def to_datatime(startingDate):
    data_time = datetime.datetime.strptime(startingDate, "%Y-%m-%dT%H:%M:%S.000")
    return data_time


def count_distance_per_hour(distances, start_time, end_time, distance, duration):
    start_time = to_datatime(start_time)
    end_time = to_datatime(end_time)
    duration_time = duration
    duration_time_hours = duration / 3600  # in hours
    duration_from_start_to_end = end_time.hour - start_time.hour

    if duration_time > 0:
        distance_per_second = distance / duration_time

        start_hour = start_time.hour
        end_hour = end_time.hour

        if duration_from_start_to_end == 0:
            if start_hour != 0:
                distances[start_hour] += (duration_time / 2) * distance_per_second
                distances[start_hour - 1] += (duration_time / 2) * distance_per_second
            else:
                distances[start_hour] += (duration_time / 2) * distance_per_second
                distances[23] += (duration_time / 2) * distance_per_second

        else:
            # same for every time interval
            if duration_time_hours < duration_from_start_to_end:
                start_hour_id = start_hour
                # if interval from 23:00 to 0:00
                end_hour_id = end_hour
                if end_hour == 0:
                    end_hour_id = 24

                while start_hour_id < end_hour_id:
                    distances[start_hour_id] += (
                        duration_time / duration_from_start_to_end
                    ) * distance_per_second
                    start_hour_id += 1

            else:
                time_left = duration_time - 3600 * duration_from_start_to_end
                start_hour_id = start_hour
                end_hour_id = end_hour
                # if interval from 23:00 to 0:00
                if end_hour == 0:
                    end_hour_id = 24

                while start_hour_id < end_hour:
                    distances[start_hour_id] += (
                        duration_time / duration_from_start_to_end
                    ) * distance_per_second
                    start_hour_id += 1

                # adherent intervals
                if start_hour != 0:
                    distances[start_hour - 1] += (time_left / 2) * distance_per_second
                else:
                    distances[23] += (time_left / 2) * distance_per_second
                distances[end_hour] += (time_left / 2) * distance_per_second

        return distances
    else:
        return distances


def histogram_distance_per_hour(data_df):
    distances = [0 for i in range(24)]

    for row in data_df.itertuples():
        start_time = row[1]
        end_time = row[2]
        distance = row[3]
        duration = row[4]
        distances = count_distance_per_hour(
            distances, start_time, end_time, distance, duration
        )

    distance_per_hours = list(
        zip([str(i) + ":00" + "-" + str(i + 1) + ":00" for i in range(24)], distances)
    )

    fig, ax = plt.subplots(1, 1)
    df = pd.DataFrame(distance_per_hours, columns=["time", "distance"])
    df.plot(kind="bar", x="time", ax=ax)
    plt.xlabel("czas w przedziałach godzinowych")
    plt.ylabel("suma długości przejazdów [m]")

    return fig
