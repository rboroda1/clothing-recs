# main.py

from flask import Flask, redirect, url_for, request
import pandas as pd
from functions import *
from getWeather import getWeather

# for later use -- when making a web app
app = Flask(__name__)

# importing csv file -- playing around with graphs + sorting
df = pd.read_csv('data.csv')
# print(df)
df.sort_values(["temperature"],
               axis=0,
               ascending=[True],
               inplace=True)


# making program a loop
repeat = "y"
while(repeat == "y"):
    # using weather api to actually get the weather conditions
    weatherStats = getWeather()
    # to check -- print('\n', weatherStats)
    autoTemp = kelvinToFahrenheit(weatherStats[0])
    autoPrecip = raining(weatherStats[1])
    print("\nCurrent weather stats:\nTemperature:",
          int(autoTemp), "\nPrecipitation:", autoPrecip)
    recommendClothes(autoTemp, autoPrecip)

    # ask if user wants to override the automatic reading
    override = None
    while override is None:
        try:
            override = input(
                "\nWould you like to enter a new place (y), exit (n) or input your own weather conditions (o)? ")
            if(override.lower() != 'y' and override.lower() != 'n' and override.lower() != 'o'):
                raise ValueError
            break
        except ValueError:
            print("Please input (y/n/o) only...")
            override = None
            continue

    # input if api overridden
    while(override.lower() == 'o'):
        temperatureCurrent = None
        while temperatureCurrent is None:
            try:
                temperatureCurrent = int(
                    input("\nWhat is the temperature today? (degrees F) "))
                break
            except ValueError:
                print("Please input integer only...")
                continue

        precipitationCurrent = None
        while precipitationCurrent is None:
            try:
                precipitationCurrent = input(
                    "Is there supposed to be precipitation? (yes/no) ")
                if(precipitationCurrent != 'yes' and precipitationCurrent != 'no'):
                    precipitationCurrent = None
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Please input (yes/no) only...")
                continue
        recommendClothes(temperatureCurrent, precipitationCurrent)

        override = None
        while override is None:
            try:
                override = input(
                    "\nWould you like to enter a new place (y) or exit (n) or input more own weather conditions (o)? ")
                if(override.lower() != 'y' and override.lower() != 'n' and override.lower() != 'o'):
                    raise ValueError
                break
            except ValueError:
                print("Please input (y/n/o) only...")
                override = None
                continue

    # to exit
    if(override.lower() == 'n'):
        break

# name = 'Rachel '
# @app.route('/')
# def success(name):
#     return 'welcome ' % name
