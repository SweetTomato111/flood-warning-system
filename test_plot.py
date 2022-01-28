"""Unit test for the plot module"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt

def test_plot_water_levels():
    """Requirements for Task 2E"""
    stations = build_station_list()
    update_water_levels(stations)
    station = stations[0] #randomly pick a station to plot
    dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=10))
    plot_water_levels(station, dates, levels)
    plt.close()